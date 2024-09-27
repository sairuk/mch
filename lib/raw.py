class RAW(object):
    def __init__(self, dataset):
        self.data = {}
        self.dataset = dataset
        self.ext = "sav"
        self.header = b'\x53\x43'   # save data: SC
        return

    # no header only savedata
    def process(self):
        for key in self.dataset["savedata"].keys():
                self.data[key] = self.dataset["savedata"][key]
