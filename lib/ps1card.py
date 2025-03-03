class PS1(object):
    def __init__(self):
        self.CHUNK_SAVE = 8192
        self.BYTES_SAVE = b'\x53\x43'   # save data: SC

        self.CHUNK_SAVE_HEADER = 128
        self.BYTES_SAVE_HEADER = b'\x51\x00'   # save header: Q

        self.CHUNK_MEMCARD = 131072
        self.BYTES_MEMCARD = b'\x4d\x43'   # memorycard data: MC
        return

    def _empty(self):
        return {
            "headers": {},
            "savedata": {},
            "mcdata": {}
        }