import da
PatternExpr_0 = da.pat.TuplePattern([da.pat.ConstantPattern('request'), da.pat.FreePattern(None)])
PatternExpr_1 = da.pat.FreePattern('p')
PatternExpr_3 = da.pat.TuplePattern([da.pat.ConstantPattern('request'), da.pat.FreePattern('id')])
PatternExpr_4 = da.pat.FreePattern('p')
import sys
import random


class Master(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._MasterReceivedEvent_0 = []
        self._events.extend([
        da.pat.EventPattern(da.pat.ReceivedEvent, '_MasterReceivedEvent_0', PatternExpr_0, sources=[PatternExpr_1], destinations=None, timestamps=None, record_history=True, handlers=[]), 
        da.pat.EventPattern(da.pat.ReceivedEvent, '_MasterReceivedEvent_1', PatternExpr_3, sources=[PatternExpr_4], destinations=None, timestamps=None, record_history=None, handlers=[self._Master_handler_0])])

    def main(self):
        _st_label_8 = 0
        while (_st_label_8 == 0):
            _st_label_8+=1
            if (len([p for (_, (_, _, p), (_ConstantPattern11_, _)) in self._MasterReceivedEvent_0 if (_ConstantPattern11_ == 'request')]) == self.n):
                self.output('every client has a server:\n')
                if (not (len(self.resp) == 0)):
                    for (k, v) in self.resp.items():
                        message = ('process:  value: %i' % v)
                        self.output(message)
                _st_label_8+=1
            else:
                super()._label('_st_label_8', block=True)
                _st_label_8-=1

    def setup(self, n):
        self.n = n
        self.resp = {}

    def _Master_handler_0(self, id, p):
        random.seed()
        c = random.randint(0, 50)
        self._send(('reply', c), p)
        self.output(('receive from %s\n' % id))
        self.resp[
        p.getId()] = c
    _Master_handler_0._labels = None
    _Master_handler_0._notlabels = None
