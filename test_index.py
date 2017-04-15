import itertools
import threading
import time

from monitor_server import app
from storage import table

if __name__ == '__main__':
    var = itertools.cycle(range(0, 100))

    def update_thread():
        table.update(a=var.next())
        time.sleep(1)
    t = threading.Thread(target=update_thread)
    t.setDaemon(True)
    t.start()

    app.run(debug=True)
