import random
import string
from hashlib import blake2b

key0 = blake2b(digest_size=16)
characters = string.ascii_letters + string.digits + string.punctuation
key1 = ''.join(random.choice(characters) for i in range(32))
print ("The pseudorandom value is:", key1)
key_byte = bytes(key1, 'utf-8')
print("the byte convert is: ", str(key_byte))
key0.update(key_byte)
print("The hash is :",key0.hexdigest())
hexstr = (str(key0.hexdigest()))
hexstr_byte = bytes(hexstr, 'utf-8')
print(hexstr_byte)
