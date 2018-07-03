import math

# Greek dictionary to display greek letter
greek = {
    "gamma": u'\u03b3',
    "delta": u'\u03b4',
    "deltaU": u'\u0394',
}


def index_to_str(i):
    """
    Turn integer to str with this logic :
    0 : a
    25 : z
    26 : aa
    27 : ab
    etc

    :param i: the integer to parse
    :return: the converted string
    """
    res_array = []
    while i >= 26:
        left = math.floor(i / 26)
        right = i - 26 * left
        res_array.append(right)

        i = left - 1

    res_array.append(i)

    res_str = ""
    for v in reversed(res_array):
        res_str += str(chr(v + 97))

    return res_str
