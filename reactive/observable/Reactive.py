from reactive.shared import current_observer


class Reactive:
    def __init__(self, obj):
        self._data = obj
        self._observers = []

    def __getter(self, key):
        current_observer_ = current_observer[-1]
        self._observers.append(current_observer_)
        current_observer_._deps.append(self)
        return self._data[key]

    def __setter(self, key, value):
        self._data[key] = value
        self._trigger()

    def _trigger(self):
        for observer in self._observers:
            observer._track()
