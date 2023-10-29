import math

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return math.sqrt(number)


def calc(your_number):
    """Проверяет, что принимаемое число меньше или равно 0."""
    if your_number <= 0:
        return 'Квадратный корень можно получить только из положительных чисел'
    calc = calculate_square_root(your_number)
    return print('Мы вычислили квадратный корень из введённого вами числа. '
                 'Это будет:', calc)


print(message)
calc(25.5)
