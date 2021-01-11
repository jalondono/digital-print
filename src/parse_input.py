import re


def verify_input(text_input: str) -> str:
    """
    Verify the input has a correct form
    :param text_input:
    :return: a list with size, expression and extra args or None
    """
    pattern = '\s*[0-9],[0-9]*\s*(0,0)?\s*'
    fullmatch = re.fullmatch(pattern, text_input)
    if fullmatch:
        return fullmatch.string
    raise ValueError('The format input is incorrect, Should be as follow: \n <size>,<number>')


def str2list(valid_input: str) -> list:
    """
    Convert a valid str into a list
    :param valid_input:
    :return:
    """
    output_list = []
    input_list = valid_input.split()
    # adding size
    str_number = input_list.pop(0)
    number_list = str_number.split(',')
    number_list.extend(input_list)

    return number_list
