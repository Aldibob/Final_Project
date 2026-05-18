import os
import pygame

def load_frames(folder):
	frames = []

	for file in sorted(os.listdir(folder)):
		path = os.path.join(folder, file)
		image = pygame.image.load(path).convert_alpha()
		frames.append(image)

	return frames

class Character:
	def __init__(self,name,hp,damage,x):
		self.name = name
		self.hp = hp
		self.damage = damage
		self.x = x
		self.y = 210
		self.is_jump = False
		self.frame_index = 0
		self.state = "idle"
		self.animations = {}
		self.jump_count = 9
		self.vx = 0
		self.speed = 7

	def update(self, keys):
		self.move(keys)
		self.jump(keys)
		self.update_animation()

	def update_animation(self):
		old_state = self.state

		if self.vx != 0:
			self.state = "run"
		else:
			self.state = "idle"

		if old_state != self.state:
			self.frame_index = 0

		self.frame_index += 0.2

		if self.frame_index >= len(self.animations[self.state]):
			self.frame_index = 0

	def draw(self, screen):
		if self.state in self.animations:
			frame = self.animations[self.state][int(self.frame_index)]
			screen.blit(frame, (self.x, self.y))

	def move(self,keys):
		self.vx = 0

		if keys[pygame.K_a]:
			self.vx -= self.speed
		if keys[pygame.K_d]:
			self.vx += self.speed

		self.x += self.vx


	def jump(self,keys):
		if not self.is_jump:
			if keys[pygame.K_w]:
				self.is_jump = True
		else:
			if self.jump_count >= -9:
				if self.jump_count > 0:
					self.y -= (self.jump_count ** 2) / 2
				else:
					self.y += (self.jump_count ** 2) / 2

				self.jump_count -= 1
			else:
				self.is_jump = False
				self.jump_count = 9

