import unittest
from forest import Frame

class TestFrame(unittest.TestCase):
	def test_line(self):
		frame = Frame(['cat','doggy'],'*')
		self.assertEqual(len(frame.showLine()),9)
		self.assertEqual(frame.showContent().find('cat'),2)
		self.assertEqual(frame.height, len(frame.content)+2)
		self.assertEqual(frame.content[1], 'doggy')
