import pygame
from random import randint
pygame.init()

BACKGROUND = (245, 145, 45)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


class Area:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def fill(self):
        return self.fill_color, self.rect

    def outline(self, frame_color, thickness):
        return frame_color, self.rect, thickness


class Label(Area):
    def set_text(self, text, fsize, color):
        self.image = pygame.font.SysFont("Comic Sans", fsize).render(text, True, color)

    def draw_without_text(self, window, rect_func, frame_color, thickness):
        rect_func(window, *self.fill())
        rect_func(window, *self.outline(frame_color, thickness))

    def draw_all(self, window, rect_func, frame_color, thickness, shift_x, shift_y):
        rect_func(window, *self.fill())
        rect_func(window, *self.outline(frame_color, thickness))
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()


cards = []
x = 36
for card in range(4):
    new_card = Label(x, 170, 95, 150, YELLOW)
    x += 110
    new_card.set_text("Click", 26, BLACK)
    cards.append(new_card)

run = True
wait = 0

while run:
    if wait == 0:
        wait = 20
        num = randint(0, 3)
    wait -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for index, card in enumerate(cards):
                if card.rect.collidepoint(x, y):
                    if index == num:
                        card.fill_color = GREEN
                    else:
                        card.fill_color = RED
                else:
                    card.fill_color = YELLOW


    window.fill(BACKGROUND)

    for index, card in enumerate(cards):
        if index == num:
            card.draw_all(window, pygame.draw.rect, RED, 10, 19, 55)
        else:
            card.draw_without_text(window, pygame.draw.rect, RED, 10)

    pygame.display.update()
    clock.tick(40)
