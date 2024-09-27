
"""
128b header
save data
"""


class MCS(object):
    def __init__(self, dataset):
        self.data = {}
        self.dataset = dataset
        self.ext = "mcs"
        self.header = b'\x51\x00'   # save header: Q
        return

    def process(self):
        for key in self.dataset["headers"]:
            if key in self.dataset["savedata"]:
                self.data[key] = b''.join([self.dataset["headers"][key],self.dataset["savedata"][key]])
