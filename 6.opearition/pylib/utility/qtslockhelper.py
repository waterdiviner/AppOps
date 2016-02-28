import threading

class LockGuard:
    ELocked = 1
    EReleased = 2

    def __init__(self, mutex, timout=-1):
        self.mutex = mutex
        self.status = LockGuard.ELocked
        if mutex.acquire(timout):
            return
        else:
            exit("mutex acquire timeout")

    def release(self):
        if self.status == LockGuard.ELocked:
            self.mutex.release()
            self.status == LockGuard.EReleased

    def __del__(self):
        if self.status == LockGuard.ELocked:
            self.mutex.release()

def synchronizer(mutex):
    def getFunc(func):
        def wrappedFunc(*args, **kw):
            LockGuard(mutex)
            func(*args, **kw)
        return wrappedFunc
    return getFunc