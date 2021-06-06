#!/usr/bin/python3
import sys, random

def factorial(n):
	r=1
	for i in range(1,n+1):
		r *= i
	return r

text = ""
if len(sys.argv) == 2:
	text = sys.argv[1]
else:
	text = input("Text: ")
#brute-force approach
n = len(text)
t = list(text)
p = factorial(n)

permutations = []
permutations.append(''.join(t))

while len(permutations) < p:
	random.shuffle(t)
	text = ''.join(t)
	if text not in permutations:
		print(text)
		permutations.append(text)

print("")
print("Final Permutations")
print(sorted(permutations))
