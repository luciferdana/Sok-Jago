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
pemain1_size = 162
pemain1_scale = 4
pemain1_offset = [72, 56]
pemain1_data = [pemain1_size, pemain1_scale, pemain1_offset]

pemain2_size = 250
pemain2_scale = 3
pemain2_offset = [112, 107]
pemain2_data = [pemain2_size, pemain2_scale, pemain2_offset]

# Load music and sound effects
pygame.mixer.music.load('assets/audio/music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)

warrior_fx = pygame.mixer.Sound('assets/audio/sword.wav')
wizard_fx = pygame.mixer.Sound('assets/audio/magic.wav')
warrior_fx.set_volume(0.4)
wizard_fx.set_volume(0.5)

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
pemain1_sheet = pygame.image.load('assets/images/pemain1/warrior.png')
pemain2_sheet = pygame.image.load('assets/images/pemain2/wizard.png')

# Define animation steps
pemain1_animation_steps = [10, 8, 1, 7, 7, 3, 7]
pemain2_animation_steps = [8, 8, 1, 8, 8, 3, 7]

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

pemain1 = Fighter(1, 200, 390, pemain1_data, pemain1_sheet, pemain1_animation_steps, False, warrior_fx)
pemain2 = Fighter(2, 700, 390, pemain2_data, pemain2_sheet, pemain2_animation_steps, True, wizard_fx)

run = True
while run:
    clock.tick(FPS)
    
    if MENU:
        screen.blit(menu_bg, (0, 0))
        draw_text("Press Enter to Start", smaller_menu_font, (0, 0, 0), 320, 385)
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            BACKGROUND_MENU = True
            MENU = False
            PAUSE_MENU = False
        if END_MENU:
            if key[pygame.K_RETURN]:
                run = False

    elif PLAYER1_CHARACTER_MENU:
        screen.blit(choose_bg, (0, 0))
        draw_text("Player 1: Choose Your Character", menu_font, Red, 200, 200)

        key = pygame.key.get_pressed()
        if key[pygame.K_1]:
            pemain1 = Fighter(1, 200, 390, pemain1_data, pemain1_sheet, pemain1_animation_steps, False, warrior_fx)
            PLAYER1_CHARACTER_MENU = False
            PLAYER2_CHARACTER_MENU = True

        elif key[pygame.K_2]:
            pemain1 = Fighter(1, 200, 390, pemain1_data, pemain1_sheet, pemain1_animation_steps, False, wizard_fx)
            PLAYER1_CHARACTER_MENU = False
            PLAYER2_CHARACTER_MENU = True

    elif PLAYER2_CHARACTER_MENU:
        screen.blit(choose_bg, (0, 0))
        draw_text("Player 2: Choose Your Character", menu_font, Red, 200, 200)

        key = pygame.key.get_pressed()
        if key[pygame.K_1]:
            pemain2 = Fighter(2, 700, 390, pemain2_data, pemain2_sheet, pemain2_animation_steps, True, warrior_fx)
            PLAYER2_CHARACTER_MENU = False
            BACKGROUND_MENU = True

        elif key[pygame.K_2]:
            pemain2 = Fighter(2, 700, 390, pemain2_data, pemain2_sheet, pemain2_animation_steps, True, wizard_fx)
            PLAYER2_CHARACTER_MENU = False
            BACKGROUND_MENU = True

    elif BACKGROUND_MENU:
        screen.blit(arena_bg, (0, 0)) 
        key = pygame.key.get_pressed()
        if key[pygame.K_1]:
            current_background = arena1
            BACKGROUND_MENU = False
            MENU = False
        elif key[pygame.K_2]:  # Gunakan elif agar hanya satu kondisi yang dievaluasi
            current_background = arena2
            BACKGROUND_MENU = False
            MENU = False

    elif PAUSE_MENU:
        screen.blit(option_bg, (0, 0))
        draw_text("Press Enter to Resume", menu_font, Red, 300, 300)
        draw_text("Press Space to Quit", menu_font, Red, 320, 350)
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            PAUSE_MENU = False
        if key[pygame.K_SPACE]:
            pygame.quit()


    else:        
        screen.blit(current_background, (0, 0))

        pemain1.update()
        pemain2.update()

        pemain2.draw(screen)
        pemain1.draw(screen)

        #
        draw_health_bar(pemain1.health, 20, 20)
        draw_health_bar(pemain2.health, 580, 20)
        draw_text("P1: " + str(score[0]), score_font, Red, 20, 60)
        draw_text("P2: " + str(score[1]), score_font, Red, 580, 60)

        # Inisialisasi variabel game_over sebelum loop game
        game_over = False

        #
        if intro <= 0 and not game_over:
            pemain1.move(Screen_Width, Screen_Height, screen, pemain2, round_over)
            pemain2.move(Screen_Width, Screen_Height, screen, pemain1, round_over)
        else:
            if not game_over:  # Hanya jika permainan belum berakhir
                draw_text(str(intro), count_font, Red, (Screen_Width / 2) - 40, (Screen_Height / 3) - 50)
                if pygame.time.get_ticks() - last_count_update >= 1000:
                    intro -= 1
                    last_count_update = pygame.time.get_ticks()



        #
        pemain1.update()
        pemain2.update()

        pemain1.draw(screen)
        pemain2.draw(screen)

        #
        if round_over == False:
            if pemain1.alive == False:
                score[1] += 1
                round_over = True
                round_over_time = pygame.time.get_ticks()
            elif pemain2.alive == False:
                score[0] += 1
                round_over = True
                round_over_time = pygame.time.get_ticks()
        else:
            if score[0] < 3 and score[1] < 3:
                draw_text('Ronde Selesai', ronde_font, Red, 175, 230)
            if pygame.time.get_ticks() - round_over_time > round_over_cooldown:
                round_over = False
                pemain1 = Fighter(1, 200, 390, pemain1_data, pemain1_sheet, pemain1_animation_steps, False, warrior_fx)
                pemain2 = Fighter(2, 700, 390, pemain2_data, pemain2_sheet, pemain2_animation_steps, True, wizard_fx)
  
        if score[0] >= 3 or score[1] >= 3:
            draw_text('VICTORY', victory_font, Red, 250, 170)
            draw_text('Tekan "R" untuk bermain kembali', reset_font, Red, 200, 120)
            game_over = True  # Menandakan bahwa permainan telah berakhir

      # Ketika permainan selesai dan pemain memilih untuk memulai kembali
        if game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                # Atur ulang kondisi permainan
                score = [0, 0]
                game_over = False
                last_count_update = pygame.time.get_ticks()  # Atur ulang waktu intro terakhir   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()

    if key[pygame.K_ESCAPE]:
        PAUSE_MENU = True

    pygame.display.flip()

pygame.quit()