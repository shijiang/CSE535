import da
PatternExpr_0 = da.pat.TuplePattern([da.pat.ConstantPattern('replyHead'), da.pat.TuplePattern([da.pat.FreePattern('h'), da.pat.FreePattern('t')])])
PatternExpr_1 = da.pat.FreePattern('m')
PatternExpr_3 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('getBalanceRep'), da.pat.TuplePattern([da.pat.FreePattern('acc'), da.pat.FreePattern('amount')])]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('id')])])
PatternExpr_4 = da.pat.FreePattern('t')
PatternExpr_6 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('replyHead')]), da.pat.TuplePattern([da.pat.FreePattern('h'), da.pat.FreePattern('t')])])
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
        n = random.randint(0, 6)
        time.sleep(n)
        self._send((('head', self.chainNum), self.id), self.m)
        m = t = h = None

        def ExistentialOpExpr_0():
            nonlocal m, t, h
            for (_, (_, _, m), (_ConstantPattern13_, (h, t))) in self._ClientReceivedEvent_0:
                if (_ConstantPattern13_ == 'replyHead'):
                    if True:
                        return True
            return False
        _st_label_15 = 0
        while (_st_label_15 == 0):
            _st_label_15+=1
            if ExistentialOpExpr_0():
                _st_label_15+=1
            else:
                super()._label('_st_label_15', block=True)
                _st_label_15-=1
        self.getBalance()
        rlc = t = amount = id = acc = None

        def ExistentialOpExpr_1():
            nonlocal rlc, t, amount, id, acc
            for (_, (_, _, t), ((_ConstantPattern35_, (acc, amount)), (rlc, id))) in self._ClientReceivedEvent_1:
                if (_ConstantPattern35_ == 'getBalanceRep'):
                    if ((t == self.tail) and ((rlc, id) > (self.lc, id))):
                        return True
            return False
        _st_label_17 = 0
        self._timer_start()
        while (_st_label_17 == 0):
            _st_label_17+=1
            if ExistentialOpExpr_1():
                print(amount)
                _st_label_17+=1
            elif self._timer_expired:
                print('query head')
                _st_label_17+=1
            else:
                super()._label('_st_label_17', block=True, timeout=2)
                _st_label_17-=1

    def setup(self, m, chainNum, accountNum):
        self.chainNum = chainNum
        self.m = m
        self.accountNum = accountNum
        self.head = 0
        self.tail = 0
        self.lc = self.logical_clock()

    def getBalance(self):
        self.lc = self.logical_clock()
        self._send((('getBalance', (self.accountNum,)), (self.lc, self.id)), self.tail)

    def deposit(self, amount):
        self.lc = self.logical_clock()
        self._send((('deposit', (self.accountNum, amount)), (self.lc, id)), self.head)

    def _Client_handler_0(self, t, h, m):
        self.head = h
        self.tail = t
    _Client_handler_0._labels = None
    _Client_handler_0._notlabels = None
