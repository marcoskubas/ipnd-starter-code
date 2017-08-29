# Lesson 2.6: For Loops

# For loops, like while loops, are useful for running a block of code
# multiple times. For loops make iterating through elements in a list
# easier than using a while loop.

# https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4152219158/concepts/50309288180923

def print_all_elements(p):
    for e in p:
        print e

myList = [1, 2, [3, 4]]
print_all_elements(myList)

# Add your own code and notes here
def measure_udacity(p):
	count = 0
	for e in p:
		if e[0] == 'U':
			count += 1
	return count

print measure_udacity(['Katy', 'Marcos'])
print measure_udacity(['Uncle', 'Ursula'])

def find_element(lista, value):
	i = 0
	while i < len(lista):
		if lista[i] == value:
			return i
		i += 1
	return -1

def find_element_for(lista, value):	
	i = 0
	for e in lista:
		if e == value:
			return i
		i += 1
	return -1

def find_element_index(lista, value):	
	if value in lista:
		return lista.index(value)
	return -1

print find_element([1,2,3], 3)
print find_element_index([1,2,3], 3)
print find_element_index([1,2,3], 4)

def union(lista1, lista2):
	for e in lista2:
		if e not in lista1:
			lista1.append(e)

a = [1,2,3]
b = [2,4,6]
union(a,b)
print a 			