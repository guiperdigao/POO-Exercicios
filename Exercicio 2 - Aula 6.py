# Decorators
from functools import wraps

def Caracteristica(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        return orig_func(*args, **kwargs)

    return wrapper

@Caracteristica
def display_info(name, age):
    print('{} tem {} anos'.format(name, age))

display_info('Joao', 25)
display_info('Carla', 37)