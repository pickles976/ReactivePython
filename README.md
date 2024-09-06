# Svelte-style stores in python

### Javascript

`main.js`

```javascript
import { data } from "../../stores";
```

`stores.js`

```javascript
import { writable } from 'svelte/store';

export let data = writable({
    "jobs": [],
    "experiments": []
})
```

### Python

`main.py`

```python
from stores import data
```

`stores.py`

```python
from sleek import makeStore
data = makeStore({
    "jobs": [],
    "experiments": []
})
```

How do we get here?


```python
from signals import Signal

def makeStore(data: dict):
    
    # Make an __init__() that wraps every field in a Signal
    
    # Make a custom class
    CustomClass = type(...)
    
    return CustomClass(**data)

```

### Example

```python
from src.sleek import makeStore

data = makeStore({
    "jobs": [],
    "experiments": []
})

# Sugar for adding an effect, same as: `effect(lambda: print(data.jobs.value))`
data.jobs += lambda: print(f"Job: {data.jobs.value}")
data.jobs.value = 6

# Create a derived value
double = derived(lambda: data.jobs.value * 2)
double += lambda: print(f"Job Double: {data.jobs.value}")

data.experiments += lambda: print(f"Experiments: {data.experiments.value}")
data.experiments.value += ["Experiment 1"]
data.experiments.value += ["Experiment 2"]

# Does not call setter!!! Will not emit a signal!
data.experiments.value.append("Experiment 3")
```