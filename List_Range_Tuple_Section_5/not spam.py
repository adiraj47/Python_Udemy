menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "bacon", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "egg", "bacon", "spam"]
]
for meal in menu:
    for item in meal:
        if "spam" not in item:
            print(item, end=", ")
    print()
for meal in menu:
    for item in range(len(meal) - 1, -1, -1):
        if meal[item] == "spam":
            del meal[item]
    print(", ".join(meal))
