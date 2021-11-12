#PyCryptodome library import
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

#16 byte * 8 = 128-bit Encryption Key
key = b'mysecretpassword'
#Encryption Cipher and Encryption Mode = Cipher Block Chaining
cipher = AES.new(key,AES.MODE_CBC)
#Converts plaintext to bytes for encryption
plaintext = b'this is a message'
#The pad variable pads the plaintext into multiples of 128-bits
ciphertext = cipher.encrypt(pad(plaintext,AES.block_size))
#Saves the ciphertext and the padding to make sure that the cipher text fits wihtin the 128-bit limit
with open('cipher_file', 'wb') as c_file:
	c_file.write(cipher.iv)
	c_file.write(ciphertext)
