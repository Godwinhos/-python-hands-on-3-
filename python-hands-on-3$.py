meals = ["Gwote", "Masa", "Tuwon Acha", "Fura da Nono", "Kunu", "Miyan Kuka"]
print(meals)
#manager want miyan taushe to be added
meals.insert(4, "miyan taushe")
print(meals)

#masa wont be available
meals.remove(meals[1])
print(meals)

#a meal has to be move
meals.pop(3)
meals.append("fura da nono")
print(meals)

#manager need to know what is centre of the list
print(meals[2])
