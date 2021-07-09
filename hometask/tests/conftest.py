import pytest

from hometask.calculator import Calculator


@pytest.fixture()
def calculator() -> Calculator:
    return Calculator()
