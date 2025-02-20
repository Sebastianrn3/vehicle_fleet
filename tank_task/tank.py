from random import randint

class Battlefield:
    def __init__(self,
                 length: int = 9,
                 width: int = 9,
    ):
        self.length = length
        self.width = width
        self.tank = Tank(self.length, self.width)
        self.target = Target(self.length, self.width)
        self.generate_field()

    def generate_field(self):
        print("Score:000")
        for x in range(self.length):
            row = ""
            for y in range(self.width):
                if self.tank.position[0] == x and self.tank.position[1] == y:
                    row += f"{self.tank.direction} "
                elif x == self.target.position[0] and y== self.target.position[1]:
                    row += "⟡ "
                else:
                    row += "⬚ "
            print(row)

class Tank:
    def __init__(self, length, width):
        self.directions = ("⇑", "⇒", "⇓", "⇐")
        self.position = [int(length/2), int(width/2)]
        self.direction = self.directions[0]

    def create_tank(self):
        pass

    def info(self):
        pass
        # į kurią kryptį tankas šiuo metu yra pasisukęs,
        # kokios yra jo koordinatės,
        # kiek iš viso atliko šūvių
        # kiek atliko šūvių į kiekvieną kryptį atskirai.

class Target:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.position = self.generate_target()

    def generate_target(self):
        return randint(0, self.length - 1), randint(0, self.width - 1)

game = Battlefield()

while True:
    value = input("There you go:")
    game.tank.direction = value
    game.generate_field()


# {self.tank.direction}

# print("⇐	⇑	⇒	⇓")
# print("←	↑	→	↓⬚⬚⬚⬚⬚⬚")
# print("✹ ▒ ▓ ⟡ ◇ ⬚ ▢ ⿴ ⿶ ◫ ▩ ⌕")