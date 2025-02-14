#!/usr/bin/python
#. : | △ - □ O

pn = {
	'.': 1,
	':': 2,
	'|': 3,
	'△': 9,
	'-': 12,
	'□ ': 48,
	'o': 60,
}

banner = f"""

###	██████╗ ██╗   ██╗██████╗  █████╗ ███╗   ███╗██╗██████╗ 	###
###	██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗████╗ ████║██║██╔══██╗	###
###	██████╔╝ ╚████╔╝ ██████╔╝███████║██╔████╔██║██║██║  ██║	###
###	██╔═══╝   ╚██╔╝  ██╔══██╗██╔══██║██║╚██╔╝██║██║██║  ██║	###
###	██║        ██║   ██║  ██║██║  ██║██║ ╚═╝ ██║██║██████╔╝	###
###	╚═╝        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═════╝ 	###
###	███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗  	###
###	████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗ 	###
###	██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝ 	###
###	██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗ 	###
###	██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║ 	###
###	╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝ 	###
###	███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗  	###
###	██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║  	###
###	███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║  	###
###	╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║  	###
###	███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║  	###
###	╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝  	###

	{'\t'.join(map(str, pn.keys()))}
	{'\t'.join(map(str, pn.values()))}

Usage:
- Each symbol represents a specific value.
- The symbol 'O' (60) can be multiplied by 
	the sum of other symbols to the left.
- For example:
	'|.O'	→	(3 + 1) * 60	 = 240
	:OO||	→	 2 * 60 * 60 + 6 = 7206
	-|||o-|o=:o-|o-|||: → -△ o-|o=:o-|o-◬ . → 275494523
"""

import time
import readline
import random as rnd

# Dictionary to store base 60 symbols and their corresponding values
n = {
	'.': 1,
	':': 2,
	'|': 3,
	'△ ': 9,
	#'◬ ': 10,
	'▲ ': 10,
	'-': 12,
	'=': 24,
	'☰': 36,
	'□ ': 48,
	'o': 60,
}

# Reverse dictionary for converting numbers back to symbols
reverse_n = {v: k for k, v in n.items()}

def sym2num(symbols):
	# """Convert base-60 symbols to a number based on custom notation."""
	# symbols = symbols.lower().replace('0', 'o')
	# num = 0
	# multiplier = 1
	
	# for i in reversed(symbols):
	# 	if i == 'o':
	# 		num += 60 * multiplier
	# 		multiplier = 1
	# 	else:
	# 		num += n[i] * multiplier
	# return num
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
	num_o = number // 60
	number %= 60

	if num_o > 0:
		symbols.append('o ')
		if num_o > 1:
			symbols.insert(0, num2sym(num_o))

	# Use a sorted list of symbol counts to build the representation.
	symbol_counts = sorted(((value, symbol) for symbol, value in n.items() if symbol != 'o' and value < 60), reverse=True)
	for value, symbol in symbol_counts:
		count = number // value
		number -= count * value
		if count > 0:
			symbols.append(symbol * count)
			number %= value

	# Handle remaining values
	if number == 2:
		symbols.append(':')  # Use ':' for exactly 2
	elif number > 0:
		symbols.append('.')  # Use '.' for any remaining value greater than 0 but less than 2

			
	return ''.join(symbols)

def main():
	while True:
		try:
			user_input = input("> ")
			
			if user_input.lower() in ['exit', 'quit', 'e', 'q']:
				break

			c = dict.fromkeys(n, 0)

			if user_input.lower() in ['h', 'help']:
				print(banner)
				continue

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
	
			# Check if input is a digit (number)
			if user_input.isdigit():
				num = int(user_input)
				conv = num2sym(num)
				print('\t',end='')
			else:
				try:
					res = eval(user_input)
					conv = num2sym(res)
					print('\t',end='')
				except:
					# Otherwise, treat it as symbols
					conv = sym2num(user_input.replace(' ',''))
			print(f"  {conv}")
			
		# except ValueError as e:
		except Exception as e:
			print(e)

print(banner)

try:
	main()
except KeyboardInterrupt:
    print("Program interrupted by user.")
    
