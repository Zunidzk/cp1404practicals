from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flag_fall = 4.5

    def __init__(self, name, fuel, fanciness=0.0):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = super().price_per_km * self.fanciness

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flag_fall

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flag_fall}"
