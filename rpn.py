#!/usr/bin/env python3

import operator
import readline
from prettytable import PrettyTable

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow
}


def calculate(arg):
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			result = operator_fn(arg1, arg2)
			
			stack.append(result)
	return stack.pop()

def main():
	b = 3 * 3
	table = PrettyTable(['Operator','Function'])
	table.add_row(['+','Addition'])
	table.add_row(['-','Subtraction'])
	table.add_row(['*','Multiplication'])
	table.add_row(['/','Divison'])
	table.add_row(['^','Exponentiation'])
	print(table)
	while True:
		result = calculate(input('rpn calc> '))
		print("Result:", result)

if __name__ == '__main__':
	main()
