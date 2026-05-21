#!/usr/bin/env python3
"""Factory pattern - vehicle registry."""


class Vehicle:
    """Base class for all vehicles."""

    def mode(self) -> str:
        """Return the travel mode of the vehicle."""
        raise NotImplementedError


class Bus(Vehicle):
    """Represents a bus."""

    def mode(self) -> str:
        """Return the travel mode."""
        return "road"


class Train(Vehicle):
    """Represents a train."""

    def mode(self) -> str:
        """Return the travel mode."""
        return "rails"


class Bike(Vehicle):
    """Represents a bike."""

    def mode(self) -> str:
        """Return the travel mode."""
        return "lane"


class Scooter(Vehicle):
    """Represents a scooter."""

    def mode(self) -> str:
        """Return the travel mode."""
        return "scooter_lane"


class VehicleFactory:
    """Factory that creates vehicles via a registry."""

    def __init__(self):
        """Initialize the factory with an empty registry."""
        self._registry = {}

    def register_kind(self, name: str, cls) -> None:
        """Register a vehicle class under a given name.

        Args:
            name: the string key to associate with the class.
            cls: the vehicle class to register.
        """
        self._registry[name] = cls

    def create(self, kind: str) -> Vehicle:
        """Create and return a vehicle instance by kind.

        Args:
            kind: the registered name of the vehicle type.

        Returns:
            A new instance of the registered vehicle class.

        Raises:
            ValueError: if kind is not registered.
        """
        if kind not in self._registry:
            raise ValueError("Unknown vehicle kind: {}".format(kind))
        return self._registry[kind]()


def main():
    """Demonstrate the vehicle factory."""
    factory = VehicleFactory()
    factory.register_kind("bus", Bus)
    factory.register_kind("train", Train)
    factory.register_kind("bike", Bike)
    factory.register_kind("scooter", Scooter)

    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
