import pygame, sys, random

class SpaceShip(pygame.sprite.Sprite):
	def __init__(self,path,x_pos,y_pos):
		super().__init__()
		self.uncharged = pygame.image.load(path)
		self.charged = pygame.image.load('spaceship_charged.png')
		self.image = self.uncharged
		self.rect = self.image.get_rect(center = (x_pos,y_pos))
		self.shield_surface = pygame.image.load('shield.png')
		self.health = 5

	def update(self):
		self.rect.center = pygame.mouse.get_pos()
		self.screen_constrain()
		self.display_health()

	def screen_constrain(self):
		if self.rect.right >= 1280:
			self.rect.right = 1280
		elif self.rect.left <= 0:
			self.rect.left = 0

	def display_health(self):
		for index,shield in enumerate(range(self.health)):
			screen.blit(self.shield_surface,(10 + index*40,10))	

	def get_damage(self, damage_amount):
		self.health -= damage_amount	

	def charge(self):
		self.image = self.charged

	def uncharge(self):
		self.image = self.uncharged				
					
class Meteor(pygame.sprite.Sprite):
	def __init__(self,path,x_pos,y_pos,x_speed,y_speed):
		super().__init__()
		self.image = pygame.image.load(path)
		self.rect = self.image.get_rect(center = (x_pos,y_pos))
		self.x_speed = x_speed
		self.y_speed = y_speed

	def update(self):
		self.rect.centerx += self.x_speed
		self.rect.centery += self.y_speed
		if self.rect.centery >= 800:
			self.kill

class Lazer(pygame.sprite.Sprite):
	def __init__(self,path,pos,speed):
		super().__init__()
		self.image = pygame.image.load(path)
		self.rect = self.image.get_rect(center = pos)
		self.speed = speed		
	def update(self):
		self.rect.centery -= self.speed
		if self.rect.centery <= -100:
			self.kill

def main_game():
	global lazer_active
	lazer_group.draw(screen)
	lazer_group.update()
	spaceship_group.draw(screen)
	spaceship_group.update()
	meteor_group.draw(screen)
	meteor_group.update()
	if pygame.sprite.spritecollide(spaceship_group.sprite, meteor_group, True):
		spaceship_group.sprite.get_damage(1)
	for lazer in lazer_group:
		pygame.sprite.spritecollide(lazer, meteor_group, True)
	if pygame.time.get_ticks() - lazer_timer >= 1000:
		lazer_active = True
		spaceship_group.sprite.charge()	
	return 1 	


def end_game():
	text_surface = game_font.render('Game Over', True, (255,255,255))
	text_rect = text_surface.get_rect(center = (640,340)) 
	screen.blit(text_surface,text_rect)

	score_surface = game_font.render(f'Score: {score}', True, (255,255,255))
	score_rect = score_surface.get_rect(center = (640,380)) 
	screen.blit(score_surface,score_rect)



pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
game_font = pygame.font.Font('LazenByCompSmooth.ttf', 40)
score = 0
lazer_timer = 0
lazer_active = False

meteor_group = pygame.sprite.Group()

METEOR_EVENT = pygame.USEREVENT
pygame.time.set_timer(METEOR_EVENT,200)

spaceship = SpaceShip('spaceship.png',640,500)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

lazer_group = pygame.sprite.Group()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			pygame.quit()
			sys.exit()
		if event.type == METEOR_EVENT:
			meteor_path = random.choice(('Meteor1.png','Meteor2.png','Meteor3.png'))
			random_x_pos = random.randrange(0,1280)
			random_y_pos = random.randrange(-500,-50)
			random_x_speed = random.randrange(-1,1)
			random_y_speed = random.randrange(4,10)
			meteor = Meteor(meteor_path,random_x_pos,random_y_pos,random_x_speed,random_y_speed)
			meteor_group.add(meteor)
		if event.type == pygame.MOUSEBUTTONDOWN and lazer_active:
			new_lazer = Lazer('Laser.png', event.pos, 5)
			lazer_group.add(new_lazer)	
			lazer_active = False
			lazer_timer = pygame.time.get_ticks()
			spaceship_group.sprite.uncharge()
		if event.type == pygame.MOUSEBUTTONDOWN and spaceship_group.sprite.health <=0:	
			spaceship_group.sprite.health = 5
			meteor_group.empty()
			score = 0

	screen.fill((42,45,51))	
	if spaceship_group.sprite.health > 0:
		score += main_game()
	else:
		end_game()	
	pygame.display.update()
	clock.tick(120)		

	