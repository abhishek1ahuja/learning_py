from collections import deque
import numpy as np
# make a list
cities = ['Chennai', 'Bangalore', 'Delhi']
names = []
print(cities)

print("#" * 10 + "part 1.1")
line = ''
with open("cities.txt", 'r') as cities_file:
# for can iterate through all items in a collection
    for line in cities_file.readlines():
        # list method append, adds to the end of a list
        cities.append(line)
        print(cities)

#copying cities data into a cities queue
cities_queue = deque()
for city in cities:
    cities_queue.append(city)

print("\n" + "#" * 10 + "part 1.2")
#delete first 3 items from the list
for dummy in range(3):
    print("dummy: ", dummy)
    city_y = cities.pop()
    print("removing " + city_y)
    print("cities: ", cities)
print("cities after removing 3 items")
print(cities)
#NOTE THAT pop() removes elements at the end of the list

#removing elements at the beginning of the list
for i in range(3):
    print("removing " + cities_queue.popleft())
print("cities_queue after removing 3 items")
print(cities_queue)

print("\n" + "#" * 10 + "part 1.3")
# range(n) - values from 0 to n-1
# range(a, b) - values from a to b-1
# range(a, b, step) - values from a to b-1 in increments of step
range1 = [] #making an empty list
for i in range(10):
    range1.append(i)
print("range1: ", range1)

range2 = []
for jack in range(8, 19):
    range2.append(jack)
print("range2: ", range2)

range3 = []
for markey in range(20, 80, 7): # 7 is the step
    range3.append(markey)
print("range3: ", range3)

# # THIS DOES NOT WORK however - try it
# range4 = []
# for becca in range(4, 4.3, 0.018):
#     range4.append(becca)
# print("range4: ", range4)
# so we use a different version of range provided by numpy
range5 = []
for becca in np.arange(4, 4.3, 0.025):
    range5.append(np.round(becca, 3)) # why am I using round() here?
    # range5.append(becca) # why am I using round() here?
print("range5: ", range5)

