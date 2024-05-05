import pygame
import sys

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        self.options = []
        self.selected_option = 0

    def add_option(self, text, action):
        self.options.append((text, action))

    def draw(self):
        self.screen.fill((0, 0, 0))  # Mengisi layar dengan warna hitam

        # Judul Menu
        title_text = self.font.render("Nama_Game", True, (255, 255, 255))
        self.screen.blit(title_text, (400 - title_text.get_width() // 2, 50))

        # Opsi Menu
        y = 200
        for idx, (text, _) in enumerate(self.options):
            option_text = self.font.render(text, True, (255, 255, 255))
            self.screen.blit(option_text, (400 - option_text.get_width() // 2, y))
            if idx == self.selected_option:
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(300, y, 200, option_text.get_height()), 3)
            y += 100

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    _, action = self.options[self.selected_option]
                    action()

class MainMenu(Menu):
    def __init__(self, screen):
        super().__init__(screen)
        self.add_option("Mulai Permainan", self.start_game)
        self.add_option("Keluar", self.quit_game)

    def start_game(self):
        print("Memulai permainan...")  # Ganti dengan kode untuk memulai permainan

    def quit_game(self):
        pygame.quit()
        sys.exit()
