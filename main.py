from src.str2digital import transform_numbers
from src.parse_input import verify_input
from src.parse_input import str2list


if __name__ == '__main__':
    while True:
        print('Type an input and press ENTER')
        text_input = input()
        validated_input = verify_input(text_input)
        arg_lists = str2list(validated_input)
        size = int(arg_lists[0])
        expression = arg_lists[1]
        transform_numbers(size, expression)
        if len(arg_lists) > 2:
            exit()
