#abbr.py
import sys

with sys.stdin as f:
	data = []
	for i in range(4):
		data.append(f.readline())
	#print([lambda x: x + words[0] for words in sentences.split() for sentences in data])
	for sentences in data:
		for words in sentences.split():
			print(words[0], end='')
		print("")