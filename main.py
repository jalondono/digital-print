print_digits = __import__('str2digital').transform_numbers


if __name__ == '__main__':
    size = 4
    expression = '0123456789'
    print_digits(size, expression)
    print()
