import pygame #Pygame sebagai gui
from abc import ABC, abstractmethod #Import untuk melakukan abstraction

#Mendefinisikan warna
Yellow = (255, 255, 0)
Red = (255, 0, 0)
White = (255, 255, 255)
Blue = (0,0, 255)
Green = (0, 255, 0)

#Membuat kelas abstrak
class AbstrakHealthbar(ABC): #Abstraction dan kelas induk
    def __init__(self, health):
        self._health = int(health)
        #Membuat atribut yaitu health

    #Membuat method abstrak agar kelas turunannya wajib menggunakannya
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass

class HealthBarAgus(AbstrakHealthbar): #Pewarisan, membuat kelas Anak
    def __init__(self, health): #Mendefinisikan konstruktor untuk menerima parameter health
        super().__init__(health) #Memanggil konstruktor kelas induk
        self._full_health = int(health) #Menyimpan nilai nyawa penuh
        self._ratio = self._health / self._full_health #Menyimpan rasio yang berguna untuk tampilan

    #Membuat method untuk mengupdate health dan rasio
    def update(self, health): #polymorphism
        self._health = health
        self._ratio = self._health / self._full_health

    #Membuat method untuk menggambar health bar pada layar
    def draw(self, screen, x, y): #polymorphism
       #Menggambar border putih di sekitar health bar
       pygame.draw.rect(screen, White, (x - 2, y - 2, 405, 34))

       #Menggambar persegi panjang merah sebagai background dari health bar
       pygame.draw.rect(screen, Red, (x, y, 400, 30))

       #Menggambar persegi panjang kuning sebagai health
       pygame.draw.rect(screen, Yellow, (x, y, 400 * self._ratio, 30)) 
    
class HealthBarIca(AbstrakHealthbar): #Pewarisan, memubat kelas Anak
    def __init__(self, health): #Mendefinisikan konstruktor untuk menerima parameter health
        super().__init__(health) #Memanggil konstruktor kelas induk
        self._full_health = int(health) #Menyimpan nilai nyawa penuh
        self._ratio = self._health / self._full_health #Menyimpan rasio yang berguna untuk tampilan
    
    #Membuat method untuk mengupdate health dan rasio
    def update(self, health): #polymorphism
        self._health = health
        self._ratio = self._health / self._full_health

    #Membuat method untuk menggambar health bar pada layar
    def draw(self, screen, x, y): #polymorphism
       #Menggambar border putih di sekitar health bar
       pygame.draw.rect(screen, White, (x - 2, y - 2, 405, 34))

       #Menggambar persegi panjang merah sebagai background dari health bar
       pygame.draw.rect(screen, Red, (x, y, 400, 30))

       #Menggambar persegi panjang hijau sebagai health
       pygame.draw.rect(screen, Green, (x, y, 400 * self._ratio, 30))

class HealthBarSamson(AbstrakHealthbar): #Pewarisan, memubat kelas Anak
    def __init__(self, health): #Mendefinisikan konstruktor untuk menerima parameter health
        super().__init__(health) #Memanggil konstruktor kelas induk
        self._full_health = int(health) #Menyimpan nilai nyawa penuh
        self._ratio = self._health / self._full_health #Menyimpan rasio yang berguna untuk tampilan
    
    #Membuat method untuk mengupdate health dan rasio
    def update(self, health): #polymorphism
        self._health = health
        self._ratio = self._health / self._full_health 

    #Membuat method untuk menggambar health bar pada layar
    def draw(self, screen, x, y): #polymorphism
       #Menggambar border putih di sekitar health bar
       pygame.draw.rect(screen, White, (x - 2, y - 2, 405, 34))

       #Menggambar persegi panjang merah sebagai background dari health bar
       pygame.draw.rect(screen, Red, (x, y, 400, 30))

       #Menggambar persegi panjang biru sebagai health
       pygame.draw.rect(screen, Blue, (x, y, 400 * self._ratio, 30))
