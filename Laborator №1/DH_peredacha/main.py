import DH
from  random import randint
g = 3
A_private =randint(0,100000)
p = 17
B_private = randint(0,100000)
Alica = DH.DH(g, p, A_private)
Bob = DH.DH(g, p, B_private)
A_partial = Alica.generate_partial_key()
B_partial = Bob.generate_partial_key()
A_secret_key = Alica.generate_full_key(B_partial)
print(A_secret_key)
B_secret_key=Bob.generate_full_key(A_partial)
print(B_secret_key)