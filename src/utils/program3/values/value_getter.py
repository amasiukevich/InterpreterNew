from .value import Value


class ValueGetter(Value):


    def __init__(self, base_getters=[]):
        self.base_getters = base_getters


    def __repr__(self):
        return ".".join(self.base_getters)


    def get_num_base_getters(self):
        return len(self.base_getters)