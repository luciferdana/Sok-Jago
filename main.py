from pickle import FALSE, TRUE
import pygame
import fighter
from pygame import mixer
import health_bar
import sliders

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
Black = (0, 0, 0)
Yellow = (255, 255, 0)
Red = (255, 0, 0)
White = (255, 255, 255)

# Define game variables
MENU = True
PLAYER_CHARACTER_MENU = False
PLAYER1_NAME = ""
PLAYER2_NAME = ""
VICTORY = ""
PLAYER1_SELECTED = False
BACKGROUND_MENU = False
PAUSE_MENU = False
GAME_GUIDE = False
END_MENU = False

# Define game variables
intro = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]
round_over = False
round_over_cooldown = 2000

# Membuat variabel pemain
pemain1_size = 128
pemain1_scale = 1.75
pemain1_offset = [25, 40]
pemain1_data = [pemain1_size, pemain1_scale, pemain1_offset]

pemain2_size = 128
pemain2_scale = 1.75
pemain2_offset = [25, 40]
pemain2_data = [pemain2_size, pemain2_scale, pemain2_offset]

#Membuat atribut unik setiap karakter
#setiap atribut disusun dengan urutan: speed, cooldown, damage, health
atr_agus = [10, 20, 10, 100]
atr_samson = [7, 25, 8, 140]
atr_ica = [15, 15, 15, 70]

