#freq.py
from collections import defaultdict

num_list = input().split()
freq = defaultdict(int)

for num in num_list:
	freq[num] += 1

for k, v in freq.items():
	print(k, " : ", v)