#import random.py


TAKEN = "+"
FREE = " "
START = "S"
FINISH = "F"


class Maze:
	sectors
	sectorWidth
	sectorHeight
	
	map
	start
	end
	
	def init:
		self.sectors = 3
		self.sectorWidth = 5
		self.sectorHeight = 5
		
		self.map = []
		cols = self.sectors * (self.sectorWidth * 2)
		for col in range(0, cols):
			self.map.append([])
