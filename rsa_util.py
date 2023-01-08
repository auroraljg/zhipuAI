#  pip3 uninstall pycrypto
#  pip3 install pycryptodome

import base64

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA


def rsa_encode(text, public_key):
    key = RSA.importKey(base64.b64decode(public_key))
    cipher = PKCS1_v1_5.new(key)
    return base64.b64encode(cipher.encrypt(text)).decode('utf-8')
