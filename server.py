import da
PatternExpr_0 = da.pat.TuplePattern([da.pat.ConstantPattern('terminate')])
PatternExpr_1 = da.pat.FreePattern('m')
PatternExpr_3 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('ping')]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('id')])])
PatternExpr_4 = da.pat.FreePattern('m')
PatternExpr_5 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('getBalance'), da.pat.TuplePattern([da.pat.FreePattern('accountNum')])]), da.pat.TuplePattern([da.pat.FreePattern('lc'), da.pat.FreePattern('id')])])
PatternExpr_6 = da.pat.FreePattern('p')
PatternExpr_7 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('deposit'), da.pat.TuplePattern([da.pat.FreePattern('accountNum'), da.pat.FreePattern('amount')])]), da.pat.TuplePattern([da.pat.FreePattern('lc'), da.pat.FreePattern('id')])])
PatternExpr_8 = da.pat.FreePattern('p')
PatternExpr_9 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.TuplePattern([da.pat.FreePattern('SN'), da.pat.ConstantPattern('deposit')]), da.pat.TuplePattern([da.pat.FreePattern('accountNum'), da.pat.FreePattern('amount')])]), da.pat.TuplePattern([da.pat.FreePattern('lc'), da.pat.FreePattern('id')])])
PatternExpr_10 = da.pat.FreePattern('p')
PatternExpr_11 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('ack'), da.pat.FreePattern('m')]), da.pat.TuplePattern([da.pat.FreePattern('lc'), da.pat.BoundPattern('_BoundPattern53_')])])
PatternExpr_12 = da.pat.FreePattern('p')
PatternExpr_13 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('addServer'), da.pat.FreePattern('p')]), da.pat.TuplePattern([da.pat.FreePattern('lc'), da.pat.FreePattern('id')])])
PatternExpr_14 = da.pat.FreePattern('m')
PatternExpr_15 = da.pat.TuplePattern([da.pat.ConstantPattern('hist')])
PatternExpr_16 = da.pat.FreePattern('p')
PatternExpr_17 = da.pat.TuplePattern([da.pat.ConstantPattern('done')])
PatternExpr_18 = da.pat.FreePattern('p')
PatternExpr_19 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('queryTail')]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_20 = da.pat.FreePattern('client')
PatternExpr_21 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('replyNeighbor'), da.pat.TuplePattern([da.pat.FreePattern('prev'), da.pat.FreePattern('next')])]), da.pat.TuplePattern([da.pat.FreePattern('lc'), da.pat.FreePattern('id')])])
PatternExpr_22 = da.pat.FreePattern('m')
PatternExpr_23 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('replyPid')]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_24 = da.pat.FreePattern('np')
PatternExpr_26 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('replyPid')]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_27 = da.pat.FreePattern('p')
import sys
import random
import time


