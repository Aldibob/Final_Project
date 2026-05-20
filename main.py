import pygame
from Character import Character, load_frames


clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1200, 500)) # flags= NOFRAME
pygame.display.set_caption("Pixel Fighters")
icon = pygame.image.load('images/fightericon.png').convert_alpha()
pygame.display.set_icon(icon)


bg = pygame.image.load('icons/main_bg.jpg').convert()


# bg_sound = pygame.mixer.Sound('sounds/walking_sound.mp3')
# bg_sound.play()

player1_controls = {
	"left": pygame.K_a,
	"right": pygame.K_d,
	"up": pygame.K_w,
	"attack": pygame.K_e
}

player1 = Character("Baki", 100, 10, 150, player1_controls)

player1.animations = {
	"idle_frames": load_frames(r"images\Fighter\idle"),
	"run_frames": load_frames(r"images\Fighter\Run\run"),
	"attack": load_frames(r"images\Fighter\attack_frames")
}

player2_controls = {
	"left": pygame.K_LEFT,
	"right": pygame.K_RIGHT,
	"up": pygame.K_UP,
	"attack": pygame.K_KP0
}

player2 = Character("Samurai",100, 10, 900, player2_controls)

player2.animations = {
	"idle_frames": load_frames(r"images\Samurai\idle_frames"),
	"run_frames": load_frames(r"images\Samurai\run_frames"),
	"attack": load_frames(r"images\Samurai\attack_frames")
}


running = True
while running:

	screen.blit(bg,(0, 0))
	player1.draw_hp(screen,50,30)
	player2.draw_hp(screen, 850, 30)

	keys = pygame.key.get_pressed()

	player1.update(keys)
	player1.damage_deal(player2)
	player1.draw(screen)

	player2.update(keys)
	player2.damage_deal(player1)
	player2.draw(screen)

	pygame.display.update()


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()

		if event.type == pygame.KEYDOWN:
			if event.key == player1.controls["attack"]:
				player1.start_attack()

			if event.key == player2.controls["attack"]:
				player2.start_attack()



	clock.tick(30)
