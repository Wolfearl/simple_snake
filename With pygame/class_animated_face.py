from pygame.sprite import Sprite
from pygame.transform import rotate

class AnimatedSprite(Sprite):
    def __init__(self, images, speed, frame_rate=10):
        super().__init__()
        self.images = images
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.speed = speed
        self.frame_rate = frame_rate

    def update(self, check):
        self.index += 1
        if self.index >= len(self.images) * self.frame_rate:
            self.index = 0

        index = self.index // self.frame_rate
        self.image = self.images[index]

        match check:
            case "RIGHT":
                self.image = rotate(self.image,-90)
            case "LEFT":
                self.image = rotate(self.image, 90)
            case "DOWN":
                self.image = rotate(self.image, 180)
