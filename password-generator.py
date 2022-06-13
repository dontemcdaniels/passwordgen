import random
import string

# creates the variable to store password
total = string.ascii_letters + string.digits + string.punctuation
# makes the length of password 16 characters
length = 16
# password is created
password = "".join(random.sample(total, length))

print(password)
