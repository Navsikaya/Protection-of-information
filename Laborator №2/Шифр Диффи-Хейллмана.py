from random import randint
def DH():
    g=3
    p=17
    A_secret=randint(0,100000)
    B_secret=randint(0,100000)
    A_public=(g**A_secret)%p
    B_public=(g**B_secret)%p
    A_key=(B_public**A_secret)%p
    B_key=(A_public**B_secret)%p
    print(f"Key 1={A_key}  Key 2={B_key}")
if __name__ == '__main__':
    DH()