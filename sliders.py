import pygame #pygame sebagai gui

class Slider:
    def __init__(self, x, y, length, height, knob_radius):
        self.__x = x #Menyimpan posisi slider pada sumbu x
        self.__y = y #Menyimpan posisi slider pada sumbu y
        self.__length = length #Menentukan panjang slider
        self.__height = height #Menentukan tinggi slider

        self.__knob_radius = knob_radius #Menentukan seberapa besar radius knob
        self.__knob_x = x + length / 2 #Mengatur posisi awal knob di tengah slider agar volume = 0.5
        self.__dragging = False #apakah knob sedang digeser atau tidak 

        #Menyimpan atribut warna dari slider
        self.__slider_bg_color = (255, 255, 255)
        self.__slider_fg_color = (0, 150, 255)
        self.__knob_color = (0, 150, 255)

    #Membuat method untuk menggambar slider pada layar
    def draw(self, screen):
        #Menggambar persegi panjang yang mewakili latar belakang slider
        pygame.draw.rect(screen, self.__slider_bg_color, (self.__x, self.__y - self.__height // 2, self.__length, self.__height))
        #Menggambar persegi panjang untuk menampilkan bagian yang terisi slider
        pygame.draw.rect(screen, self.__slider_fg_color, (self.__x, self.__y - self.__height // 2, self.__knob_x - self.__x, self.__height))
        #Menggambar knob slider
        pygame.draw.circle(screen, self.__knob_color, (self.__knob_x, self.__y), self.__knob_radius)

    def handle_event(self, event): #metode menangani event Pygame
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if event.button == 1:  #Ketika mouse kiri meng-klik knob, memulai dragging
                if (self.__knob_x - event.pos[0]) ** 2 + (self.__y - event.pos[1]) ** 2 <= self.__knob_radius ** 2:
                    self.__dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  #Ketika mouse melepas knob, menghentikan dragging
                self.__dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.__dragging: #Jika knob di geser, mengupdate posisi knob
                self.__knob_x = min(max(event.pos[0], self.__x), self.__x + self.__length)

    def get_volume(self): #method getter
        #Menghitung level volume dari 0.0 sampai 1.0
        return (self.__knob_x - self.__x) / self.__length
        #nilai volume dihitung dari perbandingan antara posisi knob dan panjang slider