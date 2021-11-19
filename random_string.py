import random
import string

characters = string.ascii_letters + string.digits + string.punctuation
key = ''.join(random.choice(characters) for i in range(32))
print("Random String is:", key)

