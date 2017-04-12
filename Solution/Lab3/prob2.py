import math
import unittest

class InterfataShape (object):
	#def __init__(self, x):
		#raise NotImplementedError("Neimplementat")
	def aria(self):
		raise NotImplementedError("Neimplementat")

class Square(InterfataShape):
	def __init__ (self, latura):
		self._latura = latura
		
	@property
	def aria(self):
		return self._latura ** 2
	
class Circle(InterfataShape):
	def __init__(self, raza):
		self._raza = raza
		
	@property
	def aria(self):
		return math.pi * self._raza ** 2
	

class TestShape(unittest.TestCase):
	def test_square(self):
		self.assertEquals(Square(10).aria,100)
	def test_circle(self):
		self.assertEquals(Circle(1).aria,math.pi)