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
    if "spam" not in meal:
        print(meal)
        for item in meal:
            print(item)
    else:
        print("{0} has a spam score of {1}"
              .format(meal, meal.count("spam")))