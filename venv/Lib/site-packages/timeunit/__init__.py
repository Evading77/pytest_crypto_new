# -*- coding: utf-8 -*-

from __future__ import division
import time as _time

'''
timeunit:
    timeunit base on java.util.concurrent.TimeUnit

    Sample:
        >>> import timeunit
        >>> timeunit.seconds.to_millis(5)
        5000
'''


# Handy constants for conversion methods
_C0 = 1
_C1 = _C0 * 1000
_C2 = _C1 * 1000
_C3 = _C2 * 1000
_C4 = _C3 * 60
_C5 = _C4 * 60
_C6 = _C5 * 24

_C = [_C0, _C1, _C2, _C3, _C4, _C5, _C6]

class _BaseTimeUnit(object):
    def __init__(self, index, name):
        self._index = index
        self._name = name

    @property
    def index(self):
        return self._index

    @property
    def name(self):
        return self._name

    def to_nanos(self, d):
        return d / (_C[0]/_C[self.index])

    def to_micros(self, d):
        return d / (_C[1]/_C[self.index])

    def to_millis(self, d):
        return d / (_C[2]/_C[self.index])

    def to_seconds(self, d):
        return d / (_C[3]/_C[self.index])

    def to_minutes(self, d):
        return d / (_C[4]/_C[self.index])

    def to_hours(self, d):
        return d / (_C[5]/_C[self.index])

    def to_days(self, d):
        return d / (_C[6]/_C[self.index])

    def convert(self, source_duration, source_unit):
        return source_duration/ (_C[self._index] / _C[source_unit.index])

    def sleep(self, timeout):
        if timeout < 0:
            timeout = 0
        _time.sleep(self.to_seconds(timeout))

nanoseconds = _BaseTimeUnit(0, "nanoseconds")
microseconds = _BaseTimeUnit(1, "microseconds")
milliseconds = _BaseTimeUnit(2, "milliseconds")
seconds = _BaseTimeUnit(3, "seconds")
minutes = _BaseTimeUnit(4, "minutes")
hours = _BaseTimeUnit(5, "hours")
days = _BaseTimeUnit(6, "days")
