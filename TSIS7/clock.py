import pygame 
import datetime 
 
pygame.init() 
 
# Surface parameters 
WIDTH, HEIGHT = 1200, 950 
 
# Create surface 
surface = pygame.display.set_mode((WIDTH, HEIGHT)) 
 
# Create name of program 
name = pygame.display.set_caption("Mickey Mouse Clock") 
 
# Clock Mickey Mouse icon for app 
icon = pygame.display.set_icon(pygame.image.load('icon.jpeg'))
 
# Load image Mickey Mouse clock 
foto = pygame.image.load('mickey-clock.png')
foto = pygame.transform.scale(foto, (WIDTH, HEIGHT))
 
# Load right and left arm 
right_a = pygame.image.load('right_hand.png') 
left_a = pygame.image.load('left_hand.png') 
# Scale the arms if needed
right_a = pygame.transform.scale(right_a, (1400, 980))
left_a = pygame.transform.scale(left_a, (63, 920))
width = left_a.get_width()
height = left_a.get_height()
# Important parameters of this code 
run = True 
FPS = 60 
tickrate = pygame.time.Clock() 
print(width,height)
# Find center of foto 
center_w = WIDTH // 2 
center_h = HEIGHT // 2 
 
def rotate_image(image, angle): 
    """Rotate an image.""" 
    return pygame.transform.rotate(image, angle) 
 
while run: 
    # Get current time 
    time_now = datetime.datetime.now() 
    minutes = time_now.minute 
    seconds = time_now.second 
     
    # Calculate angles for arms 
    # 1 circle 360 degree in 1 minute = 60 seconds. This mean 1 second 6 degree 
    # Rotate the left hand (minute hand)
    # We add an offset to adjust for any discrepancies in the image
    minute_angle = (minutes + 0.75) * 6  # 6 degrees per minute, with 9 minutes added 
    
    # Rotate the right hand (second hand)
    second_angle = (seconds + 6) * 6  # 6 degrees per second 
     
    # Rotate arms ("-" mean go clockwise) 
    rotated_right_a = rotate_image(right_a, -second_angle) 
    rotated_left_a = rotate_image(left_a, -minute_angle) 
 
    # Draw on screen Mickey mouse clock 
    surface.blit(foto, (0, 0)) 
 
    # Draw rotated arms 
    # Calculate the positions of the hands based on the center of the clock image
    right_hand_pos = (center_w - rotated_right_a.get_width() // 2, center_h - rotated_right_a.get_height() // 2)
    left_hand_pos = (center_w - rotated_left_a.get_width() // 2, center_h - rotated_left_a.get_height() // 2)
    
    # Draw the rotated hands onto the surface
    surface.blit(rotated_right_a, right_hand_pos)
    surface.blit(rotated_left_a, left_hand_pos)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False 
 
    pygame.display.update() 
    tickrate.tick(FPS) 
 
pygame.quit()
