from reactive.observable import Reactive
from reactive.observer import Watch

counter = Reactive({"value": 1})

Watch(lambda: print(counter.value))
print(counter.value)
counter.value += 1

counter.value += 1
