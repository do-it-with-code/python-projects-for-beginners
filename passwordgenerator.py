import string
import random

letters =  string.ascii_letters
#print( letters )

digits = string.digits
#print( digits )

punctuation = string.punctuation
#print( punctuation )

characters = letters + digits + punctuation
#print( characters )

password = random.choices( characters, k=16 )
#print( password )

password = "".join( password )
print( password )
