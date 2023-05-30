#Создай собственный Шутер!
'''from random import randint
from pygame import *

window = display.set_mode((700, 500))
display.set_caption('ШУТЕР')
background = transform.scale(image.load ('galaxy.jpg'), (700, 500))

goal = 10


class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
       self.size_x = size_x
       self.size_y = size_y
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 630:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 15, -15)
        bullets.add(bullet)


lost = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.x = randint(80, 700 - 80)
            self.rect.y = 0
            lost = lost + 1


class Bullet(GameSprite):
   def update(self):
      self.rect.y += self.speed
      if self.rect.y < 0:
         self.kill()



monsters = sprite.Group()
for i in range(1, 6):
        monster = Enemy('ufo.png', randint(80, 700 - 80), -40, 50, 30, randint(1, 1))
        monsters.add(monster)

ship = Player('rocket.png', 5, 405, 60, 80, 3)


bullets = sprite.Group()



font.init()
font = font.Font(None, 35)
win = font.render('YOU WIN!', True, (255, 216, 0))
lose = font.render('YOU LOSE!', True, (118, 0, 0))

max_lost = 15
lost = 0
score = 0
finish = False
game = True


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.fire()
        
    if not finish:
            window.blit(background, (0, 0))
            text = font.render("Счет: " + str(score), 1, (255, 255, 255))
            window.blit(text, (10, 20))
            text_lose = font.render("Пропущено: " + str(lost), 1, (255, 255, 255))
            window.blit(text_lose, (10, 50))
            
            bullets.update()
            ship.update()
            monsters.update()

            bullets.draw(window)

            collides = sprite.groupcollide(monsters, bullets, True, True)
            for c in collides:
                score = score + 1
                monster = Enemy('ufo.png', randint(80, 700 - 80), -40, 80, 50, randint(1, 1))
                monsters.add(monster)
            if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
                finish = True 
                window.blit(lose, (200, 200))

            if score >= goal:
                finish = True
                window.blit(win, (200, 200))

            ship.reset()
            monsters.draw(window)

            display.update()'''


from random import randint
from pygame import *

window = display.set_mode((700, 500))
display.set_caption('ШУТЕР')
background = transform.scale(image.load ('galaxy.jpg'), (700, 500))

goal = 10


class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
       self.size_x = size_x
       self.size_y = size_y
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 630:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 15, -15)
        bullets.add(bullet)


lost = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.x = randint(80, 700 - 80)
            self.rect.y = 0
            lost = lost + 1


class Bullet(GameSprite):
   def update(self):
      self.rect.y += self.speed
      if self.rect.y < 0:
         self.kill()

asteroids = sprite.Group()
for i in range(1, 3):
    asteroid = Enemy('asteroid.png', randint(30, 700 - 30), -40, 80, 50, randint(1, 1))
    asteroids.add(asteroid)

monsters = sprite.Group()
for i in range(1, 6):
        monster = Enemy('ufo.png', randint(80, 700 - 80), -40, 50, 30, randint(1, 1))
        monsters.add(monster)

ship = Player('rocket.png', 5, 405, 60, 80, 3)


bullets = sprite.Group()


font.init()
font = font.SysFont('Arial', 35)
win = font.render('YOU WIN!', True, (255, 216, 0))
lose = font.render('YOU LOSE!', True, (118, 0, 0))

max_lost = 15
lost = 0
score = 0
finish = False
game = True


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.fire()
    

    if not finish:
            window.blit(background, (0, 0))
            text = font.render("Счет: " + str(score), 1, (255, 255, 255))
            window.blit(text, (10, 20))
            text_lose = font.render("Пропущено: " + str(lost), 1, (255, 255, 255))
            window.blit(text_lose, (10, 50))
            
            bullets.update()
            ship.update()
            monsters.update()
            asteroids.update()

            bullets.draw(window)

            collides = sprite.groupcollide(monsters, bullets, True, True)
            for c in collides:
                score = score + 1
                monster = Enemy('ufo.png', randint(80, 700 - 80), -40, 80, 50, randint(1, 1))
                monsters.add(monster)

            if sprite.spritecollide(ship, monsters, False) or lost >= max_lost or sprite.spritecollide(ship, asteroids, False) :
                finish = True 
                window.blit(lose, (200, 200))
    
            if score >= goal:
                finish = True
                window.blit(win, (200, 200))

            ship.reset()
            monsters.draw(window)

            asteroids.draw(window)

            display.update()








'''rel_time = False
num_fire = 0
timer = 0
last_time = 0

if rel_time == True:
        now_time = timer()
        if now_time - last_time > 3:
            reload = font2.render('Wait, reload', 1, (150, 0, 0))
            window.blit(reload, (260, 460))
        elif:
            num_fire = 0
            rel_time = False'''