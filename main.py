from py import Shop, Mail, House1, House2, Restaurant, Police, Club

shop = Shop(14)
mail = Mail(23)
police = Police(11)
house1 = House1(1)
house2 = House2(4)
restaurant = Restaurant(15)
club = Club(30)
shop.iteraction("Молоко")
mail.iteraction("Комплектующие для ПК")
police.iteraction("Владислав Киселёв")
house1.iteraction(4)
house2.iteraction(5)
restaurant.iteraction("Омлет с трюфелем")
club.iteraction("Twenty One Pilots - Heathens")
buildings = [shop, mail, police, house1, house2, restaurant, club]
for building in buildings:
	building.show_info()

house2 += house1
print(f"В общем в двух домах живут {house2} человек")

input()