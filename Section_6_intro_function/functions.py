def multiply(x, y):
    """
    Function multiply is used to multiply two variables together containing the digits.

    :param x: input type is digit(int, float)
    :param y: input type is digit(int, float)
    :return: returns the result variable which holds the value of the multiplication of two digits
    """
    result = x * y
    return result

def is_palindrome(str1):
    """
    It is used to check whether the given string is a palindrome or not.

    :param str1: the `string` is passed here
    :return: Either true or false is returned if given string is palindrome or not
    """
    # backward = str1[::-1]
    # return backward == str1
    return str1.casefold() == str1[::-1].casefold()

def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
           string += char
    is_palindrome(string)

    return string.casefold() == string[::-1].casefold()
word = input("Enter the string value: ")
if palindrome_sentence(word):
    print("'{0}' is a palindrome".format(word))
else:
    print("'{0} is not a palindrome".format(word))

answer = multiply(5, 6)
print(answer)
print()
answer = multiply(5.1, 6.7)
print(answer)
print("=" * 50)
for value in range(1, 5):
    two_times = multiply(2, value)
    print(two_times)
