import time
from table_model import Table
import variable_model as vm


class VariableTable(Table):
    a = vm.SupervisedVariable(vm.IntegerVar(), vm.PlainView())
    b = vm.SupervisedVariable(vm.IntegerVar(), vm.PlainView())

table = VariableTable()
table_access = table.get_access_model()
