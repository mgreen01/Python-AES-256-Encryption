#PyCryptodome library import
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

plaintext_input=input("Please enter your plaintext:")
plaintext = b'this is a message'
#32 byte * 8 = 256-bit Encryption Key this key is generate by the get_random_bytes from PyCryptdome
key = get_random_bytes(32)
#Encryption Cipher and Encryption Mode = Encrypt then authenticate then translate (EAX mode)
cipher = AES.new(key,AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(plaintext)n
with open("key.bin","wb")as c_file:
	c_file.write(key)




#
file_out = open ("encryptedfile.bin", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
file_out.close()
