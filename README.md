# Description

Reactive programming is popular in Web and APP development, where watching data change and triggering side effect (rerender) is a common practice.

Our Reactive-Python is going to implement a reactive programming package like Vue.js's Reactivity Core for Python, helping user interfaces and data streaming and processing in Python easier.

It at least includes `reactive` and `ref` to transform ordinary value or dict into watchable implement. Meanwhile, it should includes `watch`, `watchEffect` and `computed` to watch reactive values' change and register side effects.


# Functions

## observable.Reactive

### Description:

It is a base class for all Observable, which has a private Map attribute to store all Observers. 

It also exposes public getter and setter attributes for observed data.

### Details:

\__init__: Set the private Map to store all Observers and store initial data.

\__getattr__: Hijack data access to track observers.

\__setattr__: Hijack data mutation and trigger observers.

_trigger: Implement of observer trigger for self.\__setattr__.

## observable.Computed

### Description:

It is inherited from base Reactive, which accepts a Watch-like lambda function to do some computation of other Reactive objects. 

It serves as a read-only computed Reactive object, which observes all dependent Reactive objects and always provide the latest computed value. 

Simply, a shortcut for Reactive + Watch.

### Details:

\__init__: Accepts and pass the initial lambda function into self._update method. Set the initial data as {value: None}.

\__setattr__: Overwrite self.\__setattr__ method to make sure its value is read-only.

_update: Wrap the the initial lambda function with a mutation to self.data and pass the function into a Watch.

## observer.Watch

### Description:

It accepts a pure lambda function, where Reactive object are accessed. Effect will track all accessed Reactive objects. And the lambda function will be executed every time these Reactive objects modified.

It has a private Map attribute to store all dependent Reactive objects and provides a method to stop observe.

### Details:

\__init__: Store the initial lambda and call self.\__track__ method.

_track: Call the initial lambda function and track all dependent Reactive objects.

stop: Unregister from all dependent Reactive objects and stop observing.

## observer.WatchAttr

### Description:

It is inherited from base Watch, which receives specific reactive attributes to watch, rather than collecting dependent Reactive object automatically

### Details:

\__init__: Store the initial lambda and call self._track method.

_track: Call the tracker function and track all listed Reactive attributes.

stop: Unregister from all dependent Reactive objects and stop observing.