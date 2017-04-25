import itertools
import json
import threading
import time

from monitor_server import app
from storage import table

if __name__ == '__main__':

    table.add_var('a', 'plain')

    def int_update_thread():
        var = itertools.cycle(range(0, 100))
        while True:
            table.update(a=var.next())
            time.sleep(1)

    t = threading.Thread(target=int_update_thread)
    t.setDaemon(True)
    t.start()

    table.add_var('image', 'img')

    imgs = None
    with open('b64_imgs.json') as f:
        imgs = json.load(f)

    def img_update_thread():
        var = itertools.cycle(imgs.itervalues())
        while True:
            table.update(image=var.next())
            time.sleep(1)
    tg = threading.Thread(target=img_update_thread)
    tg.setDaemon(True)
    tg.start()

    app.run(host='0.0.0.0',debug=True,threaded=True)
