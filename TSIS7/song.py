import pygame
import os

pygame.init()
pygame.mixer.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((512, 512))
pygame.display.set_caption("Простой музыкальный плеер")
clock = pygame.time.Clock()

index = 0
playlist = []

# Путь к папке с музыкальными файлами
directory_path = "/Users/arajlymkabykenova/Desktop/PP2/songs"

# Проверяем, существует ли указанная директория
if not os.path.isdir(directory_path):
    print("Указанной директории не существует.")
else:
    # Получаем список файлов в указанной директории
    files = os.listdir(directory_path)
    
    # Отбираем только файлы с расширением mp3
    playlist = [os.path.join(directory_path, file) for file in files if file.endswith('.mp3')]
    
    if not playlist:
        print("В указанной директории нет музыкальных файлов.")
    else:
        pygame.mixer.music.load(playlist[index])
        pygame.mixer.music.play()

# Загрузка изображений кнопок с использованием метода transform.scale()
play_image = pygame.transform.scale(pygame.image.load("play.png"), (40, 40))
pause_image = pygame.transform.scale(pygame.image.load("pause.png"), (40, 40))
prev_track_image = pygame.transform.scale(pygame.image.load("prev_track.png"), (40, 40))
next_track_image = pygame.transform.scale(pygame.image.load("next_track.png"), (40, 40))

# Определение размеров и координат кнопок
BUTTON_SIZE = 40
BUTTON_MARGIN = 20

# Вычисляем координаты кнопок для размещения их в центре экрана
screen_center_x = screen.get_width() // 2
screen_center_y = screen.get_height() // 2

play_pause_button_rect = play_image.get_rect(center=(screen_center_x, screen_center_y))
prev_track_button_rect = prev_track_image.get_rect(center=(screen_center_x - 100, screen_center_y))
next_track_button_rect = next_track_image.get_rect(center=(screen_center_x + 100, screen_center_y))

run = True
paused = False

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # Проверяем, было ли нажатие на кнопку "Старт/Пауза"
            if play_pause_button_rect.collidepoint(mouse_pos):
                if paused:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
                paused = not paused
            # Проверяем, было ли нажатие на кнопку "Предыдущий трек"
            elif prev_track_button_rect.collidepoint(mouse_pos):
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
            # Проверяем, было ли нажатие на кнопку "Следующий трек"
            elif next_track_button_rect.collidepoint(mouse_pos):
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

    screen.fill(WHITE)

    # Отрисовка кнопок
    screen.blit(play_image if not paused else pause_image, play_pause_button_rect)
    screen.blit(prev_track_image, prev_track_button_rect)
    screen.blit(next_track_image, next_track_button_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
