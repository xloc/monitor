import time


class VariableTable(object):
    def __init__(self):
        self.value = {}
        
        self.update_time = {}
        self.last_extract_time = 0

    def update(self, **kwargs):
        now = time.time()
        for name, value in kwargs.iteritems():
            self.value[name] = value
            self.update_time[name] = now

    def extract(self):
        # type: () -> dict
        result = {
            k: self.value[k]
            for k, updated_time in self.update_time.iteritems()
            if updated_time > self.last_extract_time
        }
        self.last_extract_time = time.time()
        return result

table = VariableTable()
