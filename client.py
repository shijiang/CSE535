import da
PatternExpr_0 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('replyTail'), da.pat.FreePattern('t')]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_1 = da.pat.FreePattern('m')
PatternExpr_3 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('getBalanceRep'), da.pat.TuplePattern([da.pat.FreePattern('acc'), da.pat.FreePattern('amount')])]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_4 = da.pat.FreePattern('t')
PatternExpr_6 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('replyTail'), da.pat.FreePattern('t')]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_7 = da.pat.FreePattern('m')
import sys
import random
import time


class Client(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._ClientReceivedEvent_0 = []
        self._ClientReceivedEvent_1 = []
        self._events.extend([
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_0', PatternExpr_0, sources=[PatternExpr_1], destinations=None, timestamps=None, record_history=True, handlers=[]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_1', PatternExpr_3, sources=[PatternExpr_4], destinations=None, timestamps=None, record_history=True, handlers=[]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_2', PatternExpr_6, sources=[PatternExpr_7], destinations=None, timestamps=None, record_history=None, handlers=[self._Client_handler_0])])

    def main(self):
        random.seed()
        n = random.randint(5, 10)
        time.sleep(n)
        self.output('query the tail\n')
        self.lc = self.logical_clock()
        self._send((('queryTail',), (self.lc, self.id)), self.head)
        m = t = rid = rlc = None

        def ExistentialOpExpr_0():
            nonlocal m, t, rid, rlc
            for (_, (_, _, m), ((_ConstantPattern16_, t), (rlc, rid))) in self._ClientReceivedEvent_0:
                if (_ConstantPattern16_ == 'replyTail'):
                    if True:
                        return True
            return False
        _st_label_16 = 0
        while (_st_label_16 == 0):
            _st_label_16+=1
            if ExistentialOpExpr_0():
                _st_label_16+=1
            else:
                super()._label('_st_label_16', block=True)
                _st_label_16-=1
        self.getBalance()
        self.output('client query the balance')
        amount = acc = rlc = t = rid = None

        def ExistentialOpExpr_1():
            nonlocal amount, acc, rlc, t, rid
            for (_, (_, _, t), ((_ConstantPattern39_, (acc, amount)), (rlc, rid))) in self._ClientReceivedEvent_1:
                if (_ConstantPattern39_ == 'getBalanceRep'):
                    if True:
                        return True
            return False
        _st_label_19 = 0
        while (_st_label_19 == 0):
            _st_label_19+=1
            if ExistentialOpExpr_1():
                self.output(('the amount is %s\n' % amount))
                _st_label_19+=1
            else:
                super()._label('_st_label_19', block=True)
                _st_label_19-=1

    def setup(self, head, accountNum):
        self.accountNum = accountNum
        self.head = head
        self.tail = 0
        self.lc = self.logical_clock()

    def getBalance(self):
        self.lc = self.logical_clock()
        self._send((('getBalance', (self.accountNum,)), (self.lc, self.id)), self.tail)

    def deposit(self, amount):
        self.lc = self.logical_clock()
        self._send((('deposit', (self.accountNum, amount)), (self.lc, id)), self.head)

    def _Client_handler_0(self, m, t, rid, rlc):
        self.tail = t
        self.output(('I got the tail %s\n' % self.head))
    _Client_handler_0._labels = None
    _Client_handler_0._notlabels = None
