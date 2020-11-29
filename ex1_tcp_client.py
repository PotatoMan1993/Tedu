"""
tcp客户端
"""

from socket import *

ADDR = ("127.0.0.1", 8888)

s = socket()
s.getsockopt(SOL_SOCKET, SO_REUSEADDR)
s.connect(ADDR)

while True:
    message = input("请输入：")
    if not message:
        break
    s.send(message.encode())
    data = s.recv(1024)
    print("server: ", data.decode())

s.close()
print("客户端断开连接")
