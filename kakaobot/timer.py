 #-*- coding: utf-8 -*-

import threading


def hello():
    return "hello, world"

def fuck():
    return "fuck you!"

class pytimer():
    def __init__(self, time, func):
        self.time = time
        self.func = func
        t = threading.Timer(self.time, self.func)
        t.start()
