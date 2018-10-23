def city_functions(city, country, population = 0):
	if population:
		return city + ', ' + country + ' - population ' + str(population)
	else:
		return city + ', ' + country


