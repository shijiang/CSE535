import da
PatternExpr_0 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('replyNeighbor'), da.pat.TuplePattern([da.pat.FreePattern('prev'), da.pat.FreePattern('next')])]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_1 = da.pat.FreePattern('master')
PatternExpr_3 = da.pat.TuplePattern([da.pat.ConstantPattern('terminate')])
PatternExpr_4 = da.pat.FreePattern('master')
PatternExpr_6 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('ping')]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('id')])])
PatternExpr_7 = da.pat.FreePattern('m')
PatternExpr_8 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('getBalance'), da.pat.TuplePattern([da.pat.FreePattern('accountNum')])]), da.pat.TuplePattern([da.pat.FreePattern('tlc'), da.pat.FreePattern('tid')])])
PatternExpr_9 = da.pat.FreePattern('p')
PatternExpr_10 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('deposit'), da.pat.TuplePattern([da.pat.FreePattern('accountNum'), da.pat.FreePattern('amount')])]), da.pat.TuplePattern([da.pat.FreePattern('tlc'), da.pat.FreePattern('tid')])])
PatternExpr_11 = da.pat.FreePattern('p')
PatternExpr_12 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('deposit'), da.pat.FreePattern('tSN')]), da.pat.TuplePattern([da.pat.FreePattern('accountNum'), da.pat.FreePattern('amount')])]), da.pat.TuplePattern([da.pat.FreePattern('tlc'), da.pat.FreePattern('tid')])])
PatternExpr_13 = da.pat.FreePattern('p')
PatternExpr_14 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('insuff'), da.pat.TuplePattern([da.pat.FreePattern('accountNum'), da.pat.FreePattern('amount')])]), da.pat.TuplePattern([da.pat.FreePattern('tlc'), da.pat.FreePattern('tid')])])
PatternExpr_15 = da.pat.FreePattern('p')
PatternExpr_16 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('ack'), da.pat.FreePattern('m')]), da.pat.TuplePattern([da.pat.FreePattern('tlc'), da.pat.FreePattern('tid')])])
PatternExpr_17 = da.pat.FreePattern('p')
PatternExpr_18 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('addServer'), da.pat.FreePattern('p')]), da.pat.TuplePattern([da.pat.FreePattern('lc'), da.pat.FreePattern('id')])])
PatternExpr_19 = da.pat.FreePattern('m')
PatternExpr_20 = da.pat.TuplePattern([da.pat.ConstantPattern('hist')])
PatternExpr_21 = da.pat.FreePattern('p')
PatternExpr_22 = da.pat.TuplePattern([da.pat.ConstantPattern('done')])
PatternExpr_23 = da.pat.FreePattern('p')
PatternExpr_24 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('pid')]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_25 = da.pat.FreePattern('m')
PatternExpr_26 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('replyNeighbor'), da.pat.TuplePattern([da.pat.FreePattern('prev'), da.pat.FreePattern('next')])]), da.pat.TuplePattern([da.pat.FreePattern('lc'), da.pat.FreePattern('id')])])
PatternExpr_27 = da.pat.FreePattern('m')
import sys
import random
import time


