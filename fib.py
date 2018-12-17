#fib.py

n = int(input())
a = 0
b = 1

if n > 0:
	print(a)
if n > 1:
	print(b)

while n > 2:
	print(a+b)
	a, b = b, a+b
	n -=1