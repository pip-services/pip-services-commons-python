import datetime

class TestClass:
    _private_field = 123
    public_field = "ABC"
    _public_prop = datetime.datetime.now()

    def __init__(arg1):
        pass

    def _get_private_prop():
        return 543

    def _set_private_prop(value):
        pass

    def get_public_prop():
        return self._public_prop

    def set_public_prop(value):
        self._public_prop = value

    public_prop = property(get_public_prop, set_public_prop)

    def _private_method():
        pass

    def public_method(arg1, arg2):
        return arg1 + arg2
