============
Basic Usage
============

Listen for a connection for up to 10 seconds::

    >>> import tcpsleep
    >>> tcpsleep.server.serv(port=1234,timeout=10)
    >>>

If it is woken the return value will contain the remote peer::

    >>> tcpsleep.server.serv(port=1234,timeout=10)
    >>> ('127.0.0.1', 37654)

Wakeup a listening connection::

    >>> import tcpsleep
    >>> tcpsleep.client.wakeup(port=1234)


================
Advanced Usage
================

If your application currently has a backend helper that does something like this::

    while True:
        run_jobs()
        time.sleep(10)

and a frontend on another system that does::

    insert_backend_job()

you can use tcpsleep in place of sleep and send a signal to the backend to wakeup::

    while True:
        run_jobs()
        tcpsleep.server.serv(port=1234, timeout=10)

and on the frontend::

    insert_backend_job()
    tcpsleep.client.wakeup(host='backend', port=1234)
