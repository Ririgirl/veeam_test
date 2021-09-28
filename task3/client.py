import socket
from threading import Thread

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)

client2 = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)

client.connect(
    ('127.0.0.1', 8000)
)

client2.connect(
    ('127.0.0.1', 8001)
)

def listen_server():
    while True:
        data = client.recv(2048)
        print(data.decode('utf-8'))

def send_server():
    listen_thread = Thread(target=listen_server)
    listen_thread.start()
    while True:
        client.send(input(':::').encode('utf-8'))
        # data = client.recv(2048)
        # print(data.decode('utf-8'))


def autoriz():
    print(client.recv(2048).decode('utf-8'))
    client.send(input('Введите ваш ник: ').encode('utf-8'))
    client.send(input('Введите ваш код: ').encode('utf-8'))
    #print(client.recv(2048).decode('utf-8'))
    mes = client.recv(2048).decode('utf-8')
    if str(mes) != 'Ваш уникальный код введен не верно. Сообщение не передано.':
        client.send(input('Введите сообщение: ').encode('utf-8'))
        print(client.recv(2048).decode('utf-8'))
    else:
        print(mes)

def your_name():

    client.send(input('Ввведите свой ник:').encode('utf-8'))
    otv = client.recv(2048)
    if str(otv.decode('utf-8')) == 'Это имя занято':
        print(otv.decode('utf-8'))
    else:
        print(otv.decode('utf-8'))
        # print(f'Ваш ник: {name}')
        # print(f'Ваш код: {otv}')
        listen_thread = Thread(target=autoriz)
        listen_thread.start()

if __name__ == '__main__':
    #send_server()
    your_name()
