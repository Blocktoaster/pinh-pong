from pygame import*
from random import*


window = display.set_mode((700,500))
clock = time.Clock()
display.set_caption("Ping Ping")
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,66))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class GameSprite2(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,150))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

    def upravlenie(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN]:
            self.rect.y += 10
        if keys_pressed[K_UP]:
            self.rect.y -= 10

ball =GameSprite('ball1.png', 350,250)
palka = GameSprite2('palka.png',650,200)      

dx = randint(-5,5)
dy = randint(-5,5)

if dx == 0:
    dx = 4

if dy == 0:
    dy = 4
game=True
while game:
    window.fill((241,156,187))
    ball.rect.x +=dx
    ball.rect.y -=dy
    if ball.rect.x > 650:
        dx *= -1
    if ball.rect.y < 0:
        dy *= -1
    if ball.rect.x < 0:
        dx *= -1
    if ball.rect.y > 455:
        dy *= -1
    if sprite.collide_rect(ball,palka):
        dx *= -1
    for e in event.get():
        if e.type == QUIT:
            game = False
    ball.reset()
    palka.reset()
    palka.upravlenie()
    display.update()
    clock.tick(60)              
