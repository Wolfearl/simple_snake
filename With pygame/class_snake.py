import random
from random import randrange


class Snake:
    def __init__(self, width, height):
        self.body = None
        self.direction = None
        self.WIDTH = width
        self.HEIGHT = height
        self.reset()

    def reset(self):
        self.direction = random.choice(["RIGHT", "LEFT", "UP", "DOWN"])
        match self.direction:
            case "RIGHT":
                x = randrange(10, self.WIDTH - 30, 10)
                y = randrange(10, self.HEIGHT - 10, 10)
                self.body = [(x, y), (x-10, y), (x-20, y)]
            case "LEFT":
                x = randrange(40, self.WIDTH - 10, 10)
                y = randrange(10, self.HEIGHT - 10, 10)
                self.body = [(x, y), (x + 10, y), (x + 20, y)]
            case "UP":
                x = randrange(10, self.WIDTH - 10, 10)
                y = randrange(30, self.HEIGHT - 10, 10)
                self.body = [(x, y), (x, y + 10), (x, y + 20)]
            case "DOWN":
                x = randrange(10, self.WIDTH - 10, 10)
                y = randrange(10, self.HEIGHT - 30, 10)
                self.body = [(x, y), (x, y - 10), (x, y - 20)]

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == "RIGHT":
            head_x += 10
        elif self.direction == "LEFT":
            head_x -= 10
        elif self.direction == "UP":
            head_y -= 10
        elif self.direction == "DOWN":
            head_y += 10
        self.body.insert(0, (head_x, head_y))
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def check_for_boundaries(self):
        head_x, head_y = self.body[0]
        if head_x < 0 or head_x >= self.WIDTH or head_y < 0 or head_y >= self.HEIGHT:
            return True
        if self.body[0] in self.body[1:]:
            return True
        return False