class Server(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._ServerReceivedEvent_0 = []
        self._ServerReceivedEvent_1 = []
        self._events.extend([
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_0', PatternExpr_0, sources=[PatternExpr_1], destinations=None, timestamps=None, record_history=True, handlers=[]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_1', PatternExpr_3, sources=[PatternExpr_4], destinations=None, timestamps=None, record_history=True, handlers=[]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_2', PatternExpr_6, sources=[PatternExpr_7], destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_0]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_3', PatternExpr_8, sources=[PatternExpr_9], destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_1]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_4', PatternExpr_10, sources=[PatternExpr_11], destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_2]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_5', PatternExpr_12, sources=[PatternExpr_13], destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_3]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_6', PatternExpr_14, sources=[PatternExpr_15], destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_4]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_7', PatternExpr_16, sources=[PatternExpr_17], destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_5]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_8', PatternExpr_18, sources=[PatternExpr_19], destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_6]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_9', PatternExpr_20, sources=[PatternExpr_21], destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_7]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_10', PatternExpr_22, sources=[PatternExpr_23], destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_8]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_11', PatternExpr_24, sources=[PatternExpr_25], destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_9]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_12', PatternExpr_26, sources=[PatternExpr_27], destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_10])])

    def main(self):
        random.seed()
        n = random.randint(0, 1)
        self.lc = self.logical_clock()
        self._send((('neighbor', self.bankName), (self.lc, self.id)), self.master)
        rlc = master = rid = next = prev = None

        def ExistentialOpExpr_0():
            nonlocal rlc, master, rid, next, prev
            for (_, (_, _, master), ((_ConstantPattern18_, (prev, next)), (rlc, rid))) in self._ServerReceivedEvent_0:
                if (_ConstantPattern18_ == 'replyNeighbor'):
                    if True:
                        return True
            return False
        _st_label_22 = 0
        while (_st_label_22 == 0):
            _st_label_22+=1
            if ExistentialOpExpr_0():
                _st_label_22+=1
            else:
                super()._label('_st_label_22', block=True)
                _st_label_22-=1
        self.output('sets the neighbor\n')
        while True:
            master = None

            def ExistentialOpExpr_1():
                nonlocal master
                for (_, (_, _, master), (_ConstantPattern35_,)) in self._ServerReceivedEvent_1:
                    if (_ConstantPattern35_ == 'terminate'):
                        if True:
                            return True
                return False
            _st_label_25 = 0
            while (_st_label_25 == 0):
                _st_label_25+=1
                if ExistentialOpExpr_1():
                    _st_label_25+=1
                else:
                    super()._label('_st_label_25', block=True)
                    _st_label_25-=1
            else:
                if (_st_label_25 != 2):
                    continue
            if (_st_label_25 != 2):
                break

    def setup(self, master, bankName, bank):
        self.bankName = bankName
        self.master = master
        self.bank = bank
        self.sentHist = []
        self.hist = []
        self.nextP = 0
        self.prevP = 0
        self.isHead = False
        self.isTail = False
        self.SN = 0
        self.isWaitForProcessedTransfer = False
        self.lc = self.logical_clock()
        self.probDrop = 0.2

    def _Server_handler_0(self, rlc, m, id):
        self.lc = self.logical_clock()
        self._send((('reply',), (self.lc, self.id)), m)
    _Server_handler_0._labels = None
    _Server_handler_0._notlabels = None

    def _Server_handler_1(self, accountNum, tid, tlc, p):
        if self.isTail:
            r = random.random()
            if (r > self.probDrop):
                self.lc = self.logical_clock()
                self._send((('getBalanceRep', (accountNum, 
                self.bank.getBalance(accountNum))), (self.lc, self.id)), p)
        else:
            self.output('im not the tail\n')
    _Server_handler_1._labels = None
    _Server_handler_1._notlabels = None

    def _Server_handler_2(self, accountNum, tid, tlc, p, amount):
        if self.isHead:
            self.SN+=1
            if (not (((('deposit', self.SN), (accountNum, amount)), (tlc, tid)) in self.sentHist)):
                if ((self.bank.getBalance(accountNum) + amount) > 0):
                    self._send(((('deposit', self.SN), (accountNum, amount)), (tlc, tid)), self.id)
                    self.sentHist.append(((('deposit', self.SN), (accountNum, amount)), (tlc, tid)))
                    self.bank.deposit(accountNum, amount)
                else:
                    self.output('send insuff\n')
                    self._send((('insuff', (accountNum, amount)), (tlc, tid)), self.nextP)
            else:
                self._send(((('deposit', self.SN), (accountNum, amount)), (tlc, tid)), self.nextP)
    _Server_handler_2._labels = None
    _Server_handler_2._notlabels = None

    def _Server_handler_3(self, tSN, tid, accountNum, amount, p, tlc):
        if (tSN >= self.SN):
            self.SN = tSN
            if (not self.isWaitForProcessedTransfer):
                if (not (((('deposit', tSN), (accountNum, amount)), (tlc, tid)) in self.sentHist)):
                    self.bank.deposit(accountNum, amount)
                    self.sentHist.append(((('deposit', tSN), (accountNum, amount)), (tlc, tid)))
                    if self.isTail:
                        self.lc = self.logical_clock()
                        self._send((('getBalanceRep', (accountNum, 
                        self.bank.getBalance(accountNum))), (self.lc, self.id)), tid)
                        self.sentHist.remove(((('deposit', tSN), (accountNum, amount)), (tlc, tid)))
                        self.hist.append(((('deposit', tSN), (accountNum, amount)), (tlc, tid)))
                        self.lc = self.logical_clock()
                        self._send((('ack', ((('deposit', tSN), (accountNum, amount)), (tlc, tid))), (self.lc, self.id)), self.prevP)
                    else:
                        self.lc = self.logical_clock()
                        self._send(((('deposit', tSN), (accountNum, amount)), (tlc, tid)), self.nextP)
                elif self.isTail:
                    self.lc = self.logical_clock()
                    self._send((('getBalanceRep', (accountNum, 
                    self.bank.getBalance(accountNum))), (self.lc, self.id)), tid)
                else:
                    print(self.nextP)
                    self.lc = self.logical_clock()
                    self._send(((('deposit', self.SN), (accountNum, amount)), (tlc, tid)), self.nextP)
            elif self.isTail:
                self.lc = self.logical_clock()
                self._send((('getBalanceRep', (accountNum, 
                self.bank.getBalance(accountNum))), (self.lc, self.id)), tid)
    _Server_handler_3._labels = None
    _Server_handler_3._notlabels = None

    def _Server_handler_4(self, tlc, amount, accountNum, p, tid):
        if self.isTail:
            self.output('tail send insuff\n')
            self.lc = self.logical_clock()
            self._send((('insuff', (accountNum, amount)), (self.lc, self.id)), tid)
        else:
            self._send((('insuff', (accountNum, amount)), (tlc, tid)), self.nextP)
    _Server_handler_4._labels = None
    _Server_handler_4._notlabels = None

    def _Server_handler_5(self, tlc, p, m, tid):
        self.sentHist.remove(m)
        self.hist.append(m)
        if (not self.isHead):
            self._send((('ack', m), (self.lc, self.id)), self.prevP)
    _Server_handler_5._labels = None
    _Server_handler_5._notlabels = None

    def _Server_handler_6(self, p, id, lc, m):
        self._send(('hist',), p)
    _Server_handler_6._labels = None
    _Server_handler_6._notlabels = None

    def _Server_handler_7(self, p):
        self.isTail = True
        self.isWaitForProcessedTransfer = True
        self._send(('done',), (self.master, p))
    _Server_handler_7._labels = None
    _Server_handler_7._notlabels = None

    def _Server_handler_8(self, p):
        self.isTail = False
    _Server_handler_8._labels = None
    _Server_handler_8._notlabels = None

    def _Server_handler_9(self, rlc, m, rid):
        self.lc = self.logical_clock()
        self._send((('replyPid',), (self.lc, self.id)), self.master)
    _Server_handler_9._labels = None
    _Server_handler_9._notlabels = None

    def _Server_handler_10(self, next, prev, lc, id, m):
        self.nextP = next
        self.prevP = prev
        if (self.nextP == self.id):
            self.isTail = True
        if (self.prevP == self.id):
            self.isHead = True
    _Server_handler_10._labels = None
    _Server_handler_10._notlabels = None
