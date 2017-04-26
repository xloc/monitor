from unittest import TestCase
import model as m


class TestTable(TestCase):
    @classmethod
    def setUpClass(cls):
        class T(m.Table):
            i = m.IntegerVar()
            f = m.FloatVar()
            f4 = m.FloatVar(round=4)
            s = m.StringVar()
            img = m.ImageVar()

        cls.t = T()

    def test_integer_var(self):
        t = self.t

        self.assertEqual(t.i, 0, 'integer default is not 0')

        val = 3
        t.i = val
        self.assertEqual(t.i, val, 'integer is not as assigned')

    def test_float(self):
        t = self.t

        self.assertEqual(t.f, .0, 'float default is not 0.0')

        val = 2.333333333
        t.f = val
        self.assertEqual(t.f, val, 'float is not as assigned')

        t.f4 = val
        self.assertEqual(t.f4, round(val, 4), 'float is not properly rounded')

    def test_string_var(self):
        t = self.t

        self.assertEqual(t.s, '', 'string default is not ""')

        val = 'some thing'
        t.s = val
        self.assertEqual(t.s, val, 'string is not as assigned')

        val = 23333
        t.s = val
        self.assertEqual(t.s, str(val), 'string var conversion is not correct')

    def test_img_var(self):
        t = self.t


        # print t.img

        # self.assertEqual(
        #     t.img,
        #     , 'default is not something')

    def test_extract_all(self):
        print self.t.extract_all()


