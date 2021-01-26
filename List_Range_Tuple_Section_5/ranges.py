demcimals = range(0,100)
My_ranges = demcimals[3: 40: 3]
range1 = range(3,40,3)
print(My_ranges == range1)
print(range(0, 5, 2) == range(0, 6, 2))
r = range(0, 100)
for i in r[::-2]:
    print(i)
print('-'*50)
for i in range(100,0,-2):
    print(i)
