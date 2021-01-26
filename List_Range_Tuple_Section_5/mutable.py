shopping_list = ["milk","fruits","vegitables"]
another_shopping_list = shopping_list
print(id(shopping_list))
print(id(another_shopping_list))
shopping_list += "spam"
print(id(shopping_list))
a = b = c = d = e = f = another_shopping_list
print("adding cream")
b.append("cream")
print(a)
print(shopping_list)