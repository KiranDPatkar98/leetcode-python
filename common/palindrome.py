string = input('Enter the string ? ')


def palindrome():
    return string == string[::-1]


print(palindrome())
