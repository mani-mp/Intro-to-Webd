#gcd.py

a = list(map(int, input().split()))
if a[1] > a[0]:
	a[0], a[1] = a[1], a[0]

while a[0]%a[1] != 0:
	a[0], a[1] = a[1], a[0]%a[1]

print(a[1])