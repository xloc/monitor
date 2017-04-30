"""
Faking some data to display
"""
import itertools
import json
import threading
import time

from monitor_server import app
from storage import table_access as table

if __name__ == '__main__':

    # Data prepare
    a_iter = itertools.cycle(range(0, 100))
    b_iter = itertools.cycle(range(30, 0, -1))

    imgs = None
    with open('b64_imgs.json') as f:
        imgs = json.load(f)
    image_iter = itertools.cycle(imgs.itervalues())
    image_other_iter = itertools.cycle(imgs.itervalues())
    image_other_iter.next()

    # Update thread target
    def int_update_thread():
        while True:
            table.a = a_iter.next()
            table.b = b_iter.next()
            table.image = image_iter.next()
            table.image_other = image_other_iter.next()

            time.sleep(1)

    # Start Thread
    t = threading.Thread(target=int_update_thread)
    t.setDaemon(True)
    t.start()

    app.run(debug=True)
