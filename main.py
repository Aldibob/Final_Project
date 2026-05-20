import pygame
from Character import Character, load_frames


clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1200, 500)) # flags= NOFRAME
pygame.display.set_caption("Pixel Fighters")
icon = pygame.image.load('images/fightericon.png').convert_alpha()
pygame.display.set_icon(icon)

font = pygame.font.Font("fonts/Roboto_Condensed-BlackItalic.ttf", 50)
button_rect = pygame.Rect(500,250,300,60)

bg = pygame.image.load('icons/main_bg.jpg').convert()

game_over = False
winner = None

game_state = "menu"

# bg_sound = pygame.mixer.Sound('sounds/walking_sound.mp3')
# bg_sound.play()

player1_controls = {
	"left": pygame.K_a,
	"right": pygame.K_d,
	"up": pygame.K_w,
	"attack": pygame.K_e,
	"block": pygame.K_f
}

player1 = Character("Baki", 100, 15, 150, player1_controls)

player1.animations = {
	"idle_frames": load_frames(r"images\Fighter\idle_frames"),
	"run_frames": load_frames(r"images\Fighter\run_frames"),
	"attack": load_frames(r"images\Fighter\attack_frames"),
	"death": load_frames(r"images\Fighter\dead_frames"),
	"block": load_frames(r"images\Fighter\block_frames")
}

player2_controls = {
	"left": pygame.K_LEFT,
	"right": pygame.K_RIGHT,
	"up": pygame.K_UP,
	"attack": pygame.K_KP0,
	"block": pygame.K_DOWN
}

player2 = Character("Samurai",100, 15, 900, player2_controls)

player2.animations = {
	"idle_frames": load_frames(r"images\Samurai\idle_frames"),
	"run_frames": load_frames(r"images\Samurai\run_frames"),
	"attack": load_frames(r"images\Samurai\attack_frames"),
	"death": load_frames(r"images\Samurai\dead_frames"),
	"block": load_frames(r"images\Samurai\block_frames")
}


running = True
while running:
	keys = pygame.key.get_pressed()

	if game_state == "menu":

		title = font.render("PIXEL FIGHTERS", True,(255,255,255))

		pygame.draw.rect(screen, (50, 50, 50), button_rect)
		text = font.render("CLICK START", True, (200, 200, 200))
		text_rect = text.get_rect(center = button_rect.center)


		screen.blit(text, text_rect)
		screen.blit(title, (450, 200))

	elif game_state == "fight":
		screen.blit(bg, (0, 0))

		player1.update(keys)
		player2.update(keys)

		player1.damage_deal(player2)
		player2.damage_deal(player1)

		player1.draw(screen)
		player2.draw(screen)

		player1.draw_hp(screen, 50, 30)
		player2.draw_hp(screen, 850, 30)

		if player1.is_dead:

			if player1.frame_index >= len(player1.animations["death"]) - 1:
				game_state = "game_over"
				winner = "Samurai"

		if player2.is_dead:
			if player2.frame_index >= len(player2.animations["death"]) - 1:
				game_state = "game_over"
				winner = "Baki"

	elif game_state == "game_over":
		screen.blit(bg, (0,0))

		player1.draw(screen)
		player2.draw(screen)

		player1.draw_hp(screen, 50, 30)
		player2.draw_hp(screen, 850, 30)

		text = font.render("GAME OVER", True, (255, 0, 0))
		win_text = font.render(f"{winner} WINS!", True, (255, 255, 255))

		screen.blit(text, (450, 180))
		screen.blit(win_text, (420, 260))


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if game_state == "fight":
				if event.key == player1.controls["attack"]:
					player1.start_attack()

				if event.key == player2.controls["attack"]:
					player2.start_attack()

		if event.type == pygame.MOUSEBUTTONDOWN:
			if game_state == "menu":
				if button_rect.collidepoint(event.pos):
					game_state = "fight"

	pygame.display.update()
	clock.tick(30)

pygame.quit()