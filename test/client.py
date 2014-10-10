import da
PatternExpr_0 = da.pat.TuplePattern([da.pat.ConstantPattern('reply'), da.pat.FreePattern(None)])
import sys
import random
import time


class Client(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._ClientReceivedEvent_0 = []
        self._events.extend([
        da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_0', PatternExpr_0, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[])])

    def main(self):
        random.seed()
        n = random.randint(0, 6)
        time.sleep(n)
        self._send(('request', self.id), self.m)

        def ExistentialOpExpr_0():
            for (_, _, (_ConstantPattern10_, _)) in self._ClientReceivedEvent_0:
                if (_ConstantPattern10_ == 'reply'):
                    if True:
                        return True
            return False
        _st_label_13 = 0
        while (_st_label_13 == 0):
            _st_label_13+=1
            if ExistentialOpExpr_0():
                self.output(('client %s done\n' % self.id))
                _st_label_13+=1
            else:
                super()._label('_st_label_13', block=True)
                _st_label_13-=1

    def setup(self, m):
        self.m = m
        pass

    def getId(self):
        return self.id
