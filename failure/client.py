import da
PatternExpr_0 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('replyHead'), da.pat.TuplePattern([da.pat.FreePattern('h'), da.pat.FreePattern('t')])]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('id')])])
PatternExpr_1 = da.pat.FreePattern('m')
PatternExpr_3 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('createRep'), da.pat.TuplePattern([da.pat.FreePattern('acc'), da.pat.FreePattern('amount')])]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_4 = da.pat.FreePattern('m')
PatternExpr_6 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('createRep'), da.pat.TuplePattern([da.pat.FreePattern('acc'), da.pat.FreePattern('amount')])]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_7 = da.pat.FreePattern('m')
PatternExpr_8 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('replyHead'), da.pat.TuplePattern([da.pat.FreePattern('h'), da.pat.FreePattern('t')])]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_9 = da.pat.FreePattern('m')
PatternExpr_10 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('getBalanceRep'), da.pat.TuplePattern([da.pat.FreePattern('acc'), da.pat.FreePattern('amount')])]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_11 = da.pat.FreePattern('t')
PatternExpr_13 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('getBalanceRep'), da.pat.TuplePattern([da.pat.FreePattern('acc'), da.pat.FreePattern('amount')])]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_14 = da.pat.FreePattern('t')
PatternExpr_16 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('insuff'), da.pat.TuplePattern([da.pat.FreePattern('acc'), da.pat.FreePattern('amount')])]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_17 = da.pat.FreePattern('t')
PatternExpr_19 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('getBalanceRep'), da.pat.TuplePattern([da.pat.FreePattern('acc'), da.pat.FreePattern('amount')])]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_20 = da.pat.FreePattern('t')
PatternExpr_22 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('insuff'), da.pat.TuplePattern([da.pat.FreePattern('acc'), da.pat.FreePattern('amount')])]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_23 = da.pat.FreePattern('t')
PatternExpr_25 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('inconsistHist'), da.pat.TuplePattern([da.pat.FreePattern('acc'), da.pat.FreePattern('amount')])]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_26 = da.pat.FreePattern('t')
PatternExpr_28 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('getBalance'), da.pat.TuplePattern([da.pat.FreePattern('acc'), da.pat.FreePattern('amount')])]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_29 = da.pat.FreePattern('t')
import sys
import random
import time
import logging


