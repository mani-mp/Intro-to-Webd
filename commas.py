#commas.py
import sys

def add_comma(number, pos):
	if abs(pos) >= len(number):
		return
	number.insert(pos, ',')
	add_comma(number, pos-4)

with sys.stdin as f:
	data = []
	for i in range(5):
		data.append(list(f.readline()))
	for number in data:
		add_comma(number, -4)

for number in data:
	print(''.join(number))