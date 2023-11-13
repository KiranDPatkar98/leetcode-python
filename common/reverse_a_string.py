x = input('Please enter the string ? ')

# using slicing


def reverse_string():
    return x[::-1]


def reverse_string_loop():
    reversed_string = ''
    for char in x:
        reversed_string = char + reversed_string
    return reversed_string


print(reverse_string_loop())
