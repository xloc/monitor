import time
import model as m


class VariableTable(m.Table):
    a = m.IntegerVar()
    image = m.Var(type='img:jpg')

table = VariableTable()
