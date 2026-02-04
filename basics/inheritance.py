class  car:
	def __init__(self,brand,color):
		self.brand = brand
		self.color = color

	def drive(self):
		print("car is driving")


class ElectricCar(car):
	def  __init__(self,brand,color,capacity):
		super().__init__(brand,color)     #super() calls the parent class constructor
		self.capacity = capacity
	def battery(self):
		print("car brand is ",self.brand)
		print("car color is",self.color)
		print("car capacity is",self.capacity,"people")


value = ElectricCar("KN","Black",5)
value.drive()
value.battery()
