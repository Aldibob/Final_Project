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
	def __init__(self,name,hp,damage,x):
		self.name = name
		self.hp = hp
		self.damage = damage

		self.x = x
		self.base_y = 210
		self.y = self.base_y

		self.jump_count = 9
		self.is_jump = False

		self.frame_index = 0
		self.state = "idle"
		self.animations = {}

		self.vx = 0
		self.speed = 7
		self.facing_right = True

	def update(self, keys):
		self.move(keys)
		self.jump(keys)
		self.update_animation()

	def update_animation(self):
		old_state = self.state

		if self.vx != 0:
			self.state = "Run"
		else:
			self.state = "idle"

		if old_state != self.state:
			self.frame_index = 0

		frames = self.animations[self.state]

		if len(frames) == 0:
			return

		self.frame_index += 0.2

		if self.frame_index >= len(frames):
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
		self.vx = 0

		if keys[pygame.K_a] and self.x > 10:
			self.vx -= self.speed
			self.facing_right = False
		if keys[pygame.K_d] and self.x < 1100:
			self.vx += self.speed
			self.facing_right = True

		self.x += self.vx


	def jump(self,keys):
		if not self.is_jump:
			if keys[pygame.K_w]:
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

