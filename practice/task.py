
#class

#class product:
#    def __init__(self,name,price):
#        self.name = name
#        self.price = price

#    def item(self):
#       print("Item name :",self.name)
#        print("Item price:",self.price)

#value = product("Book","30")
#value.item()



#exceptions


def  age_validation():
	try : 
		age =int(input("enter your age:"))
		
		if age >= 18:
			print("Access granted.You are eligible")
		else : 
			print("Access denied. You must be 18 or older")
	except ValueError:
		print("Invalid input! Please enter a number")




age_validation()
