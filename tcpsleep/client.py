import socket
def wakeup(port,host='0.0.0.0'):
    s=socket.socket()
    try :
        s.connect((host, port))
        s.shutdown(socket.SHUT_RDWR)
        s.close()
        return True
    except:
        return False
