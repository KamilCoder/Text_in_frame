class Frame:
	def __init__(self, content, borderCharacter, space = ' '):
		self.content = content
		self.borderCharacter = borderCharacter
		self.space = space
		self.upDownLinesHeight = 2
		self.widthSpacesAndLines = 4
		self.totalWidth = len(max(content,key=len))+self.widthSpacesAndLines
		self.totalHeight = len(content)+self.upDownLinesHeight
		self.newLineForLinux='\n'

	def getLine(self):
		return self.borderCharacter*self.totalWidth

	def setSpaces(self, line):
		return self.space*(self.totalWidth -3 -(len(self.content[line])))

	def setContentLine(self, line):
		return self.borderCharacter + self.space + self.content[line]+ self.setSpaces(line) +self.borderCharacter

	def getContent(self):
		content = str()
		for line in range(self.totalHeight-self.upDownLinesHeight):
			if line == self.totalHeight-3:
				content+=self.setContentLine(line)
			else:
				content+=self.setContentLine(line)+self.newLineForLinux

		return content

	def __str__(self):
		return self.newLineForLinux.join((self.getLine(),
										self.getContent(),
										self.getLine()))

	def __repr__(self):
		return self.newLineForLinux.join((self.getLine(),
										self.getContent(),
										self.getLine()))
