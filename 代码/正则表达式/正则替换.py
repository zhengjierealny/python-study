# 替换: sub

import re

t = '43fgfg3gdsfg4sf32rsefs'
print(re.sub(r'\d', 'x', t))


def test(x):
    y = int(x.group(0))
    y *= 2
    return str(y)


print(re.sub(r'\d+', test, t))
