#AES PyCryptodome Library Import
from Crypto.Cipher import AES
#Opens the cryptotext binary and arranges in a format suitable for the program to decrypt the text.
file_in = open("encryptedfile.bin", "rb")
nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1)]
#Opens the encryption key from the encryption key binary and inserts that key into 
with open("key.bin", "rb") as c_file:
	key = c_file.read()
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
#decodes the decrypted into UTF-8 encoded text
print(data.decode('UTF-8'))

#Sources for Both Encryption and Decryption Program: Chapter 6 Files and Exceptions from Starting Out with Python (4th edn) by Tony Gaddis, PyCryptodome Documentation

