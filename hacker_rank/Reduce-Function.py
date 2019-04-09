from fractions import Fraction
from functools import reduce
fracs = []

my_frac = [
    '84025282 932952183',
    '349232934 278093065',
    '778706161 742081687',
    '374870211 874099626',
    '849763633 211127281',
    '566205501 508794028',
    '814324820 443967409',
    '402053385 120666811',
    '261003218 519477752',
    '134531387 354698174',
    '790584924 879493679',
    '520320652 475787580',
    '480239279 930995305',
    '465217671 718416348',
    '270497402 819933293',
    '216292652 688271440',
    '76664269 6180883',
    '802885525 457264574',
    '194701183 725188300',
    '63039953 241525609',
    '576817633 832775273',
]

arr = list(map(int, '1 2 3 4 5 6'.split()))

for _ in range(0, len(my_frac)-1):
    fracs.append(Fraction(*map(int, my_frac[_].split())))

result = reduce(lambda x, y: x*y, fracs)
print(fracs)
# print(' '.join(str(result).split('/')))
print(result.denominator, result.numerator)

