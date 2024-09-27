class GME(object):
    def __init__(self):
        self.ext = "gme"
        self.savedict = {
            "headers": {},
            "savedata": {},
            "mcdata": {}
        }

        self.bytes_header = b'\x31\x32\x33\x2d\x34\x35\x36\x2d\x53\x54\x44\x00' # GME header: 123-456-STD
        self.bytes_game = b'\x51\x00'   # save header
        self.bytes_save = b'\x53\x43'   # SC
        self.bytes_memc = b'\x4d\x43'   # MC
        self.MAXSIZE = 8192
        self.CHUNK_SIZE = 2

    def read(self, inputfile):
        self.filename = inputfile
        self.gme = open(inputfile,'rb')

    def header(self):
        self.gme.seek(0)
        if self.gme.read(12) != self.bytes_header:
            print(f"{self.filename} is not a valid DexDrive save")
            return False
        else:
            return True

    def saveheaders(self):
        cntr = 0
        self.gme.seek(0)
        chunk = self.gme.read(self.CHUNK_SIZE)
        while chunk:
            if chunk == self.bytes_game:
                self.savedict["headers"][cntr] = b''.join([chunk, self.gme.read(126)])
                cntr = cntr + 1
            chunk = self.gme.read(self.CHUNK_SIZE)

        total_saves = len(self.savedict["headers"])
        print(f"Found {total_saves} saves")
        return

    def mcdata(self):
        cntr = 0
        readin = False
        bytestream = []
        self.gme.seek(0)
        chunk = self.gme.read(self.CHUNK_SIZE)
        while chunk:

            if chunk == self.bytes_memc: # MC
                readin = True

            if readin:
                bytestream.append(chunk)

            chunk = self.gme.read(self.CHUNK_SIZE)

        if len(bytestream) > 0:
            self.savedict["mcdata"][cntr] = b''.join(bytestream)

        return

    def savedata(self):
        cntr = 0
        readin = False
        bytestream = []
        self.gme.seek(0)
        chunk = self.gme.read(self.CHUNK_SIZE)
        while chunk:

            if chunk == self.bytes_save:
                if len(bytestream) > 0:
                    self.savedict["savedata"][cntr - 1] = b''.join(bytestream)
                cntr = cntr + 1
                bytestream = []
                readin = True

            if chunk == self.bytes_memc: # MC
                if len(bytestream) > 0:
                    self.savedict["savedata"][cntr - 1] = b''.join(bytestream)
                bytestream = []
                readin = False

            if readin:
                bytestream.append(chunk)

            chunk = self.gme.read(self.CHUNK_SIZE)
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