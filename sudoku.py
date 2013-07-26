#!/usr/bin/python

import sys, codecs, random
import get, parse, translate

try: visade = sys.argv[1]
except: visade = 'random'
if visade == 'random':
	visade = str(random.randint(17, 81)) #Difficulty not set, make random
if not 17 <= int(visade) <= 81:
	raise ValueError('Difficulty must be an integer between 17 and 81.')

try: trans_string = sys.argv[2].decode(sys.getfilesystemencoding())
except: trans_string = u'\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d'
if len(trans_string) < 9:
	raise ValueError('tras_string') # 'Translation string must be at least 9 characters.')

try: puzzle_seed = sys.argv[3]
except: puzzle_seed = '(random seed)'

puzzle_table = get.puzzleTable(get.puzzleHtml(visade, puzzle_seed))
answer_seed = parse.seed(puzzle_table)
puzzle_dict = parse.puzzle(puzzle_table)

answer_table = get.answerTable(get.answerHtml(answer_seed, puzzle_dict))
answer_dict = parse.answer(answer_table)

header = 'Puzzle Seed: ' + answer_seed + '\t\tCharacters: ' + trans_string
translated_puzzle = translate.translate(parse.format(puzzle_dict), trans_string)
translated_answer = translate.translate(parse.format(answer_dict), trans_string)

print
print header
print
print translated_puzzle
print
print translated_answer

#with codecs.open('Puzzles', 'a', encoding='utf-8') as f:
#	f.write(translated_puzzle)
#with codecs.open('Answers', 'a', encoding='utf-8') as f:
#	f.write(translated_answer)
