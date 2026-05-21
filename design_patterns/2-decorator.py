#!/usr/bin/env python3
"""Decorator pattern - beverage customization system."""


class Beverage:
    """Abstract base class for all beverages."""

    def cost(self) -> int:
        """Return the cost of the beverage in cents."""
        raise NotImplementedError

    def description(self) -> str:
        """Return the description of the beverage."""
        raise NotImplementedError


class Coffee(Beverage):
    """Represents a plain coffee."""

    def cost(self) -> int:
        """Return the base cost of coffee."""
        return 50

    def description(self) -> str:
        """Return the base description."""
        return "Coffee"


class MilkDecorator(Beverage):
    """Decorator that adds milk to a beverage."""

    def __init__(self, inner: Beverage):
        """Initialize with the wrapped beverage.

        Args:
            inner: the beverage to wrap.
        """
        self._inner = inner

    def cost(self) -> int:
        """Return the cost with milk added."""
        return self._inner.cost() + 10

    def description(self) -> str:
        """Return the description with milk added."""
        return self._inner.description() + " + milk"


class SugarDecorator(Beverage):
    """Decorator that adds sugar to a beverage."""

    def __init__(self, inner: Beverage):
        """Initialize with the wrapped beverage.

        Args:
            inner: the beverage to wrap.
        """
        self._inner = inner

    def cost(self) -> int:
        """Return the cost with sugar added."""
        return self._inner.cost() + 5

    def description(self) -> str:
        """Return the description with sugar added."""
        return self._inner.description() + " + sugar"


class CaramelDecorator(Beverage):
    """Decorator that adds caramel to a beverage."""

    def __init__(self, inner: Beverage):
        """Initialize with the wrapped beverage.

        Args:
            inner: the beverage to wrap.
        """
        self._inner = inner

    def cost(self) -> int:
        """Return the cost with caramel added."""
        return self._inner.cost() + 15

    def description(self) -> str:
        """Return the description with caramel added."""
        return self._inner.description() + " + caramel"


def main():
    """Demonstrate the beverage decorator system."""
    b1 = MilkDecorator(Coffee())
    print("{} {}".format(b1.description(), b1.cost()))

    b2 = MilkDecorator(SugarDecorator(Coffee()))
    print("{} {}".format(b2.description(), b2.cost()))

    b3 = CaramelDecorator(MilkDecorator(SugarDecorator(Coffee())))
    print("{} {}".format(b3.description(), b3.cost()))


if __name__ == "__main__":
    main()
