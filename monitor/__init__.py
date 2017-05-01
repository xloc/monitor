# coding=utf-8

from monitor_server import app
from table_model import Table


# This is 耍流氓
def set_tracked_table(table):
    import monitor_server as s
    s.table = table
