empty_list = []
even= [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]
empty_list = even + odd
all_no = sorted(empty_list)
print(all_no)
even.extend(odd)
print(even)
even.sort(reverse= True)
print(even)
digits = '840173965'
digits = sorted("804571965")
print(digits)
more_digits = empty_list[:]
print(more_digits == empty_list)