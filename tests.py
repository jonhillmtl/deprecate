from deprecate import deprecated, DeprecationError
import pytest

@deprecated(
    message="Do not use this function anymore. Use another function instead.",
    current_version='0.2',
    deprecated_in='0.1'
)
def deprecated_func(x, y):
    return x + y

@deprecated(
    message="Do not use this function anymore. Use another function instead.",
    current_version='0.1',
    deprecated_in='0.1'
)
def deprecated_this_version_func(x, y):
    return x + y
    
def not_deprecated_func(x, y):
    return x + y

@deprecated(
    message="Do not use this function anymore. Use another function instead.",
    current_version='0.2',
    deprecated_in='0.3'
)
def not_yet_deprecated_func(x, y):
    return x + y

@deprecated(
    message="Do not use this function anymore. Use another function instead.",
    current_version='melon',
    deprecated_in='otter'
)
def bad_args_deprecated_func(x, y):
    return x + y
    
class ClassWithDeprecatedMethods(object):
    @deprecated(
        message="Do not use this method anymore. Use another method instead.",
        current_version='0.1',
        deprecated_in='0.1'
    )
    def method(x, y):
        return x + y
        
def test_basic():
    with pytest.raises(DeprecationError):
        print(deprecated_func(2, 3))
        print(deprecated_this_version_func(2, 3))
        
    assert not_deprecated_func(2, 3) == 5
    assert not_yet_deprecated_func(2, 3) == 5
    
    with pytest.raises(DeprecationError):
        print(bad_args_deprecated_func(2, 3))
        
    try:
        bad_args_deprecated_func(2, 3)
    except DeprecationError as e:
        print(e)
        
    try:
        deprecated_func(2, 3)
    except DeprecationError as e:
        print(e)
        
    try:
        deprecated_this_version_func(2, 3)
    except DeprecationError as e:
        print(e)
    
    with pytest.raises(DeprecationError):
        cwdf = ClassWithDeprecatedMethods()
        cwdf.method()