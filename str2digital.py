import numpy as np
def get_segment_setup(number: int) -> dict:
    """
    Extract a setup from a dict that contain the setup for any number
    :param number: Digit to print
    :return: a dictionary with the setup
    """
    segments = {
        0: {'a': 1, 'b': 1, 'c': 1, 'd': 0, 'e': 1, 'f': 1, 'g': 1},
        1: {'a': 0, 'b': 0, 'c': 1, 'd': 1, 'e': 0, 'f': 1, 'g': 0},
        2: {'a': 1, 'b': 0, 'c': 1, 'd': 1, 'e': 1, 'f': 0, 'g': 1},
        3: {'a': 1, 'b': 0, 'c': 1, 'd': 1, 'e': 0, 'f': 1, 'g': 1},
        4: {'a': 0, 'b': 1, 'c': 1, 'd': 1, 'e': 0, 'f': 1, 'g': 0},
        5: {'a': 1, 'b': 1, 'c': 0, 'd': 1, 'e': 0, 'f': 1, 'g': 1},
        6: {'a': 1, 'b': 1, 'c': 0, 'd': 1, 'e': 1, 'f': 1, 'g': 1},
        7: {'a': 1, 'b': 0, 'c': 1, 'd': 0, 'e': 0, 'f': 1, 'g': 0},
        8: {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1},
        9: {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 0, 'f': 1, 'g': 0},
    }
    return segments[number]


def convert2integers(digits: str) -> list:
    """
    convert string to integer list
    :param digits: strings list with the numbers
    :return: integer list
    """
    validate_list = []
    for digit in digits:
        validate_list.append(int(digit))
    return validate_list


def print_digits(size: int, expression: str):
    """
    Print a sequence of numbers into 7 segments display way
    :param size: Graphical size of digits
    :param expression: string with the numbers to print
    :return:
    """
    hor_symbol = '-'
    ver_symbol = '|'
    segments = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    base_segment = np.array([0, 1])

    h_new = (size * 4) + 3
    w_new = (size * 2) + 1
    ini = int(h_new / 2) + 1
    list_digits = []
    digit_array = np.zeros((h_new, w_new), dtype=int)
    numbers = convert2integers(expression)
    for n in numbers:
        segment_setup = get_segment_setup(n)
        for seg in segments:
            seg_status = segment_setup[seg]
            if seg_status:
                new_value_seg = np.tile(base_segment, size)
                if seg == 'a':
                    digit_array[0, 0:size*2] = new_value_seg
                elif seg == 'b':
                    digit_array[0:size*2, 0] = new_value_seg
                elif seg == 'c':
                    digit_array[0:size*2, size*2] = new_value_seg
                elif seg == 'd':
                    digit_array[(size*2 + 1), 0:size*2] = new_value_seg
                elif seg == 'e':
                    digit_array[ini:h_new - 1, 0] = new_value_seg
                elif seg == 'f':
                    digit_array[ini:h_new - 1, size*2] = new_value_seg
                elif seg == 'g':
                    digit_array[h_new - 1, 0:size*2] = new_value_seg
    list_digits.append(digit_array)
    digit_array = np.zeros((h_new, w_new), dtype=int)
    print()