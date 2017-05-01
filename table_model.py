import variable_model as vm


class TableMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        # Skip the base class Table
        if name == 'Table':
            return type.__new__(mcs, name, bases, attrs)

        variables = {}
        for k, v in attrs.iteritems():
            if isinstance(v, vm.Var):
                if not v.name:
                    v.name = k

                variables[k] = v
                attrs.pop(k)
        attrs['__vars__'] = variables

        return type.__new__(mcs, name, bases, attrs)


class Table(object):
    __metaclass__ = TableMetaclass

    def __init__(self):
        self.supervised = {}
        self.controlled = {}

    def get_supervised(self):
        return self.supervised

    @classmethod
    def extract_toc(cls):
        toc = {}
        for name, var in cls.__vars__.iteritems():
            toc[name] = var.get_toc_item()

        return toc


if __name__ == '__main__':
    class T(Table):
        a = vm.SupervisedVariable(vm.IntegerVar(), vm.View())
        image = vm.SupervisedVariable(vm.ImageVar(), vm.ImageView())

    t = T()
