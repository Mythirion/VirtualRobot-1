import Entity
import pygame
import Tile
import client
import Keyboard
import random


class RobotAI(Entity.Entity):

	
	def __init__(self,level, x, y):
		super(RobotAI,self).__init__(level,x,y)
		self.x = x
		self.y = y
		self.isSwimming = False
		self.isMoving = False
		self.img = pygame.image.load("robot.png")
		self.basicFont = pygame.font.SysFont(None, 32)
		self.path = None

	def hasCollided(self,xa, ya):
		return False
		xMin = 32
		xMax = 38
		yMin = 48
		yMax = 60
		
		
		for x in range(xMin,xMax):
			if self.isSolidTile(xa, ya, x, yMin):
				return True
		
		for x in range(xMin,xMax):
			if self.isSolidTile(xa, ya, x, yMax):
				return True

		for y in range(yMin,yMax):
			if self.isSolidTile(xa, ya, xMin, y):
				return True

		for y in range(yMin,yMax):
			if self.isSolidTile(xa, ya, xMax, y):
				return True
		return False
	

	
	def tick(self):
		global x,y
                super(RobotAI,self).tick()
		xa = 0
		ya = 0
		self.centreX= self.x+31
		self.centreY= self.y+63
		xx = self.centreX >>5
		yy = self.centreY >>5
		

		if self.ticks%20==0:
			self.path = self.level.findPath((xx,yy),(self.level.player.centreX>>5,self.level.player.centreY>>5))
		
		if self.path != None:
			if len(self.path) > 0 :
				pos = self.path[len(self.path)-1].pos
				
				if xx < pos[0]:
					xa=1
				if yy < pos[1]:
					ya=1
				if xx > pos[0]:
					xa=-1
				if yy > pos[1]:
					ya=-1
			else:
				print "You have arived!"
			



		if xa != 0 or ya != 0:
			self.isMoving = not self.move(xa, ya)
		else:
			self.isMoving = False
		
		if self.isMoving:
			client.move(self.x,self.y)

		if self.getTileUnder().getId() == Tile.water.getId():
			self.isSwimming = True
		else:
			self.isSwimming = False

	

	def render(self,screen,xoff,yoff):
		
                if self.isSwimming:
                        source_area = pygame.Rect((0,0), (self.img.get_width(), self.img.get_height()/2))
                        screen.blit(self.img,(self.x-xoff+16,self.y-yoff+32),source_area)
                else:
                        screen.blit(self.img, (self.x-xoff+16,self.y-yoff))
   	 

