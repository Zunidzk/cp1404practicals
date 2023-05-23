import random

from prac_09.car import Car


class UnreliableCar(Car):
    def __init__(self, reliability=0.0, **kwargs):
        super().__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0
