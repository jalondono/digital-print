print_digits = __import__('str2digital').transform_numbers
verify_input = __import__('parse_input').verify_input
str2list = __import__('parse_input').str2list


if __name__ == '__main__':
    while True:
        print('Type an input and press ENTER')
        text_input = input()
        validated_input = verify_input(text_input)
        arg_lists = str2list(validated_input)
        size = int(arg_lists[0])
        expression = arg_lists[1]
        print_digits(size, expression)
        if len(arg_lists) > 2:
            exit()

