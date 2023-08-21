import pygame
from settings import *

class Button():
	def __init__(self, text_input, base_color, hovering_color, left, top, w, h):

		self.rect = pygame.Rect(left,top,w,h)
		self.font = pygame.font.SysFont(UI_FONT,int(self.rect.height/3))
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(text_input,False,base_color)
		self.text_rect = self.text.get_rect(center = self.rect.center)

	def update(self, screen):
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)