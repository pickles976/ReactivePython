# Dynamic class generation from Fluent Python pg. 683 
from lib.signals import Signal, effect, derived

def makeStore(data: dict, cls_name: str = "Store"):
    def __init__(self, *args, **kwargs):
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for name, value in attrs.items():
            setattr(self, name, Signal(value))

    def __iter__(self):
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self):
        str = f"{self.__class__.__name__}("
        for name in self.__slots__:
            str += f"{name}: {getattr(self, name).value}, "
        str = str[:-2] + ")"
        return str

    cls_attrs = dict(__slots__=data.keys(), __init__=__init__, __iter__=__iter__, __repr__=__repr__)
    StoreClass = type(cls_name, (object,), cls_attrs)
    return StoreClass(**data)