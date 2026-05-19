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

player1 = Character("fighter", 100, 10, 150)

player1.animations = {
	"idle": load_frames(r"images\Fighter\idle_frames"),
	"Run": load_frames(r"images\Fighter\Run\run")
}

running = True
while running:

	screen.blit(bg,(0, 0))

	keys = pygame.key.get_pressed()

	player1.update(keys)
	player1.draw(screen)

	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()

	clock.tick(40)
