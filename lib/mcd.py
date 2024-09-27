
"""
mc data only
"""

class MCD(object):
    def __init__(self, dataset):
        self.data = {}
        self.dataset = dataset
        self.ext = "mcd"
        self.header = b'\x4d\x43'   # memorycard data: MC
        return

    def process(self):
        for key in self.dataset["mcdata"]:
            self.data[key] = self.dataset["mcdata"][key]
