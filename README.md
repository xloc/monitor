# Monitor

A Simple Variable Supervision and Control application written in python

## Usage
### Step 1: Make a table
```python
import monitor
from monitor import variable_model as vm

class VariableTable(monitor.Table):
    a = vm.PlainSupervised()
    b = vm.PlainSupervised()
    f = vm.FloatSupervised()
    g = vm.FloatSupervised(round_to=2)
    i = vm.ImageSupervised()
    j = vm.ImageSupervised()

    c = vm.PlainControlled(init=3.1415)
    
table = VariableTable()
```

### Step 2: Assign table to app
```python
import monitor
monitor.set_tracked_table(table)
```

### Step 3: Run app in a new thread
The multiprocessing one has not yet developed, so use a new thread to start the server
```python
import threading
import monitor

threading.Thread(target=monitor.app).start()
```

### Step 4: Change variable in your app
Manipulate variables in the table instance as usual.
> Notice: The variables end with `Supervised` are not readable, and the ones end with `Controlled` is not Writable 

```python
table.a = 233

# And later
table.a = 2333
```

### Step 5: Monitor your variables in the browser 

## Achievement Demonstration
- Install all dependency
- Set PYTHONPATH `export PYTHONPATH=<path of monitor app>`
- Run `python tests/test_index.py`