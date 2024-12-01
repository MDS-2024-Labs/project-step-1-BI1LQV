from reactive.shared import current_observer


class Watch:
    def __init__(self, effect):
        self._effect = effect
        self._deps = []

    def _track(self):
        current_observer.append(self)
        self._effect()
        current_observer.pop()

    def stop(self):
        for dep in self._deps:
            dep._observers.remove(self)
        self._deps = []
        self._effect = None
