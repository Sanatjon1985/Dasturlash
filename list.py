import math
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print(thislist[0])
print("Assalomu alaykum")
print("245- guruh")
print(thislist[2])
massiv = [5,2,8,1,9,3]
max_element = max(massiv)
min_element = min(massiv)
max_index = massiv.index(max_element)
min_index = massiv.index(min_element)
massiv[max_index], massiv[min_index] = massiv[min_index], massiv[max_index]
print("natija:", massiv)