#PyCryptodome library import
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
#The user inputs the plaintext
plaintext_input=input("Please enter your plaintext:")
#The string input gets converted to bytes 
plaintext = bytes(plaintext_input, 'utf-8')
#32 byte * 8 = 256-bit Encryption Key this key is generate by the get_random_bytes from PyCryptdome
key = get_random_bytes(32)
#Encryption Cipher and Encryption Mode = Encrypt then authenticate then translate (EAX mode)
cipher = AES.new(key,AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(plaintext)
#The pseudorandomly generated key is saved on to the key binary file.
with open("key.bin","wb")as c_file:
	c_file.write(key)
#The cipher text, cipher nonce and the tag is saved on to the encryptedfile binary to be decrypted by the decryption program
file_out = open ("encryptedfile.bin", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
file_out.close()

#Sources for Both Encryption and Decryption Program: Chapter 6 Files and Exceptions from Starting Out with Python (4th edn) by Tony Gaddis, PyCryptDome Documentation
