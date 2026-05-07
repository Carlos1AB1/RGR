"""
Pruebas TDD (red → green → refactor).

Orden sugerido al desarrollar desde cero:
1. Escribir un test que falle (red).
2. Implementar lo mínimo para que pase (green).
3. Mejorar el código sin cambiar el comportamiento (refactor).
"""

import pytest

from calculator import Calculadora, CalculadoraError


@pytest.fixture
def calc() -> Calculadora:
    return Calculadora()


def test_suma(calc: Calculadora) -> None:
    assert calc.sumar(2, 3) == 5
    assert calc.sumar(-1, 1) == 0


def test_resta(calc: Calculadora) -> None:
    assert calc.restar(10, 4) == 6
    assert calc.restar(0, 5) == -5


def test_multiplicacion(calc: Calculadora) -> None:
    assert calc.multiplicar(3, 4) == 12
    assert calc.multiplicar(-2, 5) == -10


def test_division(calc: Calculadora) -> None:
    assert calc.dividir(10, 2) == 5
    assert calc.dividir(7, 2) == 3.5


def test_division_entre_cero(calc: Calculadora) -> None:
    with pytest.raises(CalculadoraError, match="cero"):
        calc.dividir(1, 0)
