# -*- coding: utf-8 -*-
morse_table = dict({
	'=.===': 'a',
	'===.=.=.=': 'b',
	'===.=.===.=': 'c',
	'===.=.=': 'd',
	'=': 'e',
	'=.=.===.=': 'f',
	'===.===.=': 'g',
	'=.=.=.=': 'h',
	'=.=': 'i',
	'=.===.===.===': 'j',
	'===.=.===': 'k',
	'=.===.=.=': 'l',
	'===.===': 'm',
	'===.=': 'n',
	'===.===.===': 'o',
	'=.===.===.=': 'p',
	'===.===.=.===': 'q',
	'=.===.=': 'r',
	'=.=.=': 's',
	'===': 't',
	'=.=.===': 'u',
	'=.=.=.===': 'v',
	'=.===.===': 'w',
	'===.=.=.===': 'x',
	'===.=.===.===': 'y',
	'===.===.=.=': 'z'
})

t = int(input())

for i in range(t):
	result = []
	morse_code = input()
	morse_words = morse_code.split('.......')
	for morse_word in morse_words:
		word = ''
		for morse_letter in morse_word.split('...'):
			word += morse_table[morse_letter]
		result.append(word)
	print(' '.join(result))
