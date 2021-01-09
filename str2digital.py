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
    hor_symbol = ' -'
    ver_symbol = '|'
    segments = ['a', 'b', 'd', 'e', 'g']
    hor_segments = ['a', 'd', 'g']
    str_all_segments = []
    segs_ok = []
    space_bwn_digits = ' ' * size
    space_bwn_verticals = (' ' * ((size*2) - 1))
    seg_str = ''
    vertical_seg_flag = False
    non_active_seg_flag = False

    digits = convert2integers(expression)

    for seg in segments:
        seg_str = ''
        for n in digits:
            seg_setup = get_segment_setup(n)
            seg_status = seg_setup[seg]
            'If the segment needs turn ON'
            if seg_status:
                if seg in hor_segments:
                    'If the segment is vertical'
                    seg_str += (hor_symbol * size) + ' ' + space_bwn_digits
                else:
                    'If the segment is Horizontal it need to draw in parallel'
                    vertical_seg_flag = True
                    if seg == 'b':
                        seg_str += ver_symbol + space_bwn_verticals
                    if seg_setup['c']:
                        seg_str += ver_symbol + space_bwn_digits

                    elif seg == 'e':
                        seg_str += ver_symbol + space_bwn_verticals
                        if seg_setup['f']:
                            seg_str += ver_symbol + space_bwn_digits
            else:
                non_active_seg_flag = True

        if non_active_seg_flag:
            non_active_seg_flag = False
            continue

        seg_str += '\n'
        if vertical_seg_flag:
            vertical_seg_flag = False
            seg_str *= size
        str_all_segments.append(seg_str)
    for line in str_all_segments:
        print(line.format(end=''))
