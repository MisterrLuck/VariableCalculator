def title():
	print("Welcome to the varible calculator.")
	print("You can assign values to varibles\nusing the equal sign, '='.")
	print("All variables must only have one letter.")
	print("To quit, type 'quit' or use Ctrl + D.")
	print("To use normal operators, use this chart:")
	print("""
'+': Plus sign
'-': Minus sign
'*': Multiplication sign
'/': Division sign
'%': Modulo operator\n""")

def varCheck(string):
	if '=' in string:
		string = string.split('=')
		for i in range(len(string)):
			string[i] = string[i].replace(" ", "")

		if len(string[0]) == 1:
			return True
		return False
	elif '+' in string:
		string = string.split('+')
		for i in range(len(string)):
			string[i] = string[i].replace(" ", "")

		if len(string[0]) == 1:
			return True
		return False
	elif len(string) == 1:
		return True
	return False

def start():
	while 1:
		try:
			calc = input(">> ")
		except EOFError:
			print()
			break
		if calc.lower() == 'quit':
			break
		
		var = varCheck(calc)

		if not var:
			print(f"{red}Variable has to be one letter only.{clear}")
		else:
			try:
				exe = compile(calc, "line", "single")
				exec(exe)
			except:
				print(f"{red}Error!{clear}")

if __name__ == '__main__':
	red = "\033[1;31m"
	clear = "\033[0m"
	title()
	start()