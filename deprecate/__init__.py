from functools import wraps
from distutils.version import StrictVersion

deprecation_error_message = """
DeprecationError: {0}
    {1} was deprecated in version {2}.
    Your current version is {3}.
"""

class DeprecationError(Exception):
    def __init__(self, func, message, current_version, deprecated_in):
        self.func = func
        self.message = message
        self.current_version = current_version
        self.deprecated_in = deprecated_in
        
    def __str__(self):
        return deprecation_error_message.format(
            self.message,
            self.func.__name__,
            self.deprecated_in,
            self.current_version
        )
        
    
def deprecated(message, current_version, deprecated_in):
    def _impl(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if StrictVersion(str(current_version)) >= StrictVersion(str(deprecated_in)):
                    raise DeprecationError(func, message, current_version, deprecated_in)
            except ValueError as e:
                raise DeprecationError(func, message, "<unknown>", "<unknown>")
            
            return func(*args, **kwargs)
        return wrapper
    return _impl