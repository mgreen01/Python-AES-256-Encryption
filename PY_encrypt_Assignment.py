#PyCryptodome library import
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

plaintext
plaintext = b'this is a message'
#32 byte * 8 = 256-bit Encryption Key
key = get_random_bytes(32)
#Encryption Cipher and Encryption Mode = Encrypt then authenticate then translate (EAX_mode
cipher = AES.new(key,AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(plaintext)
#Converts plaintext to bytes for encryption

#The pad variable pads the plaintext into multiples of 128-bits

#Saves the ciphertext and the padding to make sure that the cipher text fits wihtin the 128-bit limit

with open("key.bin","wb")as c_file:
	c_file.write(key)





file_out = open ("encryptedfile.bin", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
file_out.close()
