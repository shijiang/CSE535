import da
PatternExpr_0 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('reply'), da.pat.FreePattern('lc')]), da.pat.FreePattern('id')])
PatternExpr_1 = da.pat.FreePattern('proc')
PatternExpr_3 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('reply'), da.pat.FreePattern('lc')]), da.pat.FreePattern('id')])
PatternExpr_4 = da.pat.FreePattern('p')
PatternExpr_5 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('newServer'), da.pat.FreePattern('chainNum')]), da.pat.FreePattern('id')])
PatternExpr_6 = da.pat.FreePattern('p')
PatternExpr_7 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('done'), da.pat.FreePattern('chainNum')]), da.pat.FreePattern('id')])
PatternExpr_8 = da.pat.FreePattern('p')
PatternExpr_9 = da.pat.TuplePattern([da.pat.TuplePattern([da.pat.ConstantPattern('head'), da.pat.FreePattern('chainNum')]), da.pat.FreePattern('id')])
PatternExpr_10 = da.pat.FreePattern('p')
import sys
import random
import time


class Master(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._MasterReceivedEvent_0 = []
        self._events.extend([
        da.pat.EventPattern(da.pat.ReceivedEvent, '_MasterReceivedEvent_0', PatternExpr_0, sources=[PatternExpr_1], destinations=None, timestamps=None, record_history=True, handlers=[]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_MasterReceivedEvent_1', PatternExpr_3, sources=[PatternExpr_4], destinations=None, timestamps=None, record_history=None, handlers=[self._Master_handler_0]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_MasterReceivedEvent_2', PatternExpr_5, sources=[PatternExpr_6], destinations=None, timestamps=None, record_history=None, handlers=[self._Master_handler_1]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_MasterReceivedEvent_3', PatternExpr_7, sources=[PatternExpr_8], destinations=None, timestamps=None, record_history=None, handlers=[self._Master_handler_2]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_MasterReceivedEvent_4', PatternExpr_9, sources=[PatternExpr_10], destinations=None, timestamps=None, record_history=None, handlers=[self._Master_handler_3])])

    def main(self):
        while True:
            time.sleep(self.timer)
            self.lc = self.logical_clock()
            for chain in self.ps.keys():
                for procList in self.ps[chain]:
                    for p in procList:
                        self._send(('ping', self.lc), p[0])
                        proc = id = lc = None

                        def ExistentialOpExpr_0():
                            nonlocal proc, id, lc
                            for (_, (_, _, proc), ((_ConstantPattern14_, lc), id)) in self._MasterReceivedEvent_0:
                                if (_ConstantPattern14_ == 'reply'):
                                    if ((p[0] == proc) and (lc > self.lc)):
                                        return True
                            return False
                        _st_label_19 = 0
                        self._timer_start()
                        while (_st_label_19 == 0):
                            _st_label_19+=1
                            if ExistentialOpExpr_0():
                                pass
                                _st_label_19+=1
                            elif self._timer_expired:
                                upresp[p[1]]+=1
                                _st_label_19+=1
                            else:
                                super()._label('_st_label_19', block=True, timeout=self.timer)
                                _st_label_19-=1
                        else:
                            if (_st_label_19 != 2):
                                continue
                        if (_st_label_19 != 2):
                            break
                        if (upresp[p[1]] > 3):
                            procList.remove(p)
                        self.resp[p[1]] = False

    def setup(self, ps):
        self.ps = ps
        self.resp = {}
        self.unresp = {}
        self.timer = 1
        self.lc = self.logical_clock()

    def tail(self, num):
        return self.ps[num][(-1):]

    def _Master_handler_0(self, p, lc, id):
        if (lc > self.lc):
            self.resp[id] = True
            upresp[id] = 0
    _Master_handler_0._labels = None
    _Master_handler_0._notlabels = None

    def _Master_handler_1(self, id, chainNum, p):
        self._send((('addServer', p), id), 
        self.tail(chainNum))
    _Master_handler_1._labels = None
    _Master_handler_1._notlabels = None

    def _Master_handler_2(self, id, chainNum, p):
        self.ps[chainNum].append((p, id))
        self.resp[id] = True
        self.unresp[id] = 0
    _Master_handler_2._labels = None
    _Master_handler_2._notlabels = None

    def _Master_handler_3(self, id, chainNum, p):
        self._send(('replyHead', (self.ps[chainNum][:1], 
        self.tail(chainNum))), p)
    _Master_handler_3._labels = None
    _Master_handler_3._notlabels = None
