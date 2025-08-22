import pygame
pygame.init()

BACKGROUND = (245, 145, 45)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)


class Area:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def fill(self):
        return self.fill_color, self.rect

    def outline(self, frame_color, thickness):
        return frame_color, self.rect, thickness


window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()


cards = []
x = 70
for card in range(4):
    new_card = Area(x, 170, 70, 100, YELLOW)
    x += 100
    cards.append(new_card)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill(BACKGROUND)
    for card in cards:
        pygame.draw.rect(window, *card.fill())
        pygame.draw.rect(window, *card.outline(RED, 10))

    pygame.display.update()
    clock.tick(40)
