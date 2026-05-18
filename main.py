import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1200, 500)) # flags= NOFRAME
pygame.display.set_caption("Pixel Fighters")
icon = pygame.image.load('images/fightericon.png').convert_alpha()
pygame.display.set_icon(icon)


bg = pygame.image.load('icons/main_bg.jpg').convert()


player_anim_count = 0
idle_anim_count = 0

bg_sound = pygame.mixer.Sound('sounds/walking_sound.mp3')

# bg_sound.play()


running = True
while running:


	screen.blit(bg,(0, 0))

	keys = pygame.key.get_pressed()

	# if keys[pygame.K_a]:
	# 	screen.blit(left_walk[player_anim_count], (player_x, player_y))
	# elif keys[pygame.K_d]:
	# 	screen.blit(right_walk[player_anim_count], (player_x, player_y))
	# else:
	# 	screen.blit(idle[idle_anim_count], (player_x, player_y))

	if player_anim_count == 7:
		player_anim_count = 0
	else:
		player_anim_count += 1

	if idle_anim_count == 5:
		idle_anim_count = 0
	else:
		idle_anim_count += 1

	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()

	clock.tick(13)
