======================
Command line interface
======================

tcpsleep
--------

.. program:: tcpsleep

.. cmdoption:: -p

   Port to listen on

.. cmdoption:: -s

   Source address to listen on. Defaults to INADDR_ANY.

Example
~~~~~~~

Lets have tcpsleep sleep for 5 seconds while listening on port 1234::

    $ tcpsleep 5 -p 1234 && echo 'woken up'
    $

If nothing connects to port 1234, tcpsleep will exit with an exit code of 1.
You can read that command line as "sleep for 5 seconds and if woken up echo somethin"

If we re-run that same command, but this time use telnet to connect to port 1234::

    $ tcpsleep 5 -p 1234 && echo 'woken up'
    127.0.0.1 41668
    woken up
    $

tcpsleep prints to stderr the remote host and port that caused the wakeup
