class Frame:
	def __init__(self, content, borderCharacter, space = ' '):
		self.content = content
		self.borderCharacter = borderCharacter
		self.space = space
		self.width = len(max(content,key=len))+4
		self.height = len(content)+2

	def showLine(self):
		return self.borderCharacter*self.width

	def showContent(self):
		content = str()
		for h in range(self.height-2):
			if h < self.height-3:
				content+=(self.borderCharacter+self.space+self.content[h]+(self.space*(self.width-3-(len(self.content[h]))))+self.borderCharacter+'\n')
			elif h < self.height-2:
				content+=(self.borderCharacter+self.space+self.content[h]+(self.space*(self.width-3-(len(self.content[h]))))+self.borderCharacter)
		return content

	def __str__(self):
		return '\n'.join((self.showLine(),self.showContent(),self.showLine()))

	def __repr__(self):
		return '\n'.join((self.showLine(),self.showContent(),self.showLine()))
