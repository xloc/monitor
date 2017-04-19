import itertools
import threading
import time

from monitor_server import app
from storage import table

if __name__ == '__main__': 
    # var = itertools.count(0)
    def update_thread():
        var = itertools.cycle(range(0, 100))
        while True:
            table.update(a=var.next())
            time.sleep(1)
    t = threading.Thread(target=update_thread)
    t.setDaemon(True)
    t.start()

    app.run(debug=True)
