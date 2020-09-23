import argparse
from grammar import *
import numpy as np

code = None
id_table = {}
n_id = 0
const_list = []
tokens = []
line = 1
next_char = ' '

def parse_args():
	""" Setup the input and output arguments for the script
	Return the parsed input and output files
	"""
	parser = argparse.ArgumentParser(description = 'Lexical Analysis')
	parser.add_argument('infile',
						type = argparse.FileType('r'),
						help = 'SSL file to be analyzed')
	parser.add_argument('outfile',
						type = argparse.FileType('w'),
						help = 'Output numpy file with tokens')
	return parser.parse_args()


def search_keyword(name):
	if name in reserved_words:
		return reserved_words[name]
	return Words.ID


def search_name(name):
	if name not in id_table:
		global n_id
		id_table[name] = n_id
		n_id += 1
	return id_table[name]


def add_const(const):
	if const not in const_list:
		const_list.append(const)
	return const_list.index(const)


def get_const(n):
	if (n > 0) and (n < len(const_list)):
		return const_list[n]
	return -1


def next_token():
	global next_char
	global line

	while next_char in ignored_chars:
		if next_char == '\n' or next_char == '\r':
			line += 1
		next_char = code.read(1)

	if next_char == '':
		token = Words.EOF
	elif next_char.isalpha():
		text = ''
		while next_char.isalpha() or next_char == '_': 
			text += next_char
			next_char = code.read(1)
		token = search_keyword(text)
		if token == Words.ID:
			token_sec = search_name(text)
	elif next_char.isdigit():
		numeral = ''
		while next_char.isdigit():
			numeral += next_char
			next_char = code.read(1)
		token = Words.NUMERAL
		token_sec = add_const(numeral)
	elif next_char == '"':
		string = ''
		while next_char != '"' and string != '':
			string += next_char
			next_char = code.read(1)
		string += '"'
		token = Words.STRINGVAL
		token_sec = add_const(string)
	elif next_char == '\'':
		next_char = code.read(1)
		token = Words.CHARACTER
		token_sec = add_const(next_char)
		next_char = code.read(1) # skip '
		next_char = code.read(1)
	elif next_char == '+':
		next_char = code.read(1)
		if (next_char == '+'):
			token = Words.PLUS_PLUS
			next_char = code.read(1)
		else:
			token = Words.PLUS
	elif next_char == '-':
		next_char = code.read(1)
		if next_char == '-':
			token = Words.MINUS_MINUS
			next_char = code.read(1)
		else:
			token = Words.MINUS
	elif next_char == '>':
		next_char = code.read(1)
		if next_char == '=':
			token = Words.GREATER_OR_EQUAL
			next_char = code.read(1)
		else:
			token = Words.GREATER_THAN
	elif next_char == '<':
		next_char = code.read(1)
		if next_char == '=':
			token = Words.LESS_OR_EQUAL
			next_char = code.read(1)
		else:
			token = Words.LESS_THAN
	elif next_char == '=':
		next_char = code.read(1)
		if next_char == '=':
			token = Words.EQUAL_EQUAL
			next_char = code.read(1)
		else:
			token = Words.EQUALS
	elif next_char == '!':
		next_char = code.read(1)
		if next_char == '=':
			token = Words.NOT_EQUAL
			next_char = code.read(1)
		else:
			token = Words.NOT
	elif next_char == '|':
		next_char = code.read(1)
		if next_char == '|':
			token = Words.OR
			next_char = code.read(1)
		else:
			token = Words.UNKNOWN
	elif next_char == '&':
		next_char = code.read(1)
		if next_char == '&':
			token = Words.AND
			next_char = code.read(1)
		else:
			token = Words.UNKNOWN
	elif next_char in [':', '[', ']', '{', '}', '(', ')', ';', ', ', '.', '/', '*']:
		token = symbols[next_char]
		next_char = code.read(1)
	else:
		token = Words.UNKNOWN

	tokens.append(token)
	if token in regular_tokens:
		tokens.append(token_sec)
	return token


def LexError(token):
	if token == Words.UNKNOWN:
		print('Unexpected character in line ' + str(line))
		return True
	return False


def lexical_analysis(input_file, output_file):
	global code
	try:
		code = open(input_file, 'r')
	except:
		exit()

	token = next_token()
	error = False
	while token != Words.EOF:
		if LexError(token):
			error = True
		token = next_token()
		
	for t in tokens:
		print(t)
	np.save(output_file, tokens)
	code.close()

	if not error:
		print('\nNo lexical errors\n')

if __name__ == '__main__':
	args = parse_args()
	lexical_analysis(args.infile.name, args.outfile.name)