import  socket
import  threading
import DH_code
import json
from  random import randint
from itertools import starmap, cycle

def decrypt(message, key):
    '''Vigenere decryption of message using key.'''

    def dec(c, k):
        '''Single letter decryption.'''

        return chr(((ord(c) - ord(k) - 2 * ord('A')) % 26) + ord('A'))

    return ''.join(starmap(dec, zip(message, cycle(key))))

   # gg=data_g["g"][0]
    #print("gg="+gg)

def start_server():
    while True:
        user_socket, addres = servet.accept()
        user_socket.send("Вы подключены!".encode())
        print(f"Пользователь {addres[0]} Подключился")
        users.append(user_socket)
        print("11111")
        data_g = user_socket.recv(1024)
        #print("CRASH")
        data_g = json.loads(data_g.decode())
        g = data_g.get("g")
        p = data_g.get("p")
        print("g = " , g , "p =" , p)

        Alica = user_socket.recv(1024)
        Alica = json.loads(Alica.decode())
        Alica_a = Alica.get("Alica")
        print("Alisa public",Alica_a)

        B_secret = randint(0, 100000)
        B_public = (g ** B_secret) % p
        data_B = json.dumps({"Bob": B_public})
        user_socket.send(data_B.encode("utf-8"))

        B_key = (Alica_a ** B_secret) % p
        print("key = ",B_key)




        user_listen_appect=threading.Thread(target=user_listen,args=(user_socket,B_key))
        #user_listen(user_socket)
        user_listen_appect.start()

def all_send_message(data):
    for user in users:
        user.send(data.encode("utf-8"))

def user_listen(user,B_key):

    while True:
        data = user.recv(1024)
        print(data)
        d=decrypt(str(data),str(B_key))

        print(f"User {d}")

        dd=d[2:int(len(d))-1]
        print(dd)
        all_send_message(dd)


servet = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)
servet.bind(
    ("127.0.0.1",700)  # localhost
)

servet.listen(5)
print("Сервер Старт!")

users=[]

if __name__ =='__main__':

    start_server()