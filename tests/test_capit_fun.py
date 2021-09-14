import unittest
from capitalizer import capit

class CapitTaster(unittest.TestCase):
	
	def test(self):
		self.assertEqual(capit('hello world!'), 'HELLO WORLD!')
		self.assertEqual(capit('having fun'), 'HAVING FUN')

if __name__ == '__main__':
	unittest.main()
