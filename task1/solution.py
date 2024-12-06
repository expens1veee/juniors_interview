import functools


def strict(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        arg_names = list(annotations.keys())[:-1]  # Убираем аннотацию возвращаемого типа
        for i, arg in enumerate(args):
            if not isinstance(arg, annotations[arg_names[i]]):
                raise TypeError(f'Variable {arg_names[i]} must be {annotations[arg_names[i]]}')

        return func(*args, **kwargs)
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


# print(sum_two(1, 2))
# print(sum_two(2, 2.7))