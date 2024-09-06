# An experiment translated from:
# https://www.youtube.com/watch?v=1TSLEzNzGQM&t=660s

from typing import Optional

subscriber = None


class Signal:
    """A signal wraps a value and provides reactivity.
    Subscribers are added with the `effect` function.
    When the wrapped value is changed, it will automatically call all subscribed functions."""

    def __init__(self, value: Optional[any] = None):
        self.subscriptions = set()
        self._value = value

    @property
    def value(self):
        global subscriber
        if subscriber is not None:
            self.subscriptions.add(subscriber)
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
        for sub in self.subscriptions:
            sub()

    # def __iadd__(self, other):
    #     self.value += other
    #     return self

    def __iadd__(self, fn):
        effect(fn)
        return self


def effect(fn):
    global subscriber
    subscriber = fn
    fn()
    subscriber = None


def derived(fn):
    _der = Signal()
    _fn = fn

    def temp():
        _der.value = _fn()

    effect(temp)
    return _der
