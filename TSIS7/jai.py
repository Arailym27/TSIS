import pygame
import sys

# Инициализация Pygame
pygame.init()

# Создание окна
screen = pygame.display.set_mode((400, 300))

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Начальные координаты персонажа
x = 30
y = 30

# Главный игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Очистка экрана
    screen.fill(WHITE)

    # Рисуем персонажа (прямоугольник)
    pygame.draw.rect(screen, BLUE, pygame.Rect(x, y, 20, 20))

    # Обновляем экран
    pygame.display.flip()

    # Перемещение персонажа
    x += 1
    y += 1

    # Задержка для анимации
    pygame.time.delay(50)