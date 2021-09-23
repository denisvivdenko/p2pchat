from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import base64

class Signature:


    def __init__(self, signature_bytes: bytes=None, signature_string: str=None):
        # it converts input into bytes
        # I it's required option for signature verification
        if isinstance(signature_string, str):
            self.signature = base64.b64decode(signature_string) 
        else:
            self.signature = signature_bytes

    def verify_signature(self, public_key: RSA.RsaKey, transaction_hash: SHA256.SHA256Hash) -> bool:
        '''
        Verifies with a public key from whom the data came that it was indeed 
        signed by their private key
        param: public_key imported from pem public key importKey() method
        param: transaction hash used during signature generation
        return: Boolean. True if the signature is valid; False otherwise. 
        '''
        signer = PKCS1_v1_5.new(public_key) 
        answer = signer.verify(transaction_hash, self.signature)
        return answer

    def get_byte_format(self) -> bytes:
        return self.signature

    def get_decoded_format(self) -> str:
        return base64.b64encode(self.signature).decode('utf-8')