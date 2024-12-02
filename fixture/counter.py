from reactive.observable import Reactive, Computed
from reactive.observer import Watch

counter = Reactive({"value": 1})
doubled_counter = Computed(lambda: counter.value * 2)

Watch(lambda: print("counter.value",counter.value))
Watch(lambda: print("doubled_counter.value",doubled_counter.value))

print(counter.value)
counter.value += 1

counter.value += 1
