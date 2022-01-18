import unittest
from forest import Frame

class TestFrame(unittest.TestCase):
	def test_line(self):
		frame = Frame(['cat','doggy'],'*')
		self.assertEqual(len(frame.getLine()),9)
		self.assertEqual(frame.getContent().find('cat'),2)
		self.assertEqual(frame.totalHeight, len(frame.content)+2)
		self.assertEqual(frame.content[1], 'doggy')
