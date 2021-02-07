def sum_eo(n, t):
    sum = 0
    for char in t:
        if char == 'e':
            for i in range(2, n, 2):
             sum += i
            return sum
        elif char == 'o':
            for i in range(2, n, 2):
                sum += i
            return sum
    return -1
x = sum_eo(11, 'spam')
print(x)