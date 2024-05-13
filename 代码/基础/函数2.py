# 匿名函数 lambda 只用一次
def calc(a, b, fn):
    c = fn(a, b)
    return c


x = calc(1, 2, lambda a, y: a + y)
x2 = calc(1, 2, lambda a, y: a - y)
