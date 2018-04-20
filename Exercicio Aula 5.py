import abc

class BaseLasagna(object):
    __metaclass__  = abc.ABCMeta

    @abc.abstractmethod
    def get_ingredients(self):
         """Returns the ingredient list."""

class Bolognesa(BaseLasagna):
    @classmethod
    def get_ingredients(cls):
        return cls(['meat','lasagna noodles'])

class DietLasagna(BaseLasagna):
    @staticmethod
    def get_ingredients():
        return None

