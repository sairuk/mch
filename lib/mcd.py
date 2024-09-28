
"""
mc data only
"""

import lib.ps1card as ps1

class MCD(object):
    def __init__(self, dataset):
        self.data = {}
        self.dataset = dataset
        self.ext = "mcd"
        self.header = ps1.PS1().bytes_memc # b'\x4d\x43' memorycard data: MC
        return

    def process(self):
        for key in self.dataset["mcdata"]:
            self.data[key] = self.dataset["mcdata"][key]
