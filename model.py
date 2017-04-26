from cv2 import imencode
import numpy
import base64

_sentinel = object()


class Var(object):
    """
    Server Read-only Variable Descriptor
    """
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.default = kwargs.get('default', lambda: None)
        self.type = kwargs.get('type', 'plain')

    def __get__(self, instance, owner):
        v = getattr(instance, '_'+self.name, _sentinel)
        if v is _sentinel:
            v = self.default()

        return self.get_converter(v)

    def __set__(self, instance, value):
        setattr(instance, '_'+self.name, value)

    def get_converter(self, value):
        return value


class IntegerVar(Var):
    def __init__(self, **kwargs):
        kwargs['default'] = lambda: 0
        super(IntegerVar, self).__init__(**kwargs)

    def get_converter(self, value):
        return int(value)


class FloatVar(Var):
    def __init__(self, **kwargs):
        self.digits = kwargs.pop('round', None)

        kwargs['default'] = lambda: .0
        super(FloatVar, self).__init__(**kwargs)

    def get_converter(self, value):
        return round(value, self.digits) if self.digits is not None else value


class StringVar(Var):
    def __init__(self, **kwargs):
        kwargs['default'] = lambda: ''
        super(StringVar, self).__init__(**kwargs)

    def get_converter(self, value):
        return str(value)


class ImageVar(Var):
    def __init__(self, **kwargs):
        kwargs['default'] = lambda: numpy.array([[0]])
        kwargs['type'] = 'img:jpg'
        super(ImageVar, self).__init__(**kwargs)

    def get_converter(self, value):
        encoded = imencode('.jpg', value)[1].tostring()
        b64ed = base64.b64encode(encoded)
        return b64ed


class TableMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        # Skip the base class Table
        if name == 'Table':
            return type.__new__(mcs, name, bases, attrs)

        for k, v in attrs.iteritems():
            if isinstance(v, Var):
                if not v.name:
                    v.name = k

        return type.__new__(mcs, name, bases, attrs)


class Table(object):
    __metaclass__ = TableMetaclass

    def __init__(self):
        super(Table, self).__init__()

    def extract_all(self):
        data = dict()

        for k, v in self.__class__.__dict__.iteritems():
            if isinstance(v, Var):
                data[k] = getattr(self, k)

        return data

    def extract_toc(self):
        data = {}
        for k, v in self.__class__.__dict__.iteritems():
            if isinstance(v, Var):
                data[k] = v.type

