import time


class VariableTable(object):
    def __init__(self):
        self.value = {}
        self.format = {}
        
        self.update_time = {}
        self.last_extract_time = 0

    def add_var(self, name, fmt):
        self.format[name] = fmt

    def update(self, **kwargs):
        now = time.time()
        for name, value in kwargs.iteritems():
            if name in self.format.keys():
                self.value[name] = value
                self.update_time[name] = now
            else:
                raise ValueError('Update non-exist variable')

    def extract(self):
        # type: () -> dict
        result = {
            k: {'format': self.format[k], 'value': self.value[k]}
            for k, updated_time in self.update_time.iteritems()
            if updated_time > self.last_extract_time
        }
        result = {'vars': result}

        self.last_extract_time = time.time()
        return result

table = VariableTable()
