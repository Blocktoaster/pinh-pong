from pygame import*
from random import*

window = display.set_mode((700,500))

display.set_caption("Ping Ping")
ball = background = transform.scale(image.load("Trup.jpg"),(100,100))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,66))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
