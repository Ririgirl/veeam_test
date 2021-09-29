import socket
import threading
import logging

logging.basicConfig(filename="task3.log", level=logging.DEBUG)

server1 = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server2 = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server1.bind(
    ('127.0.0.1', 8000)
)
server1.listen(50)
print('Port 8000 is opened')

server2.bind(
    ('127.0.0.1', 8001)
)
server2.listen(50)
print('Port 8001 is opened')

users = []
usersnames ={}

#server authorization, connect to 8001
def autorization(user):
    user.send(f'Введите ваш ник и ваш код, который был автоматически сгенерирован'.encode('utf-8'))
    user_socket2, address2 = server2.accept()
    print(f'User connected to 8001, {address2[1]}')

    username = user.recv(2048)
    uniqcode = user.recv(2048)

    if uniqcode.decode('utf-8') == str(usersnames.get(username)):
        user.send(
            f'Вы успешно авторизовались и подключились к порту 8001. Можете ввести ваше сообщение.'.encode('utf-8'))
        text = user.recv(2048)
        user.send(f'Ваще сообщение {text} записано в логи.'.encode('utf-8'))
        logging.info(f'User {username} send {text}')
    else:
        user.send('Ваш авторизация завершилась неудачей.'.encode('utf-8'))


#choosing a unique name and getting a password
def uniq_name(user, address):
    print('unique name')
    uniq_name = user.recv(2048)
    print(f'user: {uniq_name}')

    if uniq_name not in usersnames.keys():

        usersnames[uniq_name] = address[1]
        user.send(f'Ваш ник {uniq_name}, ваш код {address[1]}'.encode('utf-8'))

        listen_accepted_user = threading.Thread(
            target=autorization, args=(user,))
        listen_accepted_user.start()
    else:
        print('Это имя занято')
        user.send('Это имя занято'.encode('utf-8'))


#server connection, port 8000
def start_server():
    while True:
        user_socket1, address1 = server1.accept()

        users.append(user_socket1)

        for i in users:
            print(i)

        listen_accepted_user = threading.Thread(
            target=uniq_name, args=(user_socket1, address1))

        listen_accepted_user.start()


if __name__ == '__main__':
    start_server()
