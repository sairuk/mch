
"""
128b header
save data
"""
import lib.ps1card as ps1

class MCS(object):
    def __init__(self, dataset):
        self.data = {}
        self.dataset = dataset
        self.ext = "mcs"
        self.header = ps1.PS1().bytes_game
        return

    def process(self):
        for key in self.dataset["headers"]:
            if key in self.dataset["savedata"]:
                self.data[key] = b''.join([self.dataset["headers"][key],self.dataset["savedata"][key]])
