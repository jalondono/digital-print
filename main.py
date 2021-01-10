print_digits = __import__('str2digital').transform_numbers


if __name__ == '__main__':
    while True:
        expression = input()
        size = 3
        print(expression)
        print_digits(size, expression)
        print()
