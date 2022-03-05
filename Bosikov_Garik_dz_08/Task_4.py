from functools import wraps


def val_checker(valid_func):
    def _checker(func):
        @wraps(func)
        def valid(param):
            if isinstance(param, valid_func) and param >= 0:
                return func(param)
            raise ValueError(f'wrong val {param}')

        return valid

    return _checker


@val_checker(int)
def calc_cube(val):
    """Возведение числа в третью степень"""
    return val ** 3

