import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
	'''管理游戏资源和行为的类'''
	def __init__(self):
		pygame.init()
		self.settings = Settings()
		#设置背景色
		self.bg_color = (230,230,230)

		self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)

	def run_game(self):
		""" 开始游戏的主循环 """
		while True:
			#监听键盘和鼠标事件
			self._check_events()
			self.ship.update()
			self._update_screen()

	def _check_events(self):
		'''响应鼠标和键盘事件'''
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					#向右移动飞船
					self.ship.moving_right = True
				elif event.key == pygame.K_LEFT:
					self.ship.moving_left = True

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					self.ship.moving_right = False
				elif event.key == pygame.K_LEFT:
					self.ship.moving_left = False

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		pygame.display.flip()

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()