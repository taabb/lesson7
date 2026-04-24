import pygame

pygame.init()


W, H = 800, 600
display = pygame.display.set_mode( (W, H) )


class Crosshair:
    def __init__(self):
        self.image = pygame.image.load("res/crosshair_small.png")
        self.rect = self.image.get_rect()

    def move(self):
        mouse_pos = where_mouse_pressed(0)
        if mouse_pos:
            self.rect.center = mouse_pos

    def draw(self):
        display.blit(self.image, self.rect)


class Target:
    def __init__(self):
        self.image = pygame.image.load("res/target_small.png")
        self.rect = self.image.get_rect()

    def move(self):
        if is_key_pressed(pygame.K_d):
            self.rect.x += 10

        if is_key_pressed(pygame.K_a):
            self.rect.x -= 10

        if is_key_pressed(pygame.K_w):
            self.rect.y -= 10

        if is_key_pressed(pygame.K_s):
            self.rect.y += 10

    def draw(self):
        display.blit(self.image, self.rect)


def is_key_pressed(key):
    return pygame.key.get_pressed()[key]

def where_mouse_pressed(mouse_key):
    if pygame.mouse.get_pressed(num_buttons=5)[mouse_key]:
        return pygame.mouse.get_pos()


crosshair = Crosshair()
target = Target()


def main():
    while True:
        # 1 Считывание ввода
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return

        # 2 Обновление игровых объектов
        target.move()
        crosshair.move()

        # 3 Отрисовка обновленного состояния
        display.fill("white")
        target.draw()
        crosshair.draw()
        pygame.display.update()
        pygame.time.delay(50)


main()

