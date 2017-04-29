import time
from table_model import Table
import variable_model as vm


class VariableTable(Table):
    a = vm.SupervisedVariable(vm.IntegerVar(), vm.View())
    image = vm.SupervisedVariable(vm.ImageVar(), vm.ImageView())

table = VariableTable()
table_access = table.get_access_model()
