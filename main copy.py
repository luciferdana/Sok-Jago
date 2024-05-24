from pickle import FALSE
import pygame
from fighter import Fighter
from pygame import mixer

try:
    pygame.init()
    mixer.init()
except pygame.error as e:
    print("Error initializing pygame: ", e)
    exit()

# Set screen dimensions
Screen_Width = 1000
Screen_Height = 600

# Create the screen
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("Sok Jago")

# Set framerate
clock = pygame.time.Clock()
FPS = 60

# Define colors
Yellow = (255, 255, 0)
Red = (255, 0, 0)
White = (255, 255, 255)

# Define game variables
MENU = True
PLAYER1_CHARACTER_MENU = True
PLAYER2_CHARACTER_MENU = True
BACKGROUND_MENU = False
PAUSE_MENU = False
END_MENU = False

# Define game variables
intro = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]
round_over = False
round_over_cooldown = 2000

# Define player variables
pemain1_size = 128
pemain1_scale = 1.75
pemain1_offset = [25, 40]
pemain1_data = [pemain1_size, pemain1_scale, pemain1_offset]

pemain2_size = 128
pemain2_scale = 1.75
pemain2_offset = [25, 40]
pemain2_data = [pemain2_size, pemain2_scale, pemain2_offset]


# Load music and sound effects
pygame.mixer.music.load('assets/audio/music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)

ica_fx = pygame.mixer.Sound('assets/audio/ica_fx.mp3')
agus_fx = pygame.mixer.Sound('assets/audio/agus_fx.mp3')
samson_fx = pygame.mixer.Sound('assets/audio/samson_fx.mp3')
ica_fx.set_volume(0.5)
agus_fx.set_volume(0.5)
samson_fx.set_volume(0.5)

# Load images
bg_image = pygame.image.load("assets/images/background/background.png").convert_alpha()
choose_bg = pygame.image.load("assets/images/background/choose_player_bg.png").convert_alpha()
arena1 = pygame.image.load("assets/images/background/arena1.png").convert_alpha()
arena2 = pygame.image.load("assets/images/background/arena2.png").convert_alpha()
arena_bg = pygame.image.load("assets/images/background/arena_bg.png").convert_alpha()
menu_bg = pygame.image.load("assets/images/background/menu_bg.png").convert_alpha()
option_bg = pygame.image.load("assets/images/background/option_bg.png").convert_alpha()

#ukuran gambar
menu_bg = pygame.transform.scale(menu_bg, (1000, 600))
arena1 = pygame.transform.scale(arena1, (1000, 600))
arena2 = pygame.transform.scale(arena2, (1000, 600))

# Load victory image
victory_img = pygame.image.load('assets/images/icons/victory.png').convert_alpha()

# Load spritesheets for animation
agus_sheet = pygame.image.load('assets/images/character/agus.png')
samson_sheet = pygame.image.load('assets/images/character/samson.png')
ica_sheet = pygame.image.load('assets/images/character/ica.png')

# Define animation steps
agus_animation_steps = [6, 8, 10, 4, 3, 3, 3]
samson_animation_steps = [6, 8, 12, 5, 3, 2, 4]
ica_animation_steps = [6, 8, 12, 6 , 4, 2 ,3]

# Load fonts
count_font = pygame.font.Font('assets/fonts/Act_Of_Rejection.ttf', 100)
score_font = pygame.font.Font('assets/fonts/AAbsoluteEmpire-EaXpg.ttf', 30)
victory_font = pygame.font.Font('assets/fonts/AAbsoluteEmpire-EaXpg.ttf', 100)
ronde_font = pygame.font.Font('assets/fonts/AAbsoluteEmpire-EaXpg.ttf', 80)
reset_font = pygame.font.Font('assets/fonts/AAbsoluteEmpire-EaXpg.ttf', 30)
menu_font = pygame.font.Font('assets/fonts/AAbsoluteEmpire-EaXpg.ttf', 30)
smaller_menu_font = pygame.font.Font('assets/fonts/AAbsoluteEmpire-EaXpg.ttf', 27)


def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (Screen_Width, Screen_Height))
    screen.blit(scaled_bg, (0, 0))

def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, White, (x - 2, y - 2, 405, 34))
    pygame.draw.rect(screen, Red, (x, y, 400, 30))
    pygame.draw.rect(screen, Yellow, (x, y, 400 * ratio, 30))

agus = Fighter(1, 200, 390, pemain1_data, agus_sheet, agus_animation_steps, False, agus_fx)
samson = Fighter(2, 700, 390, pemain2_data, samson_sheet, samson_animation_steps, True, samson_fx)
ica = Fighter(2, 700, 390, pemain2_data, ica_sheet, ica_animation_steps, True, ica_fx)

run = True
while run:
    clock.tick(FPS)

    for menu in ['MENU', 'PLAYER1', 'PLAYER2', 'ARENA', 'GAMEPLAY']:
        print(menu)
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()

    if key[pygame.K_ESCAPE]:
        PAUSE_MENU = True

    pygame.display.flip()

pygame.quit()