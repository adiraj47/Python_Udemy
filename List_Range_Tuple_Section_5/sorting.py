pangram = "The  quick brown fox jumps over the lazy dog"
letters = sorted(pangram, key=str.casefold)
print(letters)
names = ["Aditya", "Prats", "twinkle", "haddi", "saloni"]
names.sort(key=str.casefold)
print(names)