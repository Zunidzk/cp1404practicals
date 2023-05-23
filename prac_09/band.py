from prac_09.guitar import Guitar


class Band:
    def __init__(self, name=str):
        self.name = name
        self.musicians = []

    def __str__(self):
        return f"{self.name} {self.musicians}"

    def __repr__(self):
        return str(vars(self))

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        for musician in self.musicians:
            print(musician.play())