class Server(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._ServerReceivedEvent_0 = []
        self._ServerReceivedEvent_11 = []
        self._events.extend([
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_0', PatternExpr_0, sources=[PatternExpr_1], destinations=None, timestamps=None, record_history=True, handlers=[]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_1', PatternExpr_3, sources=[PatternExpr_4], destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_0]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_2', PatternExpr_5, sources=[PatternExpr_6], destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_1]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_3', PatternExpr_7, sources=[PatternExpr_8], destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_2]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_4', PatternExpr_9, sources=[PatternExpr_10], destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_3]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_5', PatternExpr_11, sources=[PatternExpr_12], destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_4]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_6', PatternExpr_13, sources=[PatternExpr_14], destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_5]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_7', PatternExpr_15, sources=[PatternExpr_16], destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_6]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_8', PatternExpr_17, sources=[PatternExpr_18], destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_7]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_9', PatternExpr_19, sources=[PatternExpr_20], destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_8]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_10', PatternExpr_21, sources=[PatternExpr_22], destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_9]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_11', PatternExpr_23, sources=[PatternExpr_24], destinations=None, timestamps=None, record_history=True, handlers=[]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_12', PatternExpr_26, sources=[PatternExpr_27], destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_10])])

    def main(self):
        random.seed()
        n = random.randint(0, 1)
        while True:
            m = None

            def ExistentialOpExpr_0():
                nonlocal m
                for (_, (_, _, m), (_ConstantPattern10_,)) in self._ServerReceivedEvent_0:
                    if (_ConstantPattern10_ == 'terminate'):
                        if True:
                            return True
                return False
            _st_label_21 = 0
            while (_st_label_21 == 0):
                _st_label_21+=1
                if ExistentialOpExpr_0():
                    _st_label_21+=1
                else:
                    super()._label('_st_label_21', block=True)
                    _st_label_21-=1
            else:
                if (_st_label_21 != 2):
                    continue
            if (_st_label_21 != 2):
                break

    def setup(self, chainNum, bank, ps):
        self.chainNum = chainNum
        self.bank = bank
        self.ps = ps
        self.sentHist = []
        self.hist = []
        self.next = 0
        self.prev = 0
        self.isHead = False
        self.isTail = False
        self.SN = 0
        self.isWaitForProcessedTransfer = False
        self.lc = self.logical_clock()
        self.seenPid = []

    def queryPid(self, p):
        self.lc = self.logical_clock()
        self._send((('pid',), (self.lc, self.id)), p)
        np = rid = rlc = None

        def ExistentialOpExpr_1():
            nonlocal np, rid, rlc
            for (_, (_, _, np), ((_ConstantPattern103_,), (rlc, rid))) in self._ServerReceivedEvent_11:
                if (_ConstantPattern103_ == 'replyPid'):
                    if True:
                        return True
            return False
        _st_label_78 = 0
        while (_st_label_78 == 0):
            _st_label_78+=1
            if ExistentialOpExpr_1():
                _st_label_78+=1
            else:
                super()._label('_st_label_78', block=True)
                _st_label_78-=1
        return self.seenPid[(-1):]

    def _Server_handler_0(self, id, rlc, m):
        self.lc = self.logical_clock()
        self._send((('reply',), (self.lc, self.id)), m)
    _Server_handler_0._labels = None
    _Server_handler_0._notlabels = None

    def _Server_handler_1(self, p, accountNum, id, lc):
        self._send((('getBalanceRep', (accountNum, 
        self.bank.getBalance(accountNum))), (lc, id)), p)
    _Server_handler_1._labels = None
    _Server_handler_1._notlabels = None

    def _Server_handler_2(self, accountNum, lc, id, p, amount):
        if self.isHead:
            if (not ((((self.SN, 'deposit'), (accountNum, amount)), (lc, id)) in self.hist)):
                self.SN+=1
                self._send((((self.SN, 'deposit'), (accountNum, amount)), (lc, id)), next)
                self.bank.deposit((accountNum, amount))
            else:
                self._send((((self.SN, 'deposit'), (accountNum, amount)), (lc, id)), next)
    _Server_handler_2._labels = None
    _Server_handler_2._notlabels = None

    def _Server_handler_3(self, id, accountNum, p, amount, SN, lc):
        if (SN > self.SN):
            if (not self.isWaitForProcessedTransfer):
                if (not ((((SN, 'deposit'), (accountNum, amount)), (lc, id)) in self.hist)):
                    self.bank.deposit((accountNum, amount))
                    self.sentHist.append((((SN, 'deposit'), (accountNum, amount)), (lc, id)))
                    if self.isTail:
                        self._send((('getBalanceRep', (accountNum, 
                        self.bank.getBalance(accountNum))), (lc, id)), p)
                        self.sentHist.remove((((SN, 'deposit'), (accountNum, amount)), (lc, id)))
                        self.hist.append((((SN, 'deposit'), (accountNum, amount)), (lc, id)))
                        lc = self.logical_clock()
                        self._send((('ack', (((SN, 'deposit'), (accountNum, amount)), (lc, id))), (lc, self.id)), self.prev)
                    else:
                        self._send((((SN, 'deposit'), (accountNum, amount)), (lc, id)), next)
            elif self.isTail:
                self._send((('getBalanceRep', (accountNum, 
                self.bank.getBalance(accountNum))), (lc, id)), p)
            else:
                self._send((('getBalanceRep', (accountNum, 
                self.bank.getBalance(accountNum))), (lc, id)), next)
    _Server_handler_3._labels = None
    _Server_handler_3._notlabels = None

    def _Server_handler_4(self, p, lc, m):
        self.sentHist.remove(m)
        self.hist.append(m)
        self._send((('ack', m), (lc, self.id)), self.prev)
    _Server_handler_4._labels = None
    _Server_handler_4._notlabels = None

    def _Server_handler_5(self, p, id, lc, m):
        self._send(('hist',), p)
    _Server_handler_5._labels = None
    _Server_handler_5._notlabels = None

    def _Server_handler_6(self, p):
        self.isTail = True
        self.isWaitForProcessedTransfer = True
        self._send(('done',), p)
    _Server_handler_6._labels = None
    _Server_handler_6._notlabels = None

    def _Server_handler_7(self, p):
        self.isTail = False
    _Server_handler_7._labels = None
    _Server_handler_7._notlabels = None

    def _Server_handler_8(self, rid, rlc, client):
        self.lc = self.logical_clock()
        self.output('reply querytail\n')
        self._send((('replyTail', self.ps[self.chainNum][(-1):]), (self.lc, self.id)), client)
    _Server_handler_8._labels = None
    _Server_handler_8._notlabels = None

    def _Server_handler_9(self, next, prev, lc, id, m):
        self.next = next
        self.prev = prev
        if (self.next == self.id):
            self.isTail = True
            self.output('im tail\n')
        if (self.prev == self.id):
            self.isHead = True
            self.output('im head\n')
    _Server_handler_9._labels = None
    _Server_handler_9._notlabels = None

    def _Server_handler_10(self, rlc, p, rid):
        if (not (rid in self.seenPid)):
            self.seenPid.append(rid)
    _Server_handler_10._labels = None
    _Server_handler_10._notlabels = None
