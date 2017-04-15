
class VariableTable(object):
    def __init__(self):
        self.value = {}

    def update(self, name, value):
        # type: (str, object) -> None
        self.value[name] = value

    def extract(self):
        # type: () -> dict
        return self.value.copy()

table = VariableTable()