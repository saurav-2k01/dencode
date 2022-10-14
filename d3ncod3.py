

class De_ncode():
    import base64
    def __init__(self, string, layer):
        self.string = string
        self.layer = layer

    def encode_str(self):
        string = self.string
        if self.layer > 20 :
            return "Layer cannot exceed 20.\n please try again."
        else:
            encode_str = string
            for i in range(self.layer):
                encode_str = De_ncode.base64.b64encode(encode_str.encode("ascii")).decode("ascii")
            return encode_str

    def decode_str(self):
        string = self.string
        decode_str = string
        if self.layer > 20:
            return "Layer cannot exceed 20.\n please try again."
        else:
            try:
                for i in range(self.layer):
                    decode_str = De_ncode.base64.b64decode(decode_str.encode("ascii")).decode("ascii")
                return decode_str
            except:
                return "Invalid Format.\nPlease Enter Encrypted string."
                pass




