from tcpsleep import client,server
import time

import threading

def close_to(a,b):
    return abs(a-b) < 0.2


def test_client_no_server():
    assert client.wakeup(12345)==False

def test_server_timeout():
    s = time.time()
    ret = server.serv(port=12345,timeout=1)
    e = time.time()
    assert close_to(e-s, 1)
    assert ret == None

def test_server_with_client():
    def run_server():
        ret = server.serv(port=12345, timeout=3)
        assert ret[0]=='127.0.0.1', ret[0]

    t = threading.Thread(target=run_server)
    t.start()
    time.sleep(0.5)
    cret = client.wakeup(12345)
    assert cret == True
    t.join()



