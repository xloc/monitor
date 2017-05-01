"""
Faking some data to display
"""
import itertools
import json
import threading
import time

import numpy

from monitor_server import app
from storage import table_access as table

if __name__ == '__main__':

    # Data prepare
    ai = itertools.cycle(range(0, 100))
    bi = itertools.cycle(range(30, 0, -1))

    imgs = None
    with open('b64_imgs.json') as f:
        imgs = json.load(f)
    ii = itertools.cycle(imgs.itervalues())
    ji = itertools.cycle(imgs.itervalues())
    ji.next()

    fi = itertools.cycle(list(numpy.sin(numpy.linspace(0, 2*numpy.pi, 10))))
    gi = itertools.cycle(list(numpy.cos(numpy.linspace(0, 2*numpy.pi, 10))))

    # Update thread target
    def int_update_thread():
        while True:
            table.ai = ai.next()
            table.bi = bi.next()
            table.fi = fi.next()
            table.gi = gi.next()
            table.ii = ii.next()
            table.ji = ji.next()

    # Start Thread
    t = threading.Thread(target=int_update_thread)
    t.setDaemon(True)
    t.start()

    app.run(debug=True)
