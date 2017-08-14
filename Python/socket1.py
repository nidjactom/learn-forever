import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('10.9.225.216', 8090))
cmd = 'GET http://10.9.225.216/nokia-workflow-manager/workflowengine/assets/css/demo.css HTTP/1.1\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
