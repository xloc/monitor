"""
Faking some data to display
"""
import itertools
import json
import threading
import time

import numpy

import monitor
import monitor.variable_model as vm


class VariableTable(monitor.Table):
    a = vm.PlainSupervised()
    b = vm.PlainSupervised()
    f = vm.FloatSupervised()
    g = vm.FloatSupervised(round_to=2)
    i = vm.ImageSupervised()
    j = vm.ImageSupervised()

    c = vm.PlainControlled(init=3.1415)

table = VariableTable()
monitor.set_tracked_table(table)


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

    monitor.app.run(debug=True)
