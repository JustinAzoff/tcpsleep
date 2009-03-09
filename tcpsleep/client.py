import socket
def wakeup(port,host='127.0.0.1'):
    s=socket.socket()
    s.setblocking(False)
    try :
        s.connect((host, port))
        s.shutdown(socket.SHUT_RDWR)
        s.close()
        return True
    except:
        return False
