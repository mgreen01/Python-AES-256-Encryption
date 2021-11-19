from Cryptodome.Cipher import AES
file_in = open("encryptedfile.bin", "rb")
nonce, tag, ciphertext = [ file_in.read(x) for x in (32, 32, -1)]


cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
print(data.decode('UTF-8'))
