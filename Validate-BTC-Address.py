import hashlib
import base58
import binascii

def convertByteToHex(inp):
    return ''.join(["%02x" % x for x in inp])

bitcoinAddress = "1nBJUwDQm6sBd8ye8YxMd7DhS8EXKE2cp"
base58Decoder = base58.b58decode(bitcoinAddress).hex()
prefixAndHash = base58Decoder[:len(base58Decoder)-8]
checksum = base58Decoder[len(base58Decoder)-8:]
hash = prefixAndHash
for x in range(1,3):
    hash = hashlib.sha256(binascii.unhexlify(hash)).hexdigest()
if(checksum == hash[:8]):
    print("Checksum is valid!")
else:
    print("Checksum is NOT valid!")
