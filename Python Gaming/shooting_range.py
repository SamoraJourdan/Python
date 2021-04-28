import pygame, sys, random

pygame.init()

screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
wood_bg = pygame.image.load('Wood_BG.png')
land_bg = pygame.image.load('Land_BG.png')
water_bg = pygame.image.load('Water_BG.png')
cloud_1 = pygame.image.load('Cloud1.png')
cloud_2 = pygame.image.load('Cloud2.png')
crosshair = pygame.image.load('crosshair.png')
duck_surface = pygame.image.load('duck.png')
game_font = pygame.font.Font(None,60)
text_surface = game_font.render('You Won!', True, (255,255,255))
text_rect = text_surface.get_rect(center = (640, 360))
land_position_y = 560
land_speed = 1
water_position_y = 640
water_speed = 1.5
duck_list = []
for duck in range(20):
	duck_position_x = random.randrange(50,1200)
	duck_position_y = random.randrange(120,600)
	duck_rect = duck_surface.get_rect(center = (duck_position_x, duck_position_y))
	duck_list.append(duck_rect)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEMOTION:
			crosshair_rect = crosshair.get_rect(center = event.pos) 
		if event.type == pygame.MOUSEBUTTONDOWN:
			for index,duck_rect in enumerate(duck_list): 
				if duck_rect.collidepoint(event.pos): #crosshair_rect.colliderect(duck_rect):
					del duck_list[index]	

	land_position_y -= land_speed 	
	if land_position_y <= 520 or land_position_y >= 600:
		land_speed *= -1
	water_position_y -= water_speed 
	if water_position_y <= 620 or water_position_y >= 680:
		water_speed *= -1

	screen.blit(wood_bg, (0,0))
	
	for duck_rekt in duck_list:
		screen.blit(duck_surface, duck_rekt)

	if len(duck_list) <= 0:
		screen.blit(text_surface, (text_rect))	
	screen.blit(land_bg, (0,land_position_y))
	screen.blit(water_bg, (0,water_position_y))		
	screen.blit(crosshair, crosshair_rect)
	screen.blit(cloud_1, (100,50))
	screen.blit(cloud_2, (170,80))
	screen.blit(cloud_1, (604,40))
	screen.blit(cloud_2, (1000,90))
	screen.blit(cloud_1, (412,55))
	
	pygame.display.update()
	clock.tick(120)