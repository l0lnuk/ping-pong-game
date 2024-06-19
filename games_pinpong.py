import pygame
from pygame import *
import pygame_menu
pygame.init()
width = 600
height = 500
window = display.set_mode((width, height))
display.set_caption('Ping Pong games')
back = (222, 175, 111)
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self, image_file, x, y, speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(
            image.load(image_file), (size_x, size_y)
        )
        self.speed = speed
        self.rect = (
            self.image.get_rect()
        )
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < height - 150:
            self.rect.y += self.speed


    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < height - 150:
            self.rect.y += self.speed

clock = time.Clock()
FPS = 60
p1=0
p2=0
font.init()
font1 = font.SysFont(None, 36)
rackets1 = Player('racket.png', 30, 200, 6, 50, 150)
rackets2 = Player('racket.png', 520, 200, 6, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)


def main():
    rackets1 = Player('racket.png', 30, 200, 6, 50, 150)
    rackets2 = Player('racket.png', 520, 200, 6, 50, 150)
    ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

    ball_x = 4
    ball_y = 4
    global p1,p2
    while True:
        p1_text_1=font1.render(f'Счёт:{p1}',True,(0,0,0))
        p2_text_1=font1.render(f'Счёт:{p2}',True,(0,0,0))
        for e in event.get():
            if e.type == QUIT:
                return


        window.fill(back)
        rackets1.update_l()
        rackets2.update_r()
        ball.rect.x += ball_x
        ball.rect.y += ball_y

        if sprite.collide_rect(rackets1, ball):
            ball_x *= -1
        if sprite.collide_rect(rackets2, ball):
            ball_x *= -1
        if ball.rect.y < 0 or ball.rect.y > height - 50:
            ball_y *= -1
        if ball.rect.x < 0:
            p2+=1
            show_end_screen()
        if ball.rect.x > width - 1:
            p1+=1
            show_end_screen()


        rackets1.reset()
        rackets2.reset()
        ball.reset()
        window.blit(p1_text_1,(10,10))
        window.blit(p2_text_1,(500,10))
        display.update()
        clock.tick(FPS)

def restart():
    global p1,p2
    p1,p2=0,0
    main()

def show_start_screen():
    start_menu=pygame_menu.Menu('Ping Pong', 300,400,theme=pygame_menu.themes.THEME_ORANGE)
    start_menu.add.button('Начать',main)
    start_menu.add.button('Выйти',pygame_menu.events.EXIT)
    start_menu.mainloop(window)

def show_end_screen():
    start_menu=pygame_menu.Menu('конец', 300,400,theme=pygame_menu.themes.THEME_ORANGE)
    start_menu.add.button('Заново',restart)
    start_menu.add.button('Реванш',main)
    start_menu.add.button('Выйти',pygame_menu.events.EXIT)
    start_menu.mainloop(window)

if __name__=='__main__':
    show_start_screen()