class Client(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._ClientReceivedEvent_0 = []
        self._ClientReceivedEvent_1 = []
        self._ClientReceivedEvent_4 = []
        self._ClientReceivedEvent_5 = []
        self._ClientReceivedEvent_6 = []
        self._ClientReceivedEvent_7 = []
        self._ClientReceivedEvent_8 = []
        self._ClientReceivedEvent_9 = []
        self._ClientReceivedEvent_10 = []
        self._events.extend([
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_0', PatternExpr_0, sources=[PatternExpr_1], destinations=None, timestamps=None, record_history=True, handlers=[]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_1', PatternExpr_3, sources=[PatternExpr_4], destinations=None, timestamps=None, record_history=True, handlers=[]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_2', PatternExpr_6, sources=[PatternExpr_7], destinations=None, timestamps=None, record_history=None, handlers=[self._Client_handler_0]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_3', PatternExpr_8, sources=[PatternExpr_9], destinations=None, timestamps=None, record_history=None, handlers=[self._Client_handler_1]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_4', PatternExpr_10, sources=[PatternExpr_11], destinations=None, timestamps=None, record_history=True, handlers=[]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_5', PatternExpr_13, sources=[PatternExpr_14], destinations=None, timestamps=None, record_history=True, handlers=[]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_6', PatternExpr_16, sources=[PatternExpr_17], destinations=None, timestamps=None, record_history=True, handlers=[]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_7', PatternExpr_19, sources=[PatternExpr_20], destinations=None, timestamps=None, record_history=True, handlers=[]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_8', PatternExpr_22, sources=[PatternExpr_23], destinations=None, timestamps=None, record_history=True, handlers=[]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_9', PatternExpr_25, sources=[PatternExpr_26], destinations=None, timestamps=None, record_history=True, handlers=[]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_10', PatternExpr_28, sources=[PatternExpr_29], destinations=None, timestamps=None, record_history=True, handlers=[])])

    def main(self):
        random.seed(self.seed)
        n = random.randint(5, 10)
        time.sleep(n)
        retrans = True
        counter = self.resendingTime
        while (retrans and (counter > 0)):
            retrans = self.resending
            self.lc = self.logical_clock()
            self._send((('head', self.bankName), (self.lc, self.id)), self.m)
            self.logger.info(('client %i query the head for %s\n' % (self.accountNum, self.bankName)))
            m = h = t = rlc = id = None

            def ExistentialOpExpr_0():
                nonlocal m, h, t, rlc, id
                for (_, (_, _, m), ((_ConstantPattern18_, (h, t)), (rlc, id))) in self._ClientReceivedEvent_0:
                    if (_ConstantPattern18_ == 'replyHead'):
                        if (rlc > self.lc):
                            return True
                return False
            _st_label_25 = 0
            self._timer_start()
            while (_st_label_25 == 0):
                _st_label_25+=1
                if ExistentialOpExpr_0():
                    retrans = False
                    _st_label_25+=1
                elif self._timer_expired:
                    counter-=1
                    _st_label_25+=1
                else:
                    super()._label('_st_label_25', block=True, timeout=self.waitingTime)
                    _st_label_25-=1
            else:
                if (_st_label_25 != 2):
                    continue
            if (_st_label_25 != 2):
                break
        if (self.head == 0):
            self.logger.info(('client %i fail to find head\n terminate\n' % self.accountNum))
            return 
        if (self.accountNum == 0):
            retrans = True
            counter = self.resendingTime
            while (retrans and (counter > 0)):
                retrans = self.resending
                self.lc = self.logical_clock()
                amount = random.randint(1, self.pmax)
                self._send((('createAcc', amount), (self.lc, self.id)), self.head)
                self.logger.info(('client %i create acc at %s\n' % (self.accountNum, self.bankName)))
                m = acc = amount = rlc = rid = None

                def ExistentialOpExpr_1():
                    nonlocal m, acc, amount, rlc, rid
                    for (_, (_, _, m), ((_ConstantPattern43_, (acc, amount)), (rlc, rid))) in self._ClientReceivedEvent_1:
                        if (_ConstantPattern43_ == 'createRep'):
                            if (rlc > self.lc):
                                return True
                    return False
                _st_label_40 = 0
                self._timer_start()
                while (_st_label_40 == 0):
                    _st_label_40+=1
                    if ExistentialOpExpr_1():
                        retrans = False
                        _st_label_40+=1
                    elif self._timer_expired:
                        counter-=1
                        _st_label_40+=1
                    else:
                        super()._label('_st_label_40', block=True, timeout=self.waitingTime)
                        _st_label_40-=1
                else:
                    if (_st_label_40 != 2):
                        continue
                if (_st_label_40 != 2):
                    break
        if (self.accountNum == 0):
            self.logger.info(('client %i fail to create acc at %s\n terminate\n' % (self.accountNum, self.bankName)))
            return 
        hasSeq = False
        if (len(self.clientSequence) == 0):
            hasSeq = False
        else:
            hasSeq = True
        if (hasSeq == True):
            for n in range(0, len(self.clientSequence)):
                if (self.clientSequence[n] == 1):
                    if (not self.getBalance()):
                        self.logger.info(('%s head failed while deposit\n' % self.accountNum))
                elif (self.clientSequence[n] == 2):
                    if (not self.depositWithSN(self.clientSN[n])):
                        self.logger.info(('%s transfer\n' % self.accountNum))
                else:
                    self.logger.info(('%s transfer\n' % self.accountNum))
        while ((self.numReq > 0) and (hasSeq == False)):
            r = random.random()
            if (r < self.probs[0]):
                if (not self.getBalance()):
                    self.logger.info(('%s head failed while query for balance\n' % self.accountNum))
            elif ((r > self.probs[0]) and (r < (self.probs[0] + self.probs[1]))):
                if (not self.deposit()):
                    self.logger.info(('%s head failed while deposit\n' % self.accountNum))
            else:
                self.logger.info(('%s transfer\n' % self.accountNum))
            self.numReq-=1

    def setup(self, m, bankName, accountNum, seed, numReq, probs, waitingTime, resending, resendingTime, clientSequence, clientSN):
        self.resending = resending
        self.clientSN = clientSN
        self.probs = probs
        self.waitingTime = waitingTime
        self.seed = seed
        self.accountNum = accountNum
        self.resendingTime = resendingTime
        self.clientSequence = clientSequence
        self.numReq = numReq
        self.m = m
        self.bankName = bankName
        self.head = 0
        self.tail = 0
        self.lc = self.logical_clock()
        self.pmax = 5
        self.nmax = (-500)
        self.logger = logging.getLogger('')

    def getBalance(self):
        retrans = True
        counter = self.resendingTime
        while (retrans and (counter > 0)):
            retrans = self.resending
            self.lc = self.logical_clock()
            self._send((('getBalance', (self.accountNum,)), (self.lc, self.id)), self.tail)
            self.logger.info(('%s query for balance\n' % self.accountNum))
            t = amount = acc = rlc = rid = None

            def ExistentialOpExpr_2():
                nonlocal t, amount, acc, rlc, rid
                for (_, (_, _, t), ((_ConstantPattern88_, (acc, amount)), (rlc, rid))) in self._ClientReceivedEvent_4:
                    if (_ConstantPattern88_ == 'getBalanceRep'):
                        if (rlc > self.lc):
                            return True
                return False
            _st_label_84 = 0
            self._timer_start()
            while (_st_label_84 == 0):
                _st_label_84+=1
                if ExistentialOpExpr_2():
                    self.logger.info(('%s has amount of %s\n' % (acc, amount)))
                    retrans = False
                    return True
                    _st_label_84+=1
                elif self._timer_expired:
                    counter-=1
                    self.logger.info(('%s get balance timeout\n' % self.accountNum))
                    _st_label_84+=1
                else:
                    super()._label('_st_label_84', block=True, timeout=self.waitingTime)
                    _st_label_84-=1
            else:
                if (_st_label_84 != 2):
                    continue
            if (_st_label_84 != 2):
                break
        return False

    def deposit(self):
        amount = random.randint(self.nmax, self.pmax)
        retrans = True
        counter = self.resendingTime
        while (retrans and (counter > 0)):
            retrans = self.resending
            self.lc = self.logical_clock()
            self._send((('deposit', (self.accountNum, amount)), (self.lc, self.id)), self.head)
            self.logger.info(('%s deposit for amount of %i' % (self.accountNum, amount)))
            rlc = acc = t = amount = rid = None

            def ExistentialOpExpr_3():
                nonlocal rlc, acc, t, amount, rid
                for (_, (_, _, t), ((_ConstantPattern113_, (acc, amount)), (rlc, rid))) in self._ClientReceivedEvent_5:
                    if (_ConstantPattern113_ == 'getBalanceRep'):
                        if (rlc > self.lc):
                            return True
                return False
            rlc = amount = t = acc = rid = None

            def ExistentialOpExpr_4():
                nonlocal rlc, amount, t, acc, rid
                for (_, (_, _, t), ((_ConstantPattern138_, (acc, amount)), (rlc, rid))) in self._ClientReceivedEvent_6:
                    if (_ConstantPattern138_ == 'insuff'):
                        if (rlc > self.lc):
                            return True
                return False
            _st_label_100 = 0
            self._timer_start()
            while (_st_label_100 == 0):
                _st_label_100+=1
                if ExistentialOpExpr_3():
                    self.logger.info(('%s has new amount is %s\n' % (acc, amount)))
                    retrans = False
                    return True
                    _st_label_100+=1
                elif ExistentialOpExpr_4():
                    self.logger.info(('%s withdraw insufficient amount of %s\n' % (acc, amount)))
                    retrans = False
                    return True
                    _st_label_100+=1
                elif self._timer_expired:
                    counter-=1
                    self.logger.info(('%s deposit timeout\n' % self.accountNum))
                    _st_label_100+=1
                else:
                    super()._label('_st_label_100', block=True, timeout=(self.waitingTime * 2))
                    _st_label_100-=1
            else:
                if (_st_label_100 != 2):
                    continue
            if (_st_label_100 != 2):
                break
        return False

    def depositWithSN(self, SN):
        amount = random.randint(self.nmax, self.pmax)
        retrans = True
        counter = self.resendingTime
        while (retrans and (counter > 0)):
            retrans = self.resending
            self.lc = self.logical_clock()
            self._send(((('deposit', SN), (self.accountNum, amount)), (self.lc, self.id)), self.head)
            self.logger.info(('***%s deposit for amount of %i with SN %i\n' % (self.accountNum, amount, SN)))
            rlc = amount = t = acc = rid = None

            def ExistentialOpExpr_5():
                nonlocal rlc, amount, t, acc, rid
                for (_, (_, _, t), ((_ConstantPattern163_, (acc, amount)), (rlc, rid))) in self._ClientReceivedEvent_7:
                    if (_ConstantPattern163_ == 'getBalanceRep'):
                        if (rlc > self.lc):
                            return True
                return False
            t = amount = acc = rlc = rid = None

            def ExistentialOpExpr_6():
                nonlocal t, amount, acc, rlc, rid
                for (_, (_, _, t), ((_ConstantPattern188_, (acc, amount)), (rlc, rid))) in self._ClientReceivedEvent_8:
                    if (_ConstantPattern188_ == 'insuff'):
                        if (rlc > self.lc):
                            return True
                return False
            rlc = t = acc = rid = amount = None

            def ExistentialOpExpr_7():
                nonlocal rlc, t, acc, rid, amount
                for (_, (_, _, t), ((_ConstantPattern213_, (acc, amount)), (rlc, rid))) in self._ClientReceivedEvent_9:
                    if (_ConstantPattern213_ == 'inconsistHist'):
                        if (rlc > self.lc):
                            return True
                return False
            t = amount = acc = rid = rlc = None

            def ExistentialOpExpr_8():
                nonlocal t, amount, acc, rid, rlc
                for (_, (_, _, t), ((_ConstantPattern238_, (acc, amount)), (rlc, rid))) in self._ClientReceivedEvent_10:
                    if (_ConstantPattern238_ == 'getBalance'):
                        if (rlc > self.lc):
                            return True
                return False
            _st_label_119 = 0
            self._timer_start()
            while (_st_label_119 == 0):
                _st_label_119+=1
                if ExistentialOpExpr_5():
                    self.logger.info(('***%s has new amount is %s\n' % (acc, amount)))
                    retrans = False
                    return True
                    _st_label_119+=1
                elif ExistentialOpExpr_6():
                    self.logger.info(('***%s withdraw insufficient amount of %s\n' % (acc, amount)))
                    retrans = False
                    return True
                    _st_label_119+=1
                elif ExistentialOpExpr_7():
                    retrans = False
                    return True
                    _st_label_119+=1
                elif ExistentialOpExpr_8():
                    retrans = False
                    self.logger.info(('***%s has duplicate request with SN %i\n' % (self.accountNum, SN)))
                    return True
                    _st_label_119+=1
                elif self._timer_expired:
                    counter-=1
                    self.logger.info(('***%s deposit timeout with SN %i\n' % (self.accountNum, SN)))
                    _st_label_119+=1
                else:
                    super()._label('_st_label_119', block=True, timeout=(self.waitingTime * 2))
                    _st_label_119-=1
            else:
                if (_st_label_119 != 2):
                    continue
            if (_st_label_119 != 2):
                break
        return False

    def _Client_handler_0(self, m, amount, acc, rlc, rid):
        self.accountNum = acc
        self.logger.info(('client %s created acct with amount %s' % (acc, amount)))
    _Client_handler_0._labels = None
    _Client_handler_0._notlabels = None

    def _Client_handler_1(self, t, h, rid, rlc, m):
        self.head = h
        self.tail = t
        self.logger.info(('client %s got the head %s\n' % (self.accountNum, self.head)))
    _Client_handler_1._labels = None
    _Client_handler_1._notlabels = None
