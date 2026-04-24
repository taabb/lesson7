import pygame

pygame.init()


W, H = 800, 600
display = pygame.display.set_mode( (W, H) )

# image = pygame.image.load("res/crosshair_small.png")
# rect = image.get_rect()

image2 = pygame.image.load("res/target_small.png")
rect2 = image2.get_rect()


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





def is_key_pressed(key):
    return pygame.key.get_pressed()[key]

def where_mouse_pressed(mouse_key):
    if pygame.mouse.get_pressed(num_buttons=5)[mouse_key]:
        return pygame.mouse.get_pos()


crosshair = Crosshair()


def main():
    while True:
        # 1 Считывание ввода
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return

        # 2 Обновление игровых объектов
        if is_key_pressed(pygame.K_d):
            rect2.x += 10
            print(rect2.right)

        if is_key_pressed(pygame.K_a):
            rect2.x -= 10

        if is_key_pressed(pygame.K_w):
            rect2.y -= 10

        if is_key_pressed(pygame.K_s):
            rect2.y += 10

        crosshair.move()
        # mouse_pos = where_mouse_pressed(0)
        # if mouse_pos:
        #     rect.center = mouse_pos

        # 3 Отрисовка обновленного состояния
        display.fill("white")
        display.blit(image2, rect2)
        # display.blit(image, rect)
        crosshair.draw()
        pygame.display.update()
        pygame.time.delay(50)


main()

