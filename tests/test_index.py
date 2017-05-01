"""
Faking some data to display
"""
import itertools
import json
import threading
import time

import numpy

import monitor_server as server
from storage import table

if __name__ == '__main__':

    # Data prepare
    ai = itertools.cycle(range(0, 100))
    bi = itertools.cycle(range(30, 0, -1))

    imgs = None
    with open('tests/b64_imgs.json') as f:
        imgs = json.load(f)
    ii = itertools.cycle(imgs.itervalues())
    ji = itertools.cycle(imgs.itervalues())
    ji.next()

    fi = itertools.cycle(list(numpy.sin(numpy.linspace(0, 2*numpy.pi, 10))))
    gi = itertools.cycle(list(numpy.sin(numpy.linspace(0, 2*numpy.pi, 10))))

    # Update thread target
    def int_update_thread():
        while True:
            table.a = ai.next()
            table.b = bi.next()
            table.f = fi.next()
            table.g = gi.next()
            table.i = ii.next()
            table.j = ji.next()
            time.sleep(1)

    # Start Thread
    t = threading.Thread(target=int_update_thread)
    t.setDaemon(True)
    t.start()

    server.table = table

    server.app.run(debug=True)
