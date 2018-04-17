"""
    Insane Coloured Triangles
    http://www.codewars.com/kata/insane-coloured-triangles/train/python
    Luís Melo - 17/04/2018
"""
def combine_elements(a, b):
    if a not in ('R', 'G', 'B') and b not in ('R', 'G', 'B'):
        raise Exception('Wrong input')

    if a == b:
        return a

    return list({'R', 'G', 'B'} - {a, b})[0]


def triangle(row):
    if 1 > len(row) > 10 ** 5:
        raise Exception('Constraint not satisfied')

    for i in range(len(row), 1, -1):
        row = ''.join([combine_elements(row[i], row[i - 1]) for i, _ in enumerate(row) if i != 0])

    return row


assert triangle('B') == 'B'
assert triangle('GB') == 'R'
assert triangle('RRR') == 'R'
assert triangle('RGBG') == 'B'
assert triangle('RBRGBRB') == 'G'
assert triangle('RBRGBRBGGRRRBGBBBGG') == 'G'
