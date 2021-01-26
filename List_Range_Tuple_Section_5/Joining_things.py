#join only works on string data type but not on integer data type 
flowers = [
    "Daffodill",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger lily",
]
seprator = " | "
output = seprator.join(flowers)
print(output)