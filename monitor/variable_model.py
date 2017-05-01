
class Var(object):
    view_type = ''

    def __init__(self, **kwargs):
        self.name = None
        self.attrs = {}

    def get_toc_item(self):
        ti = {'view_type': self.view_type}
        ti.update(self.attrs)
        return ti


class Supervised(Var):
    def __get__(self, instance, owner):
        raise AttributeError('Should not get from a supervised variable')

    def __set__(self, instance, value):
        instance.supervised[self.name] = value


class PlainSupervised(Supervised):
    view_type = 'plain_s'


class FloatSupervised(Supervised):
    view_type = 'float_s'

    def __init__(self, round_to=None):
        super(FloatSupervised, self).__init__()
        self.attrs['round_to'] = round_to


class ImageSupervised(Supervised):
    view_type = 'image_s'


class Controlled(Var):
    def __init__(self, init):
        super(Controlled, self).__init__()
        self.attrs['init'] = self.value = init

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        raise AttributeError('Should not set a controlled variable')

    def set_value(self, value):
        self.value = value
        print self.value, 'set'
        return 0


class PlainControlled(Controlled):
    view_type = 'plain_c'

    def __init__(self, init):
        super(PlainControlled, self).__init__(init)






