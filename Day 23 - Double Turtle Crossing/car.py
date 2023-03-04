from turtle import Turtle
from random import choice, randint

X_STARTING_POSITION = 595


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color(self.random_color())
        # Make car shaped
        self.shape("square")
        self.shapesize(1, 2)
        # Random Offset is used for intrucing randomness when respawing cars.
        self.random_offset = choice(list(range(30, 60)))
        # Set heading
        self.car_heading = self.random_heading()
        self.setheading(self.car_heading)
        # Disperse the cars across the screen
        random_x = randint(0, X_STARTING_POSITION) * choice([-1,1])
        self.goto(random_x, self.random_starting_position()[1])

    def travel(self):
        self.forward(3)

    def random_color(self):
        return choice(["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"])

    def random_starting_position(self):
        y = randint(-230,240)
        if self.heading() == 0:
            x = -1 * X_STARTING_POSITION
        else:
            x = X_STARTING_POSITION

        return (x,y)

    def random_heading(self):
        return choice([0,180])
