"""Calculadora elemental: suma, resta, multiplicación y división."""


class CalculadoraError(Exception):
    """Error de dominio de la calculadora."""


class Calculadora:
    """Operaciones aritméticas básicas."""

    def sumar(self, a: float, b: float) -> float:
        return a + b

    def restar(self, a: float, b: float) -> float:
        return a - b

    def multiplicar(self, a: float, b: float) -> float:
        return a * b

    def dividir(self, a: float, b: float) -> float:
        if b == 0:
            raise CalculadoraError("No se puede dividir entre cero.")
        return a / b
