list1 = [4, 5, 100, 105, 109, 110, 125, 135, 142, 146, 150, 155, 165, 168, 172, 178, 180, 190, 200, 205, 300, 306]
min_val = 100
max_val = 200
# for index in range(len(list1) - 1, -1, -1):
#     if list1[index]< min_val or list1[index]> max_val:
#         del[list1[index]]

for index, value in enumerate(reversed(list1)):
    print(index, value)

print(list1)