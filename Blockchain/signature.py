import base64

class Signature:


    def __init__(self, signature_bytes: bytes=None, signature_string: str=None):
        # it converts input into bytes
        # I it's required option for signature verification
        if isinstance(signature_string, str):
            self.signature = base64.b64decode(signature_string) 
        else:
            self.signature = signature_bytes

    def get_byte_format(self):
        return self.signature

    def get_decoded_format(self):
        return base64.b64encode(self.signature).decode('utf-8')