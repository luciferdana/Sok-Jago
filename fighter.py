import pygame #Pygame sebagai gui
from abc import ABC, abstractmethod #Import untuk melakukan abstraction

class AbstrakFighter(ABC): #abstraction
    def __init__(self, pemain, x, y, data, sprite_sheet, animation_steps, flip, sound_fx, attribute):
        self.pemain = pemain #mendifinisikan player 1 atau player 2
        self.size = data[0] #ukuran gambar frame karakter
        self.image_scale = data[1] #menyimpan skala gambar
        self.offset = data[2] #menyimpan variabel x dan y untuk membenarkan posisi pemain

        self.rectangle = pygame.Rect((x, y, 80, 100)) #membuat hitbox pemain
        self.jump = False #atribut untuk melihat apakah pemain sedang melompat atau tidak
        self.vel_y = 0 #kecepatan saat melompat

        self.running = False #apakah kondisi karakter sedang berlari
        self.attack_cooldown = 0 #agar pemain tidak bisa spam attack terus-menerus

        self.speed = attribute[0] #kecepatan karakter
        self.cd = attribute[1] #attribute cooldown yang dimiliki oleh karakternya
        self.damage = attribute[2] #attribute damage unik setiap karakter
        self.health = attribute[3] #nyawa pemain

        self.attack = 0 #jenis attack
        self.attacking = False #untuk memeriksa apakah sedang menyerang atau tidak
        self.hit = False #apakah kondisi karakter sedang terkena serangan
        
        self.flip = flip #membalikkan arah serangan pemain dengan lokasi musuh sehingga serangan pemain pasti mengarah ke musuh
        self.animation_lists = self.load_images(sprite_sheet, animation_steps) #memanggil fungsi load images agar animasi bisa berjalan

        self.action = 0 #sebagai variabel untuk menentukan aksi apa yang dilakukan pemain, lalu nilai digunakan untuk menjalankan animasi yang sesuai
        self.frame_index = 0 #berguna sebagai index untuk memindahkan frame animasi
        self.image = self.animation_lists[self.action][self.frame_index] #untuk menunjukkan animasi yang sesuai aksi dan frame-nya

        self.time = pygame.time.get_ticks() #mengambil waktu
        self.alive = True #apakah pemain masih hidup 
        self.sound_fx = sound_fx #menyimpan sound effect

    #membuat abstract method agar harus diimplementasikan oleh keturunannya
    @abstractmethod 
    def load_images(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def performed_attack(self):
        pass

    @abstractmethod
    def update_action(self):
        pass

    @abstractmethod
    def draw(self):
        pass

class Fighter(AbstrakFighter):
    def __init__(self, pemain, x, y, data, sprite_sheet, animation_steps, flip, sound_fx, attribute):
        super().__init__(pemain, x, y, data, sprite_sheet, animation_steps, flip, sound_fx, attribute)
        #menggunakan super untuk memanggil konstruktor dari kelas induk yaitu konstruktor AbstrakFighter

    #fungsi load images untuk animasi
    def load_images(self, sprite_sheet, animation_steps):
        animation_lists = [] #berisi semua animasi, track semua animasi dari temp_image_list
        #ekstraksi image dari spritesheets
        for y, animation in enumerate(animation_steps):
            temp_image_list = []
            for x in range(animation):
                temp_image = sprite_sheet.subsurface(x * self.size, y * self.size , self.size, self.size) #menampilkan satu frame karakter
                temp_image = pygame.transform.scale(temp_image, (self.size * self.image_scale, self.size * self.image_scale))
                temp_image_list.append(temp_image) #list untuk menyimpan frame apa saja yang dibutuhkan
            animation_lists.append(temp_image_list)
        return animation_lists #mengembalikan list animasi untuk dijalankan

    #fungsi agar karakter bisa bergerak dan menyerang
    def move(self, Screen_Width, Screen_Height, surface, target, round_over):
        Gravity = 2 #agar pemain dapat turun kembali setelah melompat
        dx = 0 #perubahan koordinat sumbu x
        dy = 0 #perubahaan koordinat sumbu y

        self.running = False #apakah pemain sedang berlari
        self.attack = 0 #jenis attack pemain

        #mengambil key yang dipencet
        key = pygame.key.get_pressed()

        #memastikan pemain hanya dapat bergerak jika tidak sedang menyerang
        if self.attacking == False and self.alive == True and round_over == False:
            #movement pemain 1
            if self.pemain == 1:
                #movement
                if key[pygame.K_a]:
                    dx = -self.speed #pemain berlari ke kiri
                    self.running = True
                if key[pygame.K_d]:
                    dx = self.speed #pemain berlari ke kanan
                    self.running = True

                #melompat
                if key[pygame.K_w] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True
                    
                #menyerang
                if key[pygame.K_q] or key[pygame.K_e]:
                    self.performed_attack(surface, target)
                    if key[pygame.K_q]:
                        self.attack = 1
                    if key[pygame.K_e]:   
                        self.attack = 2        
            elif self.pemain == 2:
                #movement
                if key[pygame.K_j]:
                    dx = -self.speed #pemain berlari ke kiri
                    self.running = True
                if key[pygame.K_l]:
                    dx = self.speed #pemain berlari ke kanan
                    self.running = True

                #melompat
                if key[pygame.K_i] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True
                    
                #menyerang
                if key[pygame.K_u] or key[pygame.K_o]:
                    self.performed_attack(surface, target)
                    if key[pygame.K_u]:
                        self.attack = 1
                    if key[pygame.K_o]:   
                        self.attack = 2

        #mengimpelementasikan gravitasi
        self.vel_y += Gravity
        dy+= self.vel_y #mengupdate posisi pemain ketika melompat

        #bagian memastikan posisi karakter pemain

        #memastikan karakter pemain tetap berada pada layar di bagian kiri
        if self.rectangle.left + dx < 0:
            dx = -self.rectangle.left

        #memastikan karakter pemain tetap berada pada layar di bagian kanan
        if self.rectangle.right + dx > Screen_Width:
            dx = Screen_Width - self.rectangle.right

        #memastikan karakter pemain tetap berada pada "tanah"
        if self.rectangle.bottom + dy > Screen_Height - 110:
            self.vel_y = 0;
            self.jump = False
            dy = Screen_Height - 110 - self.rectangle.bottom

        #memastikan pemain saling mengarah ke satu sama lain
        if target.rectangle.centerx > self.rectangle.centerx:
            self.flip = False
        else:
            self.flip = True

        #mengimplementasikan cooldown attack
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        #update posisi dx dan dy nya jika berhasil bergerak
        self.rectangle.x += dx
        self.rectangle.y += dy

    #mengupdate animasi
    def update(self):

        #jika health pemain sudah habis, maka gunakan animasi death pemain
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.update_action(6) #6 untuk mati
        #mengecek aksi apa yang dilakukan pemain untuk menyesuaikan animasi
        elif self.hit == True:
            self.update_action(5) #5 untuk terkena serangan
        elif self.attacking == True:
            if self.attack == 1:
                self.update_action(3) #3 uuntuk jenis serangan 1
            elif self.attack == 2:
                self.update_action(4) #4 untuk jenis serangan 2
        elif self.jump == True:
            self.update_action(2) #2 untuk melompat
        elif self.running == True:
            self.update_action(1) #1 untuk running
        else:
            self.update_action(0) #0 untuk idle

        #mengembalikan pemain menjadi posisi semula 
        if self.action == 5:
            self.hit = False

            #jika pemain diserang, serangan pemain digagalkan
            self.attacking = False
            self.attack_cooldown = self.cd

        #menampilkan setiap frame sesuai dengan timer
        timer = 55
        #milisekon per frame
        self.image = self.animation_lists[self.action][self.frame_index]

        #mengecek waktu
        if pygame.time.get_ticks() - self.time > timer:
            self.frame_index += 1
            self.time = pygame.time.get_ticks()
        
        #mengecek apakah animasi telah selesai
        if self.frame_index >= len(self.animation_lists[self.action]):
            #jika pemain mati, akhirkan animasinya
            if self.alive == False:
                self.frame_index = len(self.animation_lists[self.action]) - 1
                #memastikan animasi berhenti pada akhir index terakhir

            else:
                self.frame_index = 0 #memulai animasi dari awal

                #mengecek apakah serangan sudah dilakukan
                if self.action == 3 or self.action == 4:
                    self.attacking = False
                    self.attack_cooldown = 20

    #mendefinisikan fungsi menyerang agar pemain bisa menyerang musuh
    def performed_attack(self, surface, target):
        #membuat dan menampilkan sebuah bentuk sebagai senjata
        attacking_rectangle = pygame.Rect(self.rectangle.centerx - (self.rectangle.width * self.flip), self.rectangle.y, 2 * self.rectangle.width, self.rectangle.height)

        #pemain boleh menyerang ketika sedang tidak cooldown
        if self.attack_cooldown == 0 :
            self.attacking = True #kondisi pemain apakah sedang menyerang atau tidak
            self.sound_fx.play() #jika pemain menyerang, nyalakan sound fx
            if attacking_rectangle.colliderect(target.rectangle):
                target.health -= self.damage
                target.hit = True

    def update_action(self, new_action):
        #mengecek apakah aksi berbeda dengan sebelumnya
        if new_action != self.action:
            self.action = new_action
        
            #mengupdate pengaturan animasi
            self.frame_index = 0
            self.time = pygame.time.get_ticks()

    #agar karakter pemain terlihat pada window dan surface adalah letak pemainnya
    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(img, (self.rectangle.x - (self.offset[0] * self.image_scale), self.rectangle.y - (self.offset[1] * self.image_scale))) 
        #laod gambar pemain sesuai dengan koordinat bentuk yang telah dibuat