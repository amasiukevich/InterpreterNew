from .value import Value


class ValueGetter(Value):


    def __init__(self, base_getters=[]):
        self.base_getters = base_getters


    def __str__(self):

        if self.get_num_base_getters() == 1:
            return f"{self.base_getters[0]}"
        else:
            try:
                return ".".join([str(base_getter) for base_getter in self.base_getters])
            except:
                breakpoint()

    def __repr__(self):
        return self.__str__()


    def is_empty(self):
        return self.base_getters == []


    def get_num_base_getters(self):
        return len(self.base_getters)