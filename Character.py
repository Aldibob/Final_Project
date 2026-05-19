import os
import pygame

BASE_DIR = os.path.dirname(__file__)

def load_frames(folder):
	frames = []

	full_path = os.path.join(BASE_DIR,folder)

	for file in sorted(os.listdir(full_path)):
		path = os.path.join(full_path, file)
		image = pygame.image.load(path).convert_alpha()
		frames.append(image)

	return frames

class Character:
	def __init__(self,name,hp,damage,x, controls):
		self.name = name
		self.hp = hp
		self.damage = damage
		self.controls = controls

		self.x = x
		self.base_y = 210
		self.y = self.base_y

		self.jump_count = 9
		self.is_jump = False

		self.frame_index = 0
		self.state = "idle"
		self.animations = {}

		self.is_attacking = False
		self.attack_frame = 0
		self.attack_timer = 0

		self.attack_started = False
		self.attack_start_frame = 3
		self.attack_end_frame = 3
		self.hit_done = False


		self.vx = 0
		self.speed = 7
		self.facing_right = True

	def update(self, keys):
		self.move(keys)
		self.jump(keys)
		self.update_attack()
		self.update_animation()

	def update_animation(self):
		old_state = self.state

		if self.is_attacking:
			self.state = "attack"

		elif self.vx != 0:
			self.state = "run"
		else:
			self.state = "idle"

		if old_state != self.state:
			self.frame_index = 0

		frames = self.animations[self.state]

		if len(frames) == 0:
			return

		self.frame_index += 0.5

		if self.frame_index >= len(frames):
			if self.state == "attack":
				self.is_attacking = False
				self.state = "idle"
			self.frame_index = 0

	def draw(self, screen):
		if self.state not in self.animations:
			return

		frames = self.animations[self.state]

		if len(frames) == 0:
			return

		frame = frames[int(self.frame_index)]

		if not self.facing_right:
			frame = pygame.transform.flip(frame,True,False)

		screen.blit(frame, (self.x, self.y))

	def move(self,keys):
		if self.is_attacking:
			return

		self.vx = 0

		if keys[self.controls["left"]] and self.x > 10:
			self.vx -= self.speed
			self.facing_right = False
		if keys[self.controls["right"]] and self.x < 1100:
			self.vx += self.speed
			self.facing_right = True

		self.x += self.vx


	def jump(self,keys):
		if not self.is_jump:
			if keys[self.controls["up"]]:
				self.is_jump = True
				self.jump_count = 9
		else:
			if self.jump_count >= -9:
				if self.jump_count > 0:
					direction = -1
				else:
					direction = 1

				self.y += (self.jump_count ** 2) / 2 * direction
				self.jump_count -= 1

			else:
				self.is_jump = False
				self.y = self.base_y


	def start_attack(self):
		if not self.is_attacking:
			self.is_attacking = True
			self.state = "attack"
			self.frame_index = 0
			self.attack_timer = 0
			self.hit_done = False

	def update_attack(self):
		if self.is_attacking:
			self.attack_timer += 1

			frames = self.animations["attack"]

			if self.frame_index > len(frames) - 1:
				self.is_attacking = False
				self.state = "idle"
				self.attack_timer = 0

	def get_hitbox(self):
		return pygame.Rect(self.x, self.y, 50, 80)

	def attack_hitbox(self):
		if not self.is_attacking:
			return None

		if self.facing_right:
			return pygame.Rect(self.x + 40, self.y, 40, 80)
		else:
			return pygame.Rect(self.x - 40, self.y, 40, 80)

	def damage_deal(self, other):
		if not self.is_attacking:
			return

		current_frame = int(self.frame_index)

		if current_frame < self.attack_start_frame or current_frame > self.attack_end_frame:
			return

		if self.hit_done:
			return

		attack_box = self.attack_hitbox()

		if attack_box and attack_box.colliderect(other.get_hitbox()):
			other.hp -= self.damage

			self.hit_done = True

