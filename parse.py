#!/usr/bin/python

def seed(markup):
	element_index = markup.rindex('a href')
	return markup[markup.index('>',element_index) + 1
		: markup.index('<',element_index)]

def puzzle(markup):
	puzzle_dict = {}
	for x in range(9):
		for y in range(9):
			name = str(x) + '.' + str(y)
			puzzle_dict[name] = value(markup, name)
	return puzzle_dict

def answer(markup):
	answer_dict = {}
	x, y = (0, 0)
	for line in markup.split('\n'):
		try:
			index = line.index('</td>')
			try:
				index = line.rindex('</b>', 0, index)
			except: pass
			name = str(x) + '.' + str(y)
			answer_dict[name] = line[line.rindex('>', 0, index) + 1 : index]
			x += 1
			if x > 8:
				y += 1
				x = 0
		except: pass
	return answer_dict

def value(markup, name):
	name_index = markup.index('name="%s"' % name)
	element = markup[markup.rindex('<',0,name_index) + 1
		: markup.index('>',name_index)]
	value_index = element.index('value="') + 7
	return element[value_index : element.index('"', value_index)]

def format(puzzle_dict):
	puzzle_string = ''
	for y in range(9):
		line = []
		for x in range(9):
			name = str(x) + '.' + str(y)
			line.append(puzzle_dict[name])
		puzzle_string += '\t'.join(line) + '\n'
	return puzzle_string
