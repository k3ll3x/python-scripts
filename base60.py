#!/usr/bin/python
#. : | - O

import time
import readline
import random as rnd

# Dictionary to store base 60 symbols and their corresponding values
n = {
	'.': 1,
	':': 2,
	'|': 3,
	'-': 12,
	'=': 24,
	'o': 60,
}

# Reverse dictionary for converting numbers back to symbols
reverse_n = {v: k for k, v in n.items()}

def sym2num(symbols):
	"""Convert base-60 symbols to a number based on custom notation."""
	symbols = symbols.lower().replace('0', 'o')  # Normalize input

	num = 0
	for i in symbols:
		if i != 'o':
			num += n[i]# if i in n else 0
		else:
			num = num * 60 if num != 0 else 60
	return num

def num2sym(number):
    """Convert a number to base 60 symbols based on custom notation."""
    if number < 1:
        raise ValueError("Number must be greater than or equal to 1.")
    
    symbols = []

    # Count how many O's (60) fit into the number
    count_O = number // n['o']
    number %= n['o']  # Reduce the number accordingly

    # Append 'O' for each 60 counted
    if count_O > 0:
        symbols.append('o')
        if count_O > 1:
            symbols.insert(0, num2sym(count_O))

    # Define a list of tuples for symbol values and their corresponding characters
    symbol_counts = [
        (n['='], '='), 
        (n['-'], '-'), 
        (n['|'], '|')
    ]

    # Handle multiples of 24 ('='), 12 ('-'), and 3 ('|')
    for value, symbol in symbol_counts:
        count = number // value
        number -= count * value
        if count > 0:
            symbols.append(symbol * count)

    # Handle remaining values
    if number == 2:
        symbols.append(':')  # Use ':' for exactly 2
    elif number > 0:
        symbols.append('.')  # Use '.' for any remaining value greater than 0 but less than 2

    return ''.join(symbols)


def main():
	while True:
		user_input = input("> ")
		
		if user_input.lower() in ['exit', 'quit', 'e', 'q']:
			break

		c = {
			'.': 0,
			':': 0,
			'|': 0,
			'-': 0,
			'=': 0,
			'o': 0,
		}

		if user_input.lower() in ['rand', 'random']:
			r = int(input("rand> "))
			for i in range(1,r+1):
				num = rnd.randint(1,r+1)
				sym = num2sym(num)
				print(f"{i}\t{num}\t{sym}")
				for k in c:
					c[k] += sym.count(k)
				#time.sleep(6/r)
			print(dict(sorted(c.items(), key=lambda item: item[1])))
			continue

		if user_input.lower() in ['r', 'range']:
			r = int(input("r> "))
			for i in range(1,r+1):
				print(f"{i}\t{num2sym(i)}")
				time.sleep(6/r)
			continue
		
		if user_input.lower() in ['t', 'test']:
			r = int(input("t> "))
			for i in range(1,r+1):
				sym = num2sym(i)
				num = sym2num(sym)
				if num != i:
					print(f"\tFailed: {i}\t{sym}")
					break
			print(f"\tAll {r} numbers passed!")
			continue
  
		if user_input.lower() in ['en', 'encode']:
			text = input("en> ")
			for i in [ord(char) - 96 for char in text.lower()]:
				print(num2sym(i), end=' ')
			print()
			continue

		if user_input.lower() in ['de', 'decode']:
			text = input("de> ").split(' ')
			for i in text:
				print(chr(sym2num(i) + 96), end='')
			print()
			continue
  
		try:
			# Check if input is a digit (number)
			if user_input.isdigit():
				num = int(user_input)
				conv = num2sym(num)
			else:
				try:
					res = eval(user_input)
					conv = num2sym(res)
				except:
					# Otherwise, treat it as symbols
					conv = sym2num(user_input.replace(' ',''))
			print(f"\t\t{conv}")
		
		except ValueError as e:
			print(e)

# Base 60 Symbols Representation
banner = """
\t\t.\t:\t|\t-\tO
\t\t1\t2\t3\t12\t60

Usage:
- Each symbol represents a specific value.
- The symbol 'O' (60) can be multiplied by the sum of other symbols to the left.
- For example:\n\t'|.O'\t→\t(3 + 1) * 60 = 240\n\t :OO||\t→\t2 * 60 * 60 + 6 = 7206
"""

print(banner)
main()