from typing import Union

class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def sum(*args):

        if len(args) != 2:
            raise Exception("должно быть два аргумента")
        try:
            return sum(args)
        except TypeError:
            return f"нельзя получить сумму, пытаешься передать не цифры"


    @staticmethod
    def subtract(*args):
        if len(args) != 2:
            raise Exception("должно быть два аргумента")
        total = args[0]

        try:
            for arg in args:
                total -= arg
            return total + args[0]
        except TypeError:
            return f"нельзя получить разность, пытаешься передать не цифры"

    @staticmethod
    def multiply(*args):
        if len(args) != 2:
            raise Exception("должно быть два аргумента")
        total = 1
        try:
            for arg in args:
                total *= arg
            return round(total, 3)
        except TypeError:
            return f"нельзя получить произведение, пытаешься передать не цифры"

    @staticmethod
    def divide(*args):
        if len(args) != 2:
            raise Exception("должно быть два аргумента")
        arg1 = args[0]
        if 0 in args[1:]:
            raise ValueError("Деление на ноль невозможно")
        try:
            for i in args[1:]:
                arg1 /= i
            return round(arg1, 3)
        except TypeError:
            return f"нельзя получить частное, пытаешься передать не цифры"



calcul = Calculator()

#print(calcul.sum(3, .5, 5))
#print(calcul.subtract(2, 1.4345634))
#print(calcul.multiply(2, 3, -4))
#print(calcul.divide(10, 1))