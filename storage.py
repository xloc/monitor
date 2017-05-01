from table_model import Table
import variable_model as vm


class VariableTable(Table):
    a = vm.PlainSupervised()
    b = vm.PlainSupervised()
    f = vm.FloatSupervised()
    g = vm.FloatSupervised(round_to=2)
    i = vm.ImageSupervised()
    j = vm.ImageSupervised()

    c = vm.PlainControlled(init=3.1415)

table = VariableTable()
