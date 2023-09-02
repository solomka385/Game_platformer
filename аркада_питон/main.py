from pygame import *
from pygame.locals import *
from random import randint



class stena(sprite.Sprite):
    def __init__(self,image3, x, y,shift):
        sprite.Sprite.__init__(self) 
        self.image =transform.scale(image.load(image3), (500, 160))
        self.rect = self.image.get_rect()
        self.rect.x = 330
        self.rect.y = 500
        self.shift = 0
    def go(self):
        self.rect.x += self.shift
        window.blit(self.image, (self.rect.x, self.rect.y))

class Hero(stena,sprite.Sprite):
    def __init__(self,score , x, y,x_speed,y_speed,prov,prizhok,image1):
        sprite.Sprite.__init__(self) 
        self.image = transform.scale(image.load(image1),(80,80))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 300
        self.x_speed = 0
        self.y_speed = 0
        self.score= 0
        self.prov = False
        self.prizhok = False
    def go(self):
        
        collides = sprite.spritecollide(self, grsten, False)
        s = sprite.spritecollideany(self, grsten, collided = None)
        if len(collides) > 0:
            
            
            collides = sprite.spritecollide(self, grsten, True)
            for c in collides:
            
                    print('efe')
                    
                    self.y_speed = 0
                    self.prov = True
                    
                    
                    self.prizhok = False
                  #  self.image = transform.scale(image.load('hero.png'),(80,80))
                
            
        else:
            if self.prov == False:
                
                
                self.gravitate()
                self.rect.y+=self.y_speed         
                
        
        
        self.rect.x += self.x_speed

        
    def jump(self):
         
        for i in range(1, 12):
            self.go()
            self.y_speed -= 1
            
            if i >= 3  and  i < 10:
                self.image = transform.scale(image.load('C://Users/alex1/Desktop/недопрограммы/питон/аркада_питон/pacletaet.png'),(80,80))

              
    def gravitate(self):
       self.y_speed += 0.4
    

class Enemy(sprite.Sprite):
    def __init__(self, image1, x, y):
        sprite.Sprite.__init__(self) 
        self.image =transform.scale(image.load(image1), (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = randint(20,950)
        
        self.rect.y = 5

def draw(Hero):
    global imageind
    global images
    hero.image= images
    if imageind == 16:
        imageind = 0
    window.blit((hero.image[imageind//4]), (hero.rect.x, hero.rect.y))
    imageind += 1
imageind = 4

window = display.set_mode((1200, 800))
background = image.load("C://Users/alex1/Desktop/недопрограммы/питон/аркада_питон/fon.jpg")
display.set_caption("Аркада")
background = transform.scale(background, (1200, 800))
window.blit(background, (0,0))



images = [image.load("C://Users/alex1/Desktop/недопрограммы/питон/аркада_питон/1.png"), image.load("C://Users/alex1/Desktop/недопрограммы/питон/аркада_питон/2.png"),
image.load("C://Users/alex1/Desktop/недопрограммы/питон/аркада_питон/3.png"), image.load("C://Users/alex1/Desktop/недопрограммы/питон/аркада_питон/4.png")]
hero = Hero(0, 10, 20, 10, 10, False, False, 'C://Users/alex1/Desktop/недопрограммы/питон/аркада_питон/2.png')
enemy = Enemy("C://Users/alex1/Desktop/недопрограммы/питон/аркада_питон/enemy.png", 200, 250)
stenapol = stena('C://Users/alex1/Desktop/недопрограммы/питон/аркада_питон/platform.png', 500, 800, 0)

shift = 0
speed = 0
allk = sprite.Group()
allk.add(hero)
allk.add(enemy)
draw(hero)

grsten = sprite.Group()
grsten.add(stenapol)

left = False
right = False

run=True
while run:
    
    for e in event.get():
        if e.type == QUIT:
            run=False
        elif e.type == KEYDOWN:
            if e.key== K_LEFT:
                hero.x_speed =- 10
                print(left)
                if left == False:
                    if imageind == 16:
                        imageind = 0
                    window.blit(transform.flip(hero.image[imageind//4], True, False), (hero.rect.x, hero.rect.y))

                left = True
                right = False

            elif e.key == K_RIGHT:
                hero.x_speed = 10
                if right == False:
                    if imageind == 16:
                        imageind = 0
                    window.blit(transform.flip(hero.image[imageind//4], True, False), (hero.rect.x, hero.rect.y)) 
                right = True
                left = False

            elif e.key == K_SPACE and hero.prizhok == False: 
                hero.prov = False
                hero.prizhok = True
                hero.jump()

        elif e.type == KEYUP:
            if e.key == K_LEFT:
                hero.x_speed=0
            elif e.key == K_RIGHT:
                hero.x_speed = 0        
                
                    
                
         

    window.blit(background, (0,0))
    
    stenapol.shift = 0
    win_width = 1250
    shift += speed
    local_shift = shift % win_width
    window.blit(background, (local_shift, 0))
    if local_shift != 0:
        window.blit(background, (local_shift - win_width + 50, 0))
    left_bound = win_width // 9
    right_bound = int(win_width - 3 * left_bound) 
    
    if (hero.rect.x > right_bound and hero.x_speed > 0):
        shift -= hero.x_speed
        hero.rect.x = right_bound
        stenapol.shift -= 15
    if (hero.rect.x < left_bound and   hero.x_speed < 0):
        shift -= hero.x_speed
        hero.rect.x = left_bound
        stenapol.shift += 15

    stenapol.go()
    #stena1.go()
    #stena2.go()
    grsten.update()
    hero.go()
    draw(hero)

    
    


    display.update()