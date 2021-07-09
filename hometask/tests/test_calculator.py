""" Calculator module test cases """
from math import sqrt
from typing import Any

import pytest

from hometask.calculator import Calculator


@pytest.mark.parametrize(
    'x, y',
    [
        (2, 3),
        (-2, 3),
        (2, -3),
        (-2, -3),
    ]
)
def test_add_valid(
        calculator: Calculator,
        x: int,
        y: int,
):
    assert x + y == calculator.add(x, y)


@pytest.mark.parametrize(
    'x, y, expected',
    [
        ([], 3, TypeError),
        ({}, 3, TypeError),
        ((1, 2), -3, TypeError),
        ('2', -3, TypeError),
    ]
)
def test_add_invalid(
        calculator: Calculator,
        x: int,
        y: int,
        expected: Exception,
):
    with pytest.raises(expected):
        calculator.add(x, y)


@pytest.mark.parametrize(
    'x, y',
    [
        (4, 2),
        (-4, 2),
        (4, -2),
        (-4, -2),
    ]
)
def test_subtract_valid(
        calculator: Calculator,
        x: int,
        y: int,
):
    assert x - y == calculator.subtract(x, y)


@pytest.mark.parametrize(
    'x, y, expected',
    [
        ([], 3, TypeError),
        ({}, 3, TypeError),
        ((1, 2), -3, TypeError),
        ('2', -3, TypeError),
    ]
)
def test_subtract_invalid(
        calculator: Calculator,
        x: int,
        y: int,
        expected: Exception,
):
    with pytest.raises(expected):
        calculator.subtract(x, y)


@pytest.mark.parametrize(
    'x, y',
    [
        (4, 2),
        (-4, 2),
        (4, -2),
        (-4, -2),
    ]
)
def test_divide_valid(
        calculator: Calculator,
        x: int,
        y: int,
):
    assert x / y == calculator.divide(x, y)


@pytest.mark.parametrize(
    'x, y, expected',
    [
        ([], 3, TypeError),
        ({}, 3, TypeError),
        ((1, 2), -3, TypeError),
        ('2', -3, TypeError),
        (3, 0, ZeroDivisionError),
    ]
)
def test_divide_invalid(
        calculator: Calculator,
        x: int,
        y: int,
        expected: Exception,
):
    with pytest.raises(expected):
        calculator.divide(x, y)


@pytest.mark.parametrize(
    'x, y',
    [
        (4, 2),
        (-4, 2),
        (4, -2),
        (-4, -2),
    ]
)
def test_multiply_valid(
        calculator: Calculator,
        x: int,
        y: int,
):
    assert x * y == calculator.multiply(x, y)


@pytest.mark.parametrize(
    'x, y, expected',
    [
        ([], 3, TypeError),
        ({}, 3, TypeError),
        ((1, 2), -3, TypeError),
        ('2', -3, TypeError),
    ]
)
def test_multiply_invalid(
        calculator: Calculator,
        x: int,
        y: int,
        expected: Exception,
):
    with pytest.raises(expected):
        calculator.multiply(x, y)


@pytest.mark.parametrize(
    'x, y',
    [
        (4, 2),
        (-4, 2),
        (4, -2),
        (-4, -2),
    ]
)
def test_mod_valid(
        calculator: Calculator,
        x: int,
        y: int,
):
    assert x % y == calculator.mod(x, y)


@pytest.mark.parametrize(
    'x, y, expected',
    [
        ([], 3, TypeError),
        ({}, 3, TypeError),
        ((1, 2), -3, TypeError),
        ('2', -3, TypeError),
        (3, 0, ZeroDivisionError),
    ]
)
def test_mod_invalid(
        calculator: Calculator,
        x: int,
        y: int,
        expected: Exception,
):
    with pytest.raises(expected):
        calculator.mod(x, y)


@pytest.mark.parametrize(
    'x, y',
    [
        (4, 2),
        (-4, 2),
        (4, -2),
        (-4, -2),
    ]
)
def test_power_valid(
        calculator: Calculator,
        x: int,
        y: int,
):
    assert x ** y == calculator.power(x, y)


@pytest.mark.parametrize(
    'x, y, expected',
    [
        ([], 3, TypeError),
        ({}, 3, TypeError),
        ((1, 2), -3, TypeError),
        ('2', -3, TypeError),
    ]
)
def test_power_invalid(
        calculator: Calculator,
        x: int,
        y: int,
        expected: Exception,
):
    with pytest.raises(expected):
        calculator.power(x, y)


@pytest.mark.parametrize(
    'x',
    [
        4,
        3,
        2,
        1,
    ]
)
def test_root_valid(
        calculator: Calculator,
        x: int,
):
    assert sqrt(x) == calculator.root(x)


@pytest.mark.parametrize(
    'x, expected',
    [
        ([], TypeError),
        ({}, TypeError),
        ((1, 2), TypeError),
        ('2', TypeError),
        (-1, ValueError),
    ]
)
def test_root_invalid(
        calculator: Calculator,
        x: int,
        expected: Exception,
):
    with pytest.raises(expected):
        calculator.root(x)


@pytest.mark.parametrize(
    'value, expected',
    [
        ({}, TypeError),
        ([], TypeError),
        ((1, 2), TypeError),
        ('1', TypeError),
    ]
)
def test_is_number(
        calculator: Calculator,
        value: Any,
        expected: Exception,
):
    with pytest.raises(expected):
        calculator.is_number(value)
