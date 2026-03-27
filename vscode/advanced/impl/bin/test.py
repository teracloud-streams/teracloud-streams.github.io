import streams

class Operator(streams.Operator):
    def __init__(self, ctx, params):
        super().__init__(ctx)


    def __del__(self):
        pass

    def allPortsReady(self):
        pass

    def processTuple(self, stream_tuple, port):
        if (stream_tuple["reading"] > 0.8):
            self.submitTuple(stream_tuple, port)

    def processPunctuation(self, punctuation, port):
        self.submitPunctuation(punctuation, port)