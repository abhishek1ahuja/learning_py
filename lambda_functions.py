cities = ['Chennai', 'Bangalore', 'Delhi', 'bombay', 'mangalore', 'hubli', 'coimbatore']

cities_bop = [city + "_bop" for city in cities]
print(cities_bop)

#similarly for numbers

temp = [17, 20, 15, 17, 16, 12, 20]
temp_cut2 = [t - 2 for t in temp]
print("temp \t\t\t:", temp)
print("temp_cut2\t\t:", temp_cut2)
