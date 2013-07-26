#!/usr/lib/python

import urllib, urllib2

url = "http://kjell.haxx.se/sudoku/"

def puzzleHtml(visade='33', seed='(random seed)'):
	data = urllib.urlencode({'visade':visade, 'seed':seed, 'action':'Create a field', 'hardchange':'0'})
	return urllib2.urlopen(url, data).read()

def answerHtml(seed, puzzle_dict):
	puzzle_dict['seed'] = seed
	puzzle_dict['action'] = 'Show solution'
	data = urllib.urlencode(puzzle_dict)
	return urllib2.urlopen(url, data).read()

def puzzleTable(html=puzzleHtml()):
	begin_index = html.index('<table border=0 cellspacing=0 cellpadding=0>')
	end_index = html.index('<input type=submit name=action value="Show solution"') - 1
	return html[begin_index:end_index]

def answerTable(html):
	begin_index = html.index('<table border=1 cellspacing=0 cellpadding=2>')
	end_index = html.index('<h1>Generate and Solve Sudoku</h1>') - 1
	return html[begin_index:end_index]
