from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

with open('key_file', 'rb') as c_file:
    key = c_file.read()

with open('cipher_file', 'rb') as c_file:
	iv = c_file.read(32)
	ciphertext = c_file.read()

cipher = AES.new(key, AES.MODE_CBC, iv)

plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

print(plaintext)
