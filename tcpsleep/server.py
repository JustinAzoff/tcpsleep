import socket
from select import select
def serv(port,host='0.0.0.0', timeout=0):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host,port))
    s.listen(0)
    ret = select([s],[],[], timeout)
    addr = None
    if ret[0]:
        _, addr = s.accept()
        s.shutdown(socket.SHUT_RDWR)
    s.close()
    return addr

def main():
    import sys
    from optparse import OptionParser
    parser = OptionParser(usage = "usage: %prog [options] timeout")
    parser.add_option("-p", "--port", dest="port", action="store", default=None,
            help="port to listen on", type="int")
    parser.add_option("-s", "--source", dest="addr", action="store", default='0.0.0.0',
            help="source address to listen on")

    (options, args) = parser.parse_args()

    if not options.port:
        sys.stderr.write("Specify port to listen on\n")
        parser.print_help()
        sys.exit(1)

    timeout = 0
    if args:
        timeout = float(args[0])

    ret = serv(options.port, options.addr, timeout)
    if ret:
        print ret[0], ret[1]
        sys.exit(0)
    else:
        sys.exit(1)
