import lib.ps1card as ps1

class GME(object):
    def __init__(self):
        self.ext = "gme"
        self.savedict = ps1.PS1()._empty()
        self.bytes_header = b'\x31\x32\x33\x2d\x34\x35\x36\x2d\x53\x54\x44\x00' # GME header: 123-456-STD

        ## consumed slots
        # 00000012:    01   ?
        # 00000013:    00   ?
        # 00000014:    01   ?
        # 00000015:    4d   M                                           21           static
        # 00000016-26: 51   Q      Consumed slots                       22           static
        # 00000f40-41: 4d43 MC     Start of MC data                     3904         static
        # 00000fc0:    51   Q      First save header 128b               4032         static
        # 00002ec0-ff: ..   .      Unknown                              11968        variable
        # 00002f00-3f: ..   .      Unknown                              12032        variable
        # 00002f40:    5343 SC     Start of SC data, variable length    12096        static (variable data length)

        ## save header
        # 51                Q      normal save
        # a0                .      no save data
        # a1                .      linked?

    def read(self, inputfile):
        self.filename = inputfile
        self.gme = open(inputfile,'rb')

    def consumption(self):
        self.gme.seek(0)
        self.gme.seek(22)

    def header(self):
        self.gme.seek(0)
        if self.gme.read(12) != self.bytes_header:
            print(f"{self.filename} is not a valid DexDrive save")
            return False
        else:
            return True

    def saveheaders(self, dstart=4032, dend=5823):
        cntr = 0
        self.gme.seek(0)
        self.gme.seek(dstart)
        chunk = True
        while chunk:
            if self.gme.tell() >= dend:
                break
            chunk = self.gme.read(ps1.PS1().CHUNK_SAVE_HEADER)
            if chunk[:2] == ps1.PS1().bytes_game:
                self.savedict["headers"][cntr] = chunk
                cntr = cntr + 1

        total_saves = len(self.savedict["headers"])
        print(f"Found {total_saves} saves")
        return

    def mcdata(self, dstart=3904, dend=None):
        self.gme.seek(0)
        self.gme.seek(dstart)
        self.savedict["mcdata"][0] = self.gme.read(ps1.PS1().CHUNK_MEMCARD)
        return

    def savedata(self, dstart=12096, dend=None):
        cntr = 0
        self.gme.seek(0)
        self.gme.seek(dstart)
        chunk = True
        while chunk:
            chunk = self.gme.read(ps1.PS1().CHUNK_SAVE)
            if chunk[:2] == ps1.PS1().bytes_save:
                self.savedict["savedata"][cntr] = chunk
                cntr = cntr + 1
        return

    def close(self):
        self.gme.close()

    def process(self, inputfile):
        self.read(inputfile)
        if self.header():
            self.saveheaders()
            self.savedata()
            self.mcdata()
        else:
            exit(1)
        self.close()