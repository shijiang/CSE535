import da
PatternExpr_0 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('reply')]), da.pat.TuplePattern([da.pat.FreePattern('lc'), da.pat.FreePattern('id')])])
PatternExpr_1 = da.pat.FreePattern('repServ')
PatternExpr_3 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('reply')]), da.pat.TuplePattern([da.pat.FreePattern('lc'), da.pat.FreePattern('id')])])
PatternExpr_4 = da.pat.FreePattern('p')
PatternExpr_5 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('newServer'), da.pat.FreePattern('n')]), da.pat.TuplePattern([da.pat.FreePattern('lc'), da.pat.FreePattern('id')])])
PatternExpr_6 = da.pat.FreePattern('p')
PatternExpr_7 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('done'), da.pat.FreePattern('n')]), da.pat.TuplePattern([da.pat.FreePattern('lc'), da.pat.FreePattern('id')])])
PatternExpr_8 = da.pat.FreePattern('p')
PatternExpr_9 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('head'), da.pat.FreePattern('n')]), da.pat.TuplePattern([da.pat.FreePattern('lc'), da.pat.FreePattern('id')])])
PatternExpr_10 = da.pat.FreePattern('p')
PatternExpr_11 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('neighbor'), da.pat.FreePattern('cn')]), da.pat.TuplePattern([da.pat.FreePattern('tlc'), da.pat.FreePattern('tid')])])
PatternExpr_12 = da.pat.FreePattern('p')
PatternExpr_13 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('replyPid')]), da.pat.TuplePattern([da.pat.FreePattern('rlc'), da.pat.FreePattern('rid')])])
PatternExpr_14 = da.pat.FreePattern('np')
import sys
import random
import time


class Master(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._MasterReceivedEvent_0 = []
        self._MasterReceivedEvent_6 = []
        self._events.extend([
        da.pat.EventPattern(da.pat.ReceivedEvent, '_MasterReceivedEvent_0', PatternExpr_0, sources=[PatternExpr_1], destinations=None, timestamps=None, record_history=True, handlers=[]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_MasterReceivedEvent_1', PatternExpr_3, sources=[PatternExpr_4], destinations=None, timestamps=None, record_history=None, handlers=[self._Master_handler_0]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_MasterReceivedEvent_2', PatternExpr_5, sources=[PatternExpr_6], destinations=None, timestamps=None, record_history=None, handlers=[self._Master_handler_1]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_MasterReceivedEvent_3', PatternExpr_7, sources=[PatternExpr_8], destinations=None, timestamps=None, record_history=None, handlers=[self._Master_handler_2]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_MasterReceivedEvent_4', PatternExpr_9, sources=[PatternExpr_10], destinations=None, timestamps=None, record_history=None, handlers=[self._Master_handler_3]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_MasterReceivedEvent_5', PatternExpr_11, sources=[PatternExpr_12], destinations=None, timestamps=None, record_history=None, handlers=[self._Master_handler_4]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_MasterReceivedEvent_6', PatternExpr_13, sources=[PatternExpr_14], destinations=None, timestamps=None, record_history=True, handlers=[])])

    def main(self):
        self.output('master starts\n')
        for k in self.ps.keys():
            for p in self.ps[k]:
                self.resp[p] = True
                self.unresp[p] = 0
        for k in self.ps.keys():
            h = self.head(k)
            t = self.tail(k)
            self.ht[k] = (h, t)
        while True:
            time.sleep(self.timer)
            for k in self.ps.keys():
                for p in self.ps[k]:
                    self.lc = self.logical_clock()
                    self._send((('ping',), (self.lc, self.id)), p)
                    id = lc = repServ = None

                    def ExistentialOpExpr_0():
                        nonlocal id, lc, repServ
                        for (_, (_, _, repServ), ((_ConstantPattern15_,), (lc, id))) in self._MasterReceivedEvent_0:
                            if (_ConstantPattern15_ == 'reply'):
                                if ((p == repServ) and (lc > self.lc)):
                                    return True
                        return False
                    _st_label_29 = 0
                    self._timer_start()
                    while (_st_label_29 == 0):
                        _st_label_29+=1
                        if ExistentialOpExpr_0():
                            pass
                            _st_label_29+=1
                        elif self._timer_expired:
                            self.unresp[p]+=1
                            _st_label_29+=1
                        else:
                            super()._label('_st_label_29', block=True, timeout=self.timer)
                            _st_label_29-=1
                    else:
                        if (_st_label_29 != 2):
                            continue
                    if (_st_label_29 != 2):
                        break
                    if (self.unresp[p] > 3):
                        self.ps[self.chainNum].remove(p)
                    self.resp[p] = False

    def setup(self, chainNum, ps):
        self.chainNum = chainNum
        self.ps = ps
        self.resp = {}
        self.unresp = {}
        self.timer = 4
        self.lc = self.logical_clock()
        self.ht = {}
        self.seenPid = []

    def tail(self, num):
        n = len(self.ps[num])
        return self.ps[num][(n - 1)]

    def head(self, num):
        return self.ps[num][0]

    def queryPid(self, p):
        self.lc = self.logical_clock()
        self._send((('pid',), (self.lc, self.id)), p)
        np = rid = rlc = None

        def ExistentialOpExpr_1():
            nonlocal np, rid, rlc
            for (_, (_, _, np), ((_ConstantPattern73_,), (rlc, rid))) in self._MasterReceivedEvent_6:
                if (_ConstantPattern73_ == 'replyPid'):
                    if (rlc > self.lc):
                        return True
            return False
        _st_label_72 = 0
        self._timer_start()
        while (_st_label_72 == 0):
            _st_label_72+=1
            if ExistentialOpExpr_1():
                return rid
                _st_label_72+=1
            elif self._timer_expired:
                self.output('pid fail\n')
                _st_label_72+=1
            else:
                super()._label('_st_label_72', block=True, timeout=3)
                _st_label_72-=1

    def _Master_handler_0(self, id, lc, p):
        if (lc > self.lc):
            self.resp[p] = True
            self.unresp[p] = 0
    _Master_handler_0._labels = None
    _Master_handler_0._notlabels = None

    def _Master_handler_1(self, n, id, lc, p):
        if (self.ps[n].count(p) == 0):
            self.ps[n].append(p)
            self._send((('addServer', p), (lc, id)), 
            self.tail(n))
            self.output(('new server %s in the ps\n' % id))
        else:
            pass
    _Master_handler_1._labels = None
    _Master_handler_1._notlabels = None

    def _Master_handler_2(self, lc, n, p, id):
        self.ps[n].append(p)
        (h, t) = self.ht[n]
        self.ht[n] = (h, id)
        self.resp[id] = True
        self.unresp[id] = 0
    _Master_handler_2._labels = None
    _Master_handler_2._notlabels = None

    def _Master_handler_3(self, n, id, lc, p):
        self._send((('replyHead', self.ht[n]), (lc, self.id)), p)
    _Master_handler_3._labels = None
    _Master_handler_3._notlabels = None

    def _Master_handler_4(self, p, cn, tid, tlc):
        n = self.ps[cn].index(p)
        if ((n + 1) < 
        len(self.ps[cn])):
            next = self.ps[cn][(n + 1)]
        else:
            next = tid
        if ((n - 1) >= 0):
            prev = self.ps[cn][(n - 1)]
        else:
            prev = tid
        self.lc = self.logical_clock()
        self._send((('replyNeighbor', (prev, next)), (self.lc, self.id)), p)
        self.output('reply to Neighbor')
    _Master_handler_4._labels = None
    _Master_handler_4._notlabels = None
