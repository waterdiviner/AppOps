#############################################################################
def singletonno(cls, *args, **kw):
    __instances = {}

    def _singleton():
        if cls not in __instances:
            instance = cls(*args, **kw)
            __instances[cls] = instance
        return __instances[cls]
    return _singleton