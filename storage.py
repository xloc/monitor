import time
import model as m


class VariableTable(m.Table):
    a = m.IntegerVar()
    img = m.Var()

table = VariableTable()
