import da
PatternExpr_0 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('replyHead'), da.pat.TuplePattern([da.pat.FreePattern('h'), da.pat.FreePattern('t')])]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('id')])])
PatternExpr_1 = da.pat.FreePattern('m')
PatternExpr_3 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('getBalanceRep'), da.pat.TuplePattern([da.pat.FreePattern('acc'), da.pat.FreePattern('amount')])]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_4 = da.pat.FreePattern('t')
PatternExpr_6 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('getBalanceRep'), da.pat.TuplePattern([da.pat.FreePattern('acc'), da.pat.FreePattern('amount')])]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_7 = da.pat.FreePattern('t')
PatternExpr_9 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('insuff'), da.pat.TuplePattern([da.pat.FreePattern('acc'), da.pat.FreePattern('amount')])]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
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
        random.seed(self.seed)
        n = random.randint(5, 10)
        time.sleep(n)
        self.retrans = True
        while self.retrans:
            self.lc = self.logical_clock()
            self._send((('head', self.bankName), (self.lc, self.id)), self.m)
            self.output(('client %i query the head for %s\n' % (self.accountNum, self.bankName)))
            m = t = h = rlc = id = None

            def ExistentialOpExpr_0():
                nonlocal m, t, h, rlc, id
                for (_, (_, _, m), ((_ConstantPattern18_, (h, t)), (rlc, id))) in self._ClientReceivedEvent_0:
                    if (_ConstantPattern18_ == 'replyHead'):
                        if (rlc > self.lc):
                            return True
                return False
            _st_label_23 = 0
            self._timer_start()
            while (_st_label_23 == 0):
                _st_label_23+=1
                if ExistentialOpExpr_0():
                    self.retrans = False
                    _st_label_23+=1
                elif self._timer_expired:
                    pass
                    _st_label_23+=1
                else:
                    super()._label('_st_label_23', block=True, timeout=self.waitingTime)
                    _st_label_23-=1
            else:
                if (_st_label_23 != 2):
                    continue
            if (_st_label_23 != 2):
                break
        while (self.numReq > 0):
            r = random.random()
            if (r < self.probs[0]):
                self.getBalance()
                t = amount = acc = rlc = rid = None

                def ExistentialOpExpr_1():
                    nonlocal t, amount, acc, rlc, rid
                    for (_, (_, _, t), ((_ConstantPattern43_, (acc, amount)), (rlc, rid))) in self._ClientReceivedEvent_1:
                        if (_ConstantPattern43_ == 'getBalanceRep'):
                            if (rlc > self.lc):
                                return True
                    return False
                _st_label_30 = 0
                self._timer_start()
                while (_st_label_30 == 0):
                    _st_label_30+=1
                    if ExistentialOpExpr_1():
                        self.output(('%s has amount of %s\n' % (acc, amount)))
                        _st_label_30+=1
                    elif self._timer_expired:
                        self.output('get balance timeout\n')
                        _st_label_30+=1
                    else:
                        super()._label('_st_label_30', block=True, timeout=self.waitingTime)
                        _st_label_30-=1
                else:
                    if (_st_label_30 != 2):
                        continue
                if (_st_label_30 != 2):
                    break
            elif ((r > self.probs[0]) and (r < (self.probs[0] + self.probs[1]))):
                amount = random.randint(self.nmax, self.pmax)
                self.deposit(amount)
                acc = rlc = rid = t = amount = None

                def ExistentialOpExpr_2():
                    nonlocal acc, rlc, rid, t, amount
                    for (_, (_, _, t), ((_ConstantPattern68_, (acc, amount)), (rlc, rid))) in self._ClientReceivedEvent_2:
                        if (_ConstantPattern68_ == 'getBalanceRep'):
                            if (rlc > self.lc):
                                return True
                    return False
                rid = rlc = acc = amount = t = None

                def ExistentialOpExpr_3():
                    nonlocal rid, rlc, acc, amount, t
                    for (_, (_, _, t), ((_ConstantPattern93_, (acc, amount)), (rlc, rid))) in self._ClientReceivedEvent_3:
                        if (_ConstantPattern93_ == 'insuff'):
                            if (rlc > self.lc):
                                return True
                    return False
                _st_label_36 = 0
                self._timer_start()
                while (_st_label_36 == 0):
                    _st_label_36+=1
                    if ExistentialOpExpr_2():
                        self.output(('%s has new amount is %s\n' % (acc, amount)))
                        _st_label_36+=1
                    elif ExistentialOpExpr_3():
                        self.output(('%s withdraw insufficient amount of %s\n' % (acc, amount)))
                        _st_label_36+=1
                    elif self._timer_expired:
                        self.output('deposit timeout\n')
                        _st_label_36+=1
                    else:
                        super()._label('_st_label_36', block=True, timeout=(self.waitingTime * 10))
                        _st_label_36-=1
                else:
                    if (_st_label_36 != 2):
                        continue
                if (_st_label_36 != 2):
                    break
            else:
                self.output(('%s transfer\n' % self.accountNum))
            self.numReq-=1

    def setup(self, m, bankName, accountNum, seed, numReq, probs):
        self.m = m
        self.numReq = numReq
        self.probs = probs
        self.accountNum = accountNum
        self.seed = seed
        self.bankName = bankName
        self.head = 0
        self.tail = 0
        self.lc = self.logical_clock()
        self.pmax = 5
        self.nmax = (-500)
        self.waitingTime = 10
        self.retrans = True

    def getBalance(self):
        self.lc = self.logical_clock()
        self._send((('getBalance', (self.accountNum,)), (self.lc, self.id)), self.tail)

    def deposit(self, amount):
        self.lc = self.logical_clock()
        self._send((('deposit', (self.accountNum, amount)), (self.lc, self.id)), self.head)

    def _Client_handler_0(self, m, t, h, rlc, rid):
        self.head = h
        self.tail = t
        self.output(('client %s got the head %s\n' % (self.accountNum, self.head)))
    _Client_handler_0._labels = None
    _Client_handler_0._notlabels = None
