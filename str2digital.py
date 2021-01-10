import numpy as np


def get_segment_setup(number: int) -> dict:
    """
    Extract a setup from a dict that contain the setup for any number
    :param number: Digit to print
    :return: a dictionary with the setup
    """
    segments = {
        0: {'a': 1, 'b': 1, 'c': 1, 'd': 0, 'e': 1, 'f': 1, 'g': 1},
        1: {'a': 0, 'b': 0, 'c': 1, 'd': 0, 'e': 0, 'f': 1, 'g': 0},
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


def print_matrix(matrix: np.ndarray):
    """
    prints "-" otherwise prints "|"
    :param matrix: a matrix with all the digits concatenated inside
    :return:
    """
    shape = matrix.shape
    mat = list(matrix)
    for i in range(shape[0]):
        for j in range(shape[1]):

            if i % 2 == 0:
                if mat[i][j] == 1:
                    print('', end='-')
                else:
                    print('', end=' ')
            else:
                if i == int(shape[0]/2):
                    if mat[i][j] == 1:
                        print('', end='-')
                    else:
                        print('', end=' ')
                else:
                    if mat[i][j] == 1:
                        print('', end='|')
                    else:
                        print('', end=' ')
        print()


def transform_numbers(size: int, expression: str):
    """
    Print a sequence of numbers into 7 segments display way
    :param size: Graphical size of digits
    :param expression: string with the numbers to print
    :return:
    """
    hor_symbol = '-'
    ver_symbol = '|'
    segments = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    list_digits = []

    h_new = (size * 4) + 3
    w_new = (size * 2) + 1
    ini = int(h_new / 2) + 1

    # create the base matrices
    base_segment_matrix = np.array([0, 1])
    space_matrix = np.zeros((h_new, size), dtype=int)
    template_matrix = np.zeros((h_new, w_new), dtype=int)

    # convert the string to integer list
    numbers = convert2integers(expression)

    for n in numbers:
        # get the setup of the segments
        segment_setup = get_segment_setup(n)
        for seg in segments:
            seg_status = segment_setup[seg]
            if seg_status:
                new_value_seg = np.tile(base_segment_matrix, size)
                if seg == 'a':
                    template_matrix[0, 0:size * 2] = new_value_seg
                elif seg == 'b':
                    template_matrix[0:size * 2, 0] = new_value_seg
                elif seg == 'c':
                    template_matrix[0:size * 2, size * 2] = new_value_seg
                elif seg == 'd':
                    template_matrix[(size * 2 + 1), 0:size * 2] = new_value_seg
                elif seg == 'e':
                    template_matrix[ini:h_new - 1, 0] = new_value_seg
                elif seg == 'f':
                    template_matrix[ini:h_new - 1, size * 2] = new_value_seg
                elif seg == 'g':
                    template_matrix[h_new - 1, 0:size * 2] = new_value_seg
        # concatenate a zero matrix to simulate the space between digits
        digit_matrix_space = np.concatenate((template_matrix, space_matrix), axis=1)
        # appended each digit to a list, to save it
        list_digits.append(digit_matrix_space)
        # reset the variable
        template_matrix = np.zeros((h_new, w_new), dtype=int)
    # Build a full matrix with all the digits
    full_matrix = np.concatenate(list_digits, axis=1)
    # print
    print_matrix(full_matrix)
