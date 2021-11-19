from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

#define our data
data=b"Private Crap"

key = get_random_bytes(32)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

file_out = open("encryptedfile.bin", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
file_out.close()

#################################################################

file_in = open("encryptedfile.bin", "rb")
nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

#the person decrypting the message will need access to the key
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
print(data.decode('UTF-8')) 

#output:
#SECRETDATA
