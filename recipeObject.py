class Recipe:
	def __init__ (self, name, serves):
		print("Constructor / init method")
		self.name = name
		self.serves = serves

	def ingredients(self):
		print("Ingredients for ", self.name, " ... serves", self.serves)
	def method(self):
		print("Method for ", self.name, " ...")

def main():

	omelette = Recipe("omelette", 6)

	omelette.ingredients()
	omelette.method()

	pancake = Recipe("Pancake", 4)

	pancake.ingredients()
	pancake.method()

if __name__ == "__main__" :
	main()
