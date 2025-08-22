import pygame
pygame.init()

BACKGROUND = (245, 145, 45)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
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

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill(BACKGROUND)
    for card in cards:
        card.draw_all(window, pygame.draw.rect, RED, 10, 19, 55)

    pygame.display.update()
    clock.tick(40)
