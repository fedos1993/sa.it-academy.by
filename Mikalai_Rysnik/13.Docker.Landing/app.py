import socket
import time


def serverTCP(port=6000, host='127.0.0.1'):
    ''' Сервер, ожидает входное соединение для получения данных и отсылает ответ после '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
    try:
        s.bind((host, port))
        s.listen()
        print('wait connect host: %s, port: %s' % (host, port))

        while True:
            conn, addr = s.accept()
            print('request from: ', addr)
            while True:
                data = conn.recv(512)
                print(data)
                conn.sendall(b'Hello')
            time.sleep(2)

    except Exception as e:
        print("ERROR ", e)
        s.close()


serverTCP(port=9090, host='')



# import socket

# sock = socket.socket()
# sock.bind(('', 9090))
# sock.listen(1)
# conn, addr = sock.accept()

# print('connected: ', addr)

# while True:
#     data = conn.recv(1024)
#     if not data:
#         break
#     conn.send(data.upper())

# conn.close()