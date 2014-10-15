import da
PatternExpr_0 = da.pat.TuplePattern([da.pat.ConstantPattern('reply'), da.pat.TuplePattern([da.pat.FreePattern('n'), da.pat.FreePattern('k')])])
PatternExpr_1 = da.pat.FreePattern('s')
import sys
import random
import time


class Client(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._ClientReceivedEvent_0 = []
        self._events.extend([
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_0', PatternExpr_0, sources=[PatternExpr_1], destinations=None, timestamps=None, record_history=True, handlers=[])])

    def main(self):
        random.seed()
        n = random.randint(0, 6)
        time.sleep(n)
        self.lc = self.logical_clock()
        self._send(('request', (self.lc, self.id)), self.m)
        k = n = s = None

        def ExistentialOpExpr_0():
            nonlocal k, n, s
            for (_, (_, _, s), (_ConstantPattern13_, (n, k))) in self._ClientReceivedEvent_0:
                if (_ConstantPattern13_ == 'reply'):
                    if True:
                        return True
            return False
        _st_label_14 = 0
        while (_st_label_14 == 0):
            _st_label_14+=1
            if ExistentialOpExpr_0():
                if (k == self.id):
                    self.output('client done\n')
                _st_label_14+=1
            else:
                super()._label('_st_label_14', block=True)
                _st_label_14-=1

    def setup(self, m):
        self.m = m
        self.lc = self.logical_clock()
