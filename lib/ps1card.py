class PS1(object):
    def __init__(self):
        self.CHUNK_SAVE = 8192
        self.CHUNK_SAVE_HEADER = 128
        self.CHUNK_MEMCARD = 131072
        self.bytes_game = b'\x51\x00'   # save header: Q
        self.bytes_memc = b'\x4d\x43'   # memorycard data: MC
        self.bytes_save = b'\x53\x43'   # save data: SC
        return

    def _empty(self):
        return {
            "headers": {},
            "savedata": {},
            "mcdata": {}
        }