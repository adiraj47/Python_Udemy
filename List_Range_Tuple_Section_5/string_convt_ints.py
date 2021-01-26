str_values = ["1", "2", "3", "4"]
int_value = []
for value in str_values:
    temp = int(value)
    int_value.append(temp)
print(int_value)
for index in range(len(str_values)):
    str_values[index] = int(str_values[index])
print(str_values)