print("first: ", "vinay"[::-1])


def reverse_string(string):
    result = ''
    for i in range(len(string) - 1, -1, -1):
        result += string[i]
    return result


def reverse_string2(string):
    reversed_str = ''
    for char in string:
        reversed_str = char + reversed_str
    return reversed_str


if __name__ == '__main__':
    print("second: ", reverse_string("haryan"))
    print("third: ", reverse_string2("vinay"))
