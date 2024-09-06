from lib.signals import Signal, effect
from lib.sleek import makeStore

data = makeStore({
    "jobs": 0,
    "experiments": []
})