import da
PatternExpr_0 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('replyHead'), da.pat.TuplePattern([da.pat.FreePattern('h'), da.pat.FreePattern('t')])]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('id')])])
PatternExpr_1 = da.pat.FreePattern('m')
PatternExpr_3 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('getBalanceRep'), da.pat.TuplePattern([da.pat.FreePattern('acc'), da.pat.FreePattern('amount')])]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_4 = da.pat.FreePattern('t')
PatternExpr_6 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('getBalanceRep'), da.pat.TuplePattern([da.pat.FreePattern('acc'), da.pat.FreePattern('amount')])]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_7 = da.pat.FreePattern('t')
PatternExpr_9 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('getBalanceRep'), da.pat.TuplePattern([da.pat.FreePattern('acc'), da.pat.FreePattern('amount')])]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_10 = da.pat.FreePattern('t')
PatternExpr_12 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('replyHead'), da.pat.TuplePattern([da.pat.FreePattern('h'), da.pat.FreePattern('t')])]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_13 = da.pat.FreePattern('m')
import sys
import random
import time


class Client(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._ClientReceivedEvent_0 = []
        self._ClientReceivedEvent_1 = []
        self._ClientReceivedEvent_2 = []
        self._ClientReceivedEvent_3 = []
        self._events.extend([
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_0', PatternExpr_0, sources=[PatternExpr_1], destinations=None, timestamps=None, record_history=True, handlers=[]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_1', PatternExpr_3, sources=[PatternExpr_4], destinations=None, timestamps=None, record_history=True, handlers=[]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_2', PatternExpr_6, sources=[PatternExpr_7], destinations=None, timestamps=None, record_history=True, handlers=[]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_3', PatternExpr_9, sources=[PatternExpr_10], destinations=None, timestamps=None, record_history=True, handlers=[]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_4', PatternExpr_12, sources=[PatternExpr_13], destinations=None, timestamps=None, record_history=None, handlers=[self._Client_handler_0])])

    def main(self):
        random.seed()
        n = random.randint(5, 10)
        time.sleep(n)
        self.lc = self.logical_clock()
        self._send((('head', self.chainNum), (self.lc, self.id)), self.m)
        self.output('client query the head\n')
        t = h = rlc = id = m = None

        def ExistentialOpExpr_0():
            nonlocal t, h, rlc, id, m
            for (_, (_, _, m), ((_ConstantPattern18_, (h, t)), (rlc, id))) in self._ClientReceivedEvent_0:
                if (_ConstantPattern18_ == 'replyHead'):
                    if True:
                        return True
            return False
        _st_label_17 = 0
        while (_st_label_17 == 0):
            _st_label_17+=1
            if ExistentialOpExpr_0():
                _st_label_17+=1
            else:
                super()._label('_st_label_17', block=True)
                _st_label_17-=1
        self.getBalance()
        acc = rlc = rid = t = amount = None

        def ExistentialOpExpr_1():
            nonlocal acc, rlc, rid, t, amount
            for (_, (_, _, t), ((_ConstantPattern43_, (acc, amount)), (rlc, rid))) in self._ClientReceivedEvent_1:
                if (_ConstantPattern43_ == 'getBalanceRep'):
                    if True:
                        return True
            return False
        _st_label_19 = 0
        while (_st_label_19 == 0):
            _st_label_19+=1
            if ExistentialOpExpr_1():
                self.output(('%s has amount of %s\n' % (acc, amount)))
                _st_label_19+=1
            else:
                super()._label('_st_label_19', block=True)
                _st_label_19-=1
        self.deposit(400)
        rlc = t = amount = rid = acc = None

        def ExistentialOpExpr_2():
            nonlocal rlc, t, amount, rid, acc
            for (_, (_, _, t), ((_ConstantPattern68_, (acc, amount)), (rlc, rid))) in self._ClientReceivedEvent_2:
                if (_ConstantPattern68_ == 'getBalanceRep'):
                    if (rlc > self.lc):
                        return True
            return False
        _st_label_22 = 0
        while (_st_label_22 == 0):
            _st_label_22+=1
            if ExistentialOpExpr_2():
                self.output(('the new amount is %s\n' % amount))
                _st_label_22+=1
            else:
                super()._label('_st_label_22', block=True)
                _st_label_22-=1
        self.deposit((-300))
        t = acc = amount = rlc = rid = None

        def ExistentialOpExpr_3():
            nonlocal t, acc, amount, rlc, rid
            for (_, (_, _, t), ((_ConstantPattern93_, (acc, amount)), (rlc, rid))) in self._ClientReceivedEvent_3:
                if (_ConstantPattern93_ == 'getBalanceRep'):
                    if (rlc > self.lc):
                        return True
            return False
        _st_label_25 = 0
        while (_st_label_25 == 0):
            _st_label_25+=1
            if ExistentialOpExpr_3():
                self.output(('the new amount is %s\n' % amount))
                _st_label_25+=1
            else:
                super()._label('_st_label_25', block=True)
                _st_label_25-=1

    def setup(self, m, chainNum, accountNum):
        self.m = m
        self.chainNum = chainNum
        self.accountNum = accountNum
        self.head = 0
        self.tail = 0
        self.lc = self.logical_clock()

    def getBalance(self):
        self.lc = self.logical_clock()
        self._send((('getBalance', (self.accountNum,)), (self.lc, self.id)), self.tail)

    def deposit(self, amount):
        self.lc = self.logical_clock()
        self._send((('deposit', (self.accountNum, amount)), (self.lc, self.id)), self.head)

    def _Client_handler_0(self, m, t, h, rlc, rid):
        self.head = h
        self.tail = t
        self.output(('I got the head %s\n' % self.head))
    _Client_handler_0._labels = None
    _Client_handler_0._notlabels = None