# Load music and sound effects
pygame.mixer.music.load('assets/audio/music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 6000)

ica_fx = pygame.mixer.Sound('assets/audio/ica_fx.mp3')
agus_fx = pygame.mixer.Sound('assets/audio/agus_fx.mp3')
samson_fx = pygame.mixer.Sound('assets/audio/samson_fx.mp3')
ica_fx.set_volume(0.5)
agus_fx.set_volume(0.5)
samson_fx.set_volume(0.5)

# Load gambar gambar
bg_image = pygame.image.load("assets/images/background/background.png").convert_alpha()
choose1_bg = pygame.image.load("assets/images/background/choose1.png").convert_alpha()
choose2_bg = pygame.image.load("assets/images/background/choose2.png").convert_alpha()
arena1 = pygame.image.load("assets/images/background/arena1.png").convert_alpha()
arena2 = pygame.image.load("assets/images/background/arena2.png").convert_alpha()
arena_bg = pygame.image.load("assets/images/background/arena_bg.png").convert_alpha()
menu_bg = pygame.image.load("assets/images/background/menu_bg.png").convert_alpha()
option_bg = pygame.image.load("assets/images/background/option_bg.png").convert_alpha()
guide_bg = pygame.image.load("assets/images/background/guide_bg.png").convert_alpha()

#ukuran gambar
menu_bg = pygame.transform.scale(menu_bg, (1000, 600))
arena1 = pygame.transform.scale(arena1, (1000, 600))
arena2 = pygame.transform.scale(arena2, (1000, 600))
choose1_bg = pygame.transform.scale(choose1_bg, (1000, 600))
choose2_bg = pygame.transform.scale(choose2_bg, (1000, 600))
arena_bg=pygame.transform.scale(arena_bg ,(1000,600))
option_bg=pygame.transform.scale(option_bg, (1000, 600))
guide_bg=pygame.transform.scale(guide_bg,(1000, 600))

#membuat sliders untuk volume
bg_slider = sliders.Slider(x=250, y=440, length=200, height=10, knob_radius=10)
fx_slider = sliders.Slider(x= 600, y= 440, length= 200, height= 10, knob_radius=10)

# Load spritesheets untuk animation
agus_sheet = pygame.image.load('assets/images/character/agus.png')
samson_sheet = pygame.image.load('assets/images/character/samson.png')
ica_sheet = pygame.image.load('assets/images/character/ica.png')

# Define animation steps (berapa frame-nya)
agus_animation_steps = [6, 8, 10, 4, 3, 3, 3]
samson_animation_steps = [6, 8, 12, 5, 3, 2, 4]
ica_animation_steps = [6, 8, 12, 6 , 4, 2 ,3]

# Load fonts
count_font = pygame.font.Font('assets/fonts/Act_Of_Rejection.ttf', 100)
score_font = pygame.font.Font('assets/fonts/Akira Expanded Demo.otf', 30)
victory_font = pygame.font.Font('assets/fonts/Akira Expanded Demo.otf', 80)
ronde_font = pygame.font.Font('assets/fonts/Akira Expanded Demo.otf', 60)
reset_font = pygame.font.Font('assets/fonts/Akira Expanded Demo.otf', 27)
menu_font = pygame.font.Font('assets/fonts/Akira Expanded Demo.otf', 30)
smaller_menu_font = pygame.font.Font('assets/fonts/Akira Expanded Demo.otf', 20)

#Fungsi untuk membuat teks lebih mudah
def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# Fungsi untuk menggambar teks dengan outline
def draw_text_with_outline(text, font, text_color, outline_color, x, y):
    # Render teks dengan warna outline
    text_surface = font.render(text, True, outline_color)
    # Render teks dengan warna asli
    text_surface_base = font.render(text, True, text_color)

    # Gambar teks outline sedikit bergeser ke 8 arah untuk membuat outline
    screen.blit(text_surface, (x - 2, y - 2))
    screen.blit(text_surface, (x + 2, y - 2))
    screen.blit(text_surface, (x - 2, y + 2))
    screen.blit(text_surface, (x + 2, y + 2))
    screen.blit(text_surface, (x - 2, y))
    screen.blit(text_surface, (x + 2, y))
    screen.blit(text_surface, (x, y - 2))
    screen.blit(text_surface, (x, y + 2))

    # Gambar teks asli di atas outline
    screen.blit(text_surface_base, (x, y))

#Fungsi untuk menampilkan background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (Screen_Width, Screen_Height))
    screen.blit(scaled_bg, (0, 0))

run = True
while run:
    clock.tick(FPS)
    
    if MENU:
        screen.blit(menu_bg, (0, 0))
        draw_text("Press Enter to Start", smaller_menu_font, (0, 0, 0), 320, 388)
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            MENU = False
            PAUSE_MENU = False
            PLAYER_CHARACTER_MENU = True
        if END_MENU:
            if key[pygame.K_RETURN]:
                run = False

    elif PLAYER_CHARACTER_MENU:
        if not PLAYER1_SELECTED:
            screen.blit(choose1_bg, (0, 0))

            key = pygame.key.get_pressed()
            
            if key[pygame.K_1]:
                pemain1 = fighter.Fighter(1, 200, 390, pemain1_data, samson_sheet, samson_animation_steps, False, samson_fx, atr_samson)
                pemain1_bantuan = [samson_sheet, samson_animation_steps, samson_fx]
                pemain1_health_bar = health_bar.HealthBarSamson(pemain1.health)
                PLAYER1_SELECTED = True
                PLAYER1_NAME = "Samson"

            elif key[pygame.K_2]:
                pemain1 = fighter.Fighter(1, 200, 390, pemain1_data, ica_sheet, ica_animation_steps,False, ica_fx, atr_ica)
                pemain1_bantuan = [ica_sheet, ica_animation_steps, ica_fx]
                pemain1_health_bar = health_bar.HealthBarIca(pemain1.health)
                PLAYER1_SELECTED = True
                PLAYER1_NAME = "Ica"
                
            elif key[pygame.K_3]:
                pemain1 = fighter.Fighter(1, 200, 390, pemain1_data, agus_sheet, agus_animation_steps, False, agus_fx, atr_agus)
                pemain1_bantuan = [agus_sheet, agus_animation_steps, agus_fx]
                pemain1_health_bar = health_bar.HealthBarAgus(pemain1.health)
                PLAYER1_SELECTED = True
                PLAYER1_NAME = "Agus"
                
        else:
            screen.blit(choose2_bg, (0, 0))

            key = pygame.key.get_pressed()
            
            if key[pygame.K_q]:
                pemain2 = fighter.Fighter(2, 700, 390, pemain2_data, samson_sheet, samson_animation_steps, True, samson_fx, atr_samson)
                pemain2_bantuan = [samson_sheet, samson_animation_steps, samson_fx]
                pemain2_health_bar = health_bar.HealthBarSamson(pemain2.health)
                BACKGROUND_MENU = True
                PLAYER_CHARACTER_MENU = False
                PLAYER2_NAME = "Samson"
                

            elif key[pygame.K_w]:
                pemain2 = fighter.Fighter(2, 700, 390, pemain2_data, ica_sheet, ica_animation_steps, True, ica_fx, atr_ica)
                pemain2_bantuan = [ica_sheet, ica_animation_steps, ica_fx]
                pemain2_health_bar = health_bar.HealthBarIca(pemain2.health)
                BACKGROUND_MENU = True
                PLAYER_CHARACTER_MENU = False
                PLAYER2_NAME = "Ica"

            elif key[pygame.K_e]:
                pemain2 = fighter.Fighter(2, 700, 390, pemain2_data, agus_sheet, agus_animation_steps, True, agus_fx, atr_agus)
                pemain2_bantuan = [agus_sheet, agus_animation_steps, agus_fx]
                pemain2_health_bar = health_bar.HealthBarAgus(pemain2.health)
                BACKGROUND_MENU = True
                PLAYER_CHARACTER_MENU = False
                PLAYER2_NAME = "Agus"

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
        print(pygame.mouse.get_pos())
        screen.blit(option_bg, (0, 0))
        draw_text_with_outline("Press Enter to Resume", menu_font, Black, White , 240, 250)
        draw_text_with_outline("Press H for Game Guide", menu_font, Black, White, 230, 300)
        draw_text_with_outline("Press Space to Quit", menu_font, Black, White, 300, 350)
        draw_text_with_outline("Background Music", smaller_menu_font, Black, White, 210, 400)
        draw_text_with_outline("Sound Effects", smaller_menu_font, Black, White, 585, 400)
        bg_slider.draw(screen)
        fx_slider.draw(screen)
        draw_text_with_outline("Press Space to Quit", menu_font, Black, White, 300, 350)
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            PAUSE_MENU = False
        elif key[pygame.K_h]:
            PAUSE_MENU = False
            GAME_GUIDE = True
        #elif key[pygame.K_ENTER]:
            #run = False  # Change this line to set run to False
            GAME_GUIDE = True 
        elif key[pygame.K_SPACE]:
            run =False

    elif GAME_GUIDE:
        screen.blit(guide_bg, (0, 0))
        draw_text_with_outline("Press Esc to Return to Pause Menu", smaller_menu_font, Black, White, 250, 500)
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            GAME_GUIDE = False


    else:        
        screen.blit(current_background, (0, 0))

        pemain1.update()
        pemain2.update()

        pemain2.draw(screen)
        pemain1.draw(screen)

        pemain1_health_bar.draw(screen, 20, 20)
        pemain2_health_bar.draw(screen, 580, 20)
        pemain1_health_bar.update(pemain1.health)
        pemain2_health_bar.update(pemain2.health)

        draw_text_with_outline("P1 " + PLAYER1_NAME + " : " + str(score[0]), score_font, Black, White, 20, 60)
        draw_text_with_outline("P2 " + PLAYER2_NAME + " : " + str(score[1]), score_font, Black, White, 580, 60)
        # Inisialisasi variabel game_over sebelum loop game
        game_over = False

        #
        if intro <= 0 and not game_over:
            pemain1.move(Screen_Width, Screen_Height, screen, pemain2, round_over)
            pemain2.move(Screen_Width, Screen_Height, screen, pemain1, round_over)
        else:
            if not game_over:  # Hanya jika permainan belum berakhir
                draw_text_with_outline(str(intro), count_font, Black, White, (Screen_Width / 2) - 40, (Screen_Height / 3) - 50)
                if pygame.time.get_ticks() - last_count_update >= 1000:
                    intro -= 1
                    last_count_update = pygame.time.get_ticks()

        #
        pemain1.update()
        pemain2.update()

        pemain1.draw(screen)
        pemain2.draw(screen)

        print(pemain1_health_bar.health)
        print(pemain2_health_bar.health)
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
                draw_text_with_outline('Ronde Selesai', ronde_font, Black, White, 175, 230)
            if pygame.time.get_ticks() - round_over_time > round_over_cooldown:
                round_over = False
                if PLAYER1_NAME == 'Agus':
                    pemain1 = fighter.Fighter(1, 200, 390, pemain1_data, pemain1_bantuan[0], pemain1_bantuan[1], False, pemain1_bantuan[2], atr_agus)
                elif PLAYER1_NAME == 'Ica':
                    pemain1 = fighter.Fighter(1, 200, 390, pemain1_data, pemain1_bantuan[0], pemain1_bantuan[1], False, pemain1_bantuan[2], atr_ica)
                elif PLAYER1_NAME == 'Samson':
                    pemain1 = fighter.Fighter(1, 200, 390, pemain1_data, pemain1_bantuan[0], pemain1_bantuan[1], False, pemain1_bantuan[2], atr_samson)

                if PLAYER2_NAME == 'Agus':
                    pemain2 = fighter.Fighter(2, 700, 390, pemain2_data, pemain2_bantuan[0], pemain2_bantuan[1], True, pemain2_bantuan[2], atr_agus)
                elif PLAYER2_NAME == 'Ica':
                    pemain2 = fighter.Fighter(2, 700, 390, pemain2_data, pemain2_bantuan[0], pemain2_bantuan[1], True, pemain2_bantuan[2], atr_ica)
                elif PLAYER2_NAME == 'Samson':
                    pemain2 = fighter.Fighter(2, 700, 390, pemain2_data, pemain2_bantuan[0], pemain2_bantuan[1], True, pemain2_bantuan[2], atr_samson)
  
    if score[0] >= 3 or score[1] >= 3:
        if score[0] >= 3:
            VICTORY = "P1"
        else:
            VICTORY = "P2"

        draw_text_with_outline(VICTORY + " VICTORY", victory_font, Black, White, 200, 130)
        draw_text_with_outline('Tekan "Enter" untuk bermain kembali', reset_font, Black, White, 120, 220)
        game_over = True  # Menandakan bahwa permainan telah berakhir

      # Ketika permainan selesai dan pemain memilih untuk memulai kembali
        if game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                # Atur ulang kondisi permainan
                score = [0, 0]
                game_over = False
                last_count_update = pygame.time.get_ticks()  # Atur ulang waktu intro terakhir   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        else:
            bg_slider.handle_event(event)
            fx_slider.handle_event(event)

    volume_bg = bg_slider.get_volume()
    pygame.mixer.music.set_volume(volume_bg)

    volume_fx = fx_slider.get_volume()
    ica_fx.set_volume(volume_fx)
    samson_fx.set_volume(volume_fx)
    agus_fx.set_volume(volume_fx)

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        PAUSE_MENU = True

    pygame.display.flip()

pygame.quit()