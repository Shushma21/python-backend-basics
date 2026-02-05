def divide_numbers(a,b):
	try:
		result = a/b
		return result
	except ZeroDivisionError:
		return "Cannot divide by zero"
	except TypeError:
		return "Invalid input type"
	finally:
		("operation completed")




print(divide_numbers(10,4))
print(divide_numbers(10,0))
print(divide_numbers(1,"a"))
