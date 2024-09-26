
"""
mc data only
"""

class MCD(object):
    def __init__(self, dataset):
        self.data = {}
        self.dataset = dataset
        self.ext = "mcd"
        return

    def process(self):
        for key in self.dataset["mcdata"]:
            self.data[key] = self.dataset["mcdata"][key]
