import socket
def wakeup(port,host='127.0.0.1', timeout=0.5):
    """Wake up a listening tcpsleep server

    :param port: The port to connect to
    :param host: The address to connect to
    :param timeout: The socket timeout for connecting
    :returns: True if the server was succesfully reached, False otherwise
    """
    s=socket.socket()
    s.settimeout(timeout)
    try :
        s.connect((host, port))
        s.shutdown(socket.SHUT_RDWR)
        s.close()
        return True
    except:
        return False
