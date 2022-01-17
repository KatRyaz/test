class Street():

	def __init__(self, snumber):
		self.snumber = snumber

	def street_name(self):
		self.name = "Groove"
		return f"{self.name} street, "

	def show_info(self):
		print(f"{self} находится на {self.street_name()}{self.snumber}")

class Shop(Street):
	def __str__(self):
		return "Магазин"

	def iteraction(self, iteraction):
		self.iteraction = iteraction
		print(f"Персонаж купил {self.iteraction} в магазине")

class Mail(Street):
	def __str__(self):
		return "Почта"

	def iteraction(self, iteraction):
		self.iteraction = iteraction
		print(f"Персонаж получил {self.iteraction} на почте")


class Police(Street):

	def __str__(self):
		return "Полицеский отдел"

	def iteraction(self, iteraction):
		self.iteraction = iteraction
		print(f"Персонаж подал заявление на {self.iteraction} в полицейском отделе")

class House1(Street):

	def __str__(self):
		return "Первый дом"

	def iteraction(self, iteraction):
		self.iteraction = iteraction
		print(f"В первом доме живет {self.iteraction} человек")

	def __iadd__(self, other):
		self.iteraction += other.iteraction
		return self.iteraction


class House2(Street):

	def __str__(self):
		return "Второй дом"

	def iteraction(self, iteraction):
		self.iteraction = iteraction
		print(f"Во втором доме живет {self.iteraction} человек")

	def __iadd__(self, other):
		self.iteraction += other.iteraction
		return self.iteraction

class Restaurant(Street):

	def __str__(self):
		return "Ресторан"

	def iteraction(self, iteraction):
		self.iteraction = iteraction
		print(f"Персонаж заказал {self.iteraction} в ресторане")

class Club(Street):

	def __str__(self):
		return "Клуб"

	def iteraction(self, iteraction):
		self.iteraction = iteraction
		print(f"Персонаж заказал песню {self.iteraction} в клубе")