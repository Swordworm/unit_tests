""" Home task about pytest  """
from hometask.calculator.calculator import Calculator


def main():
    calculator = Calculator()
    print(calculator.add(4, 2))
    print(calculator.subtract(4, 2))
    print(calculator.divide(4, 2))
    print(calculator.multiply(4, 2))
    print(calculator.mod(4, 2))
    print(calculator.power(4, 2))
    print(calculator.root(4))


if __name__ == '__main__':
    main()
