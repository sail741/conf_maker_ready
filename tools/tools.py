import math

greek = {
    "gamma": u'\u03b3',
    "delta": u'\u03b4',
    "deltaU": u'\u0394',
}


def index_to_str(i):
    res_array = []
    while i >= 26:
        qty = math.floor(i / 26)
        res_array.append(qty - 1)

        i = i - 26 * qty

    res_array.append(i)

    res_str = ""
    for v in res_array:
        res_str += str(chr(v + 97))

    return res_str
