import variable_model as vm


class TableMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        # Skip the base class Table
        if name == 'Table':
            return type.__new__(mcs, name, bases, attrs)

        for k, v in attrs.iteritems():
            if isinstance(v, (vm.SupervisedVariable, vm.ControlledVariable)):
                if not v.name:
                    v.name = k

        return type.__new__(mcs, name, bases, attrs)


class Table(object):
    __metaclass__ = TableMetaclass

    def __init__(self):
        self.vals = {}

    def get_access_model(self):
        class_dict = {'_vals': self.vals}
        for v in self.__class__.__dict__.itervalues():
            if isinstance(v, vm.SupervisedVariable):
                class_dict[v.name] = v.get_descriptor()
        return type('AccessTable', (object,), class_dict)()

    def exchange_data(self):
        return self.vals

    @classmethod
    def extract_toc(cls):
        supervised = {}
        for v in cls.__dict__.itervalues():
            if isinstance(v, vm.SupervisedVariable):
                name, info = v.extract_toc_item()
                supervised[name] = info

        return supervised

    @classmethod
    def extract_renderer(cls):
        view_classes = {
            v for v in vars(vm).itervalues() if (
                v is vm.PlainView)
            # isinstance(v, type) and
            # issubclass(v, vm.View) and
            # v is not vm.View)
        }
        return {v.type_id: v.content_renderer for v in view_classes}


if __name__ == '__main__':
    class T(Table):
        a = vm.SupervisedVariable(vm.IntegerVar(), vm.PlainView())

    t = T()
    # print t.extract_toc()
    # ta = t.get_access_model()
    # ta.a = 1
    # print t.vals
    t.extract_renderer()
