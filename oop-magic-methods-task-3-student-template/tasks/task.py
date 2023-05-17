from __future__ import annotations
from typing import Type


class Currency:
    """
    1 EUR = 2 USD = 100 GBP

    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """

    def __init__(self, value: float):
        pass

    def __init__(self, value: float):
        self.value = value

    def __str__(self):
        return f"{self.value} {self.__class__.__name__}"

    def __repr__(self):
        return str(self)

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        if cls == other_cls:
            return f"1 {cls.__name__} = 1 {cls.__name__}"
        elif cls == Euro and other_cls == Dollar:
            return f"2.0 USD for 1 EUR"
        elif cls == Euro and other_cls == Pound:
            return f"100.0 GBP for 1 EUR"
        elif cls == Dollar and other_cls == Euro:
            return f"0.5 EUR for 1 USD"
        elif cls == Dollar and other_cls == Pound:
            return f"50.0 GBP for 1 USD"
        elif cls == Pound and other_cls == Euro:
            return f"0.01 EUR for 1 GBP"
        elif cls == Pound and other_cls == Dollar:
            return f"0.02 USD for 1 GBP"
        else:
            return "Unknown conversion"

    def to_currency(self, other_cls: Type[Currency]) -> Currency:
        if self.__class__ == other_cls:
            return self
        else:
            ratio_str = self.__class__.course(other_cls)
            ratio = float(ratio_str.split()[0])
            return other_cls(self.value * ratio)

    def __add__(self, other: Currency) -> Currency:
        ratio = float(other.to_currency(self.__class__).split()[0])
        return self.__class__(self.value + other.value / ratio)

    def __sub__(self, other: Currency) -> Currency:
        ratio = float(other.to_currency(self.__class__).split()[0])
        return self.__class__(self.value - other.value / ratio)

    def __eq__(self, other: Currency) -> bool:
        return self.value == other.to_currency(self.__class__).value

    def __gt__(self, other: Currency) -> bool:
        return self.value > other.to_currency(self.__class__).value

    def __lt__(self, other: Currency) -> bool:
        return self.value < other.to_currency(self.__class__).value


class Euro(Currency):
    pass


class Dollar(Currency):
    pass


class Pound(Currency):
    pass
