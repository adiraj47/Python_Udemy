""" This program will delete items only from a sorted lists"""
list1 = [4, 5, 100, 105, 109, 110, 125, 135, 142, 146, 150, 155, 165, 168, 172, 178, 180, 190, 200, 205, 300, 306]
max_val = 200
min_val = 100
stop = -1
#to delete the small elements
for index, value in enumerate(list1):
    if value >= min_val:
        stop = index
        break
print(stop)
if stop != -1:
    del list1[:stop]
print(list1)
#to delete the larger elements
stop = -1
for index, value in enumerate(list1):
    if value >= max_val:
        stop = index +1
        break
print(stop)
if stop != -1:
    del list1[stop:]
print(list1)
