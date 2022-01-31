class Frame:
    def __init__(self, content, border_character, space=' '):
		self.content = content
		self.border_character = border_character
		self.space = space
		self.up_down_lines_height = 2
		self.width_spaces_lines = 4
		self.total_width = len(max(content, key=len)) + self.width_spaces_lines
		self.total_height = len(content) + self.up_down_lines_height
		self.new_line_for_linux = '\n'
		self.last_line = self.total_height - 3

    def get_line(self):
        return self.border_character * self.total_width

	def set_spaces(self, line):
		return self.space*(self.total_width - 3 - (len(self.content[line])))

	def set_content_line(self, line):
		return self.border_character + self.space + self.content[line]
                + self.set_spaces(line) + self.border_character

	def get_content(self):
		content = str()
		for line in range(self.total_height - self.up_down_lines_height):
			if line == self.last_line:
				content += self.set_content_line(line)
			else:
				content += self.set_content_line(line) + self.new_line_for_linux

		return content

	def __str__(self):
		return self.new_line_for_linux.join((self.get_line(), self.get_content(),
                                             self.get_line()))

	def __repr__(self):
		return self.new_line_for_linux.join((self.get_line(), self.get_content(),
                                             self.get_line()))
	
