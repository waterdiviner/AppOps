import threading

def singleton(cls, *args, **kw):
    __instances = {}
    __lock = threading.Lock()

    def _singleton():
        if cls not in __instances:
            __lock.acquire()
            instance = cls(*args, **kw)
            __instances[cls] = instance
            __lock.release()
        return __instances[cls]
    return _singleton

