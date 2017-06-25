# Description

A Python decorator that allows you to mark a function or method as deprecated. Deprecated functions will raise a `DeprecationError`.

You can specify your `current_version` and the `deprecated_in` message.

# Installation

`pip install git+https://github.com/jonhillmtl/deprecate`

# Usage

```
from deprecate import deprecated, DeprecationError

@deprecated(
    message="Do not use this function anymore. Use another function instead.",
    current_version='0.2',
    deprecated_in='0.1'
)
def func(x, y):
    return x + y

```

or equally on a class method:

```
from deprecate import deprecated, DeprecationError

class ClassWithDeprecatedMethods(object):
    @deprecated(
        message="Do not use this method anymore. Use another method instead.",
        current_version='0.1',
        deprecated_in='0.1'
    )
    def method(x, y):
        return x + y
```

both `func`  and `method` above will raise a `DeprecationError`.

