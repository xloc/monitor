"""
All conversions will only compute once:
    For SupervisedVariable, it is done by run extract_converter
    For ControlledVariable, it is performed by converter in JS
"""
from numbers import Number


class SupervisedVariable(object):
    """
    Set only

    return ? before set: some thing represent no-data
    """
    def __init__(self, var, view):
        # type: (Var, View) -> None
        self.var = var
        self.view = view

        self.name = None

    def get_descriptor(self):
        class Variable(object):
            def __set__(s, instance, value):
                if not self.var.extract_validate(value):
                    raise ValueError('Value validation failed')
                instance._vals[self.name] = self.var.extract_converter(value)

            def __get__(self, instance, owner):
                raise AttributeError(
                    'Should not get from a supervised variable')

        return Variable()

    def extract_toc_item(self):
        return (self.name,
                dict(var_type=self.var.type_id,
                     view_type=self.view.type_id))


class ControlledVariable(object):
    """
    Get only
    Return ? before set: init value
    """
    def __init__(self):
        pass


class Var(object):
    type_id = 'plain'

    def extract_converter(self, value):
        return value

    def extract_validate(self, value):
        return True

    pass_validate = "function (value){return true}"
    pass_converter = "function (value){return value}"


class IntegerVar(Var):
    type_id = 'int'

    def extract_validate(self, value):
        return isinstance(value, int)

    pass_validate = '''function (input){
        re=/^[1-9]+[0-9]*]*$/;return re.test(input)
    }'''


class FloatVar(Var):
    type_id = 'float'

    def extract_converter(self, value):
        return float(value)

    def extract_validate(self, value):
        return isinstance(value, Number)

    pass_converter = 'function (input){return parseFloat(float)}'
    pass_validate = '''function (input){
        re=/^[1-9]+[0-9]*]*$/;return re.test(input)
    }'''


class StringVar(Var):
    type_id = 'string'

    def extract_converter(self, value):
        return str(value)

    def extract_validate(self, value):
        return isinstance(value, str)

    pass_converter = ""
    pass_validate = ""


class ImageVar(Var):
    type_id = 'image'

    def extract_converter(self, value):
        return str(value)

    def extract_validate(self, value):
        return isinstance(value, str)

    pass_converter = ""
    pass_validate = ""


class View(object):
    type_id = ''
    view_macro = ""


class PlainView(View):
    type_id = 'plain'

    view_macro = '''
    {% macro show_item(name) -%}
        <p id="var-{{ name }}"></p>
    {%- endmacro %}
    '''
    content_render = '''
    function (name, value){
        $("#var-"+name).text(value)
    }
    '''


class LinePlotView(View):
    type_id = 'line-plot'

    view_macro = ""

    def __init__(self, record_count=30):
        self.record_count = 30


class TimeLineView(View):
    view_macro = ""

    def __init__(self, record_count=30):
        self.record_count = 30


class ImageView(View):
    view_macro = ""


class EditablePlainView(View):
    view_macro = ""

    def __init__(self):
        pass






