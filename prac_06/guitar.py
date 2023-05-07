class Guitar:
    """guitar class object"""

    def __init__(self, year=0, cost=0, name=""):
        """guitar class"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """guitar detail"""
        return f"{self.name} ({self.year}) : ${self.cost:}"

    def get_age(self):
        """guitar year"""
        return 2023 - self.year

    def is_vintage(self):
        """is guitar vintage or not"""
        return self.get_age() >= 50
