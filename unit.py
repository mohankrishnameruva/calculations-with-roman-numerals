from romanoperations import romantoarabic,arabictoroman
import unittest
class SimpleTest(unittest.TestCase):
	"""docstring for SimpleTest"""
	def testromantoarabic(self):
		self.assertEquals(romantoarabic('X'),10)
		self.assertEquals(romantoarabic('XCIX'),99)
		self.assertEquals(romantoarabic('LIV'),54)
	def testarabictoroman(self):
		self.assertEquals(arabictoroman(10),'X')
		self.assertEquals(arabictoroman(99),'XCIX')
		self.assertEquals(arabictoroman(54),'LIV')
if __name__ =='__main__':
	unittest.main()
