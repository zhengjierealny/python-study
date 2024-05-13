def tell_11():
    print(1)
    print(2)
    print(3)


print('函数')
tell_11()


def work(name, room, time):
    print('姓名：' + name)
    print('地点：' + room)
    print('时间：' + time)


work('xx', '101', '10点')
work(room='1011', name='xxx', time='12点')


def jia(a, b):
    c = a + b
    return c


result = jia(1, 3)
print(result)


def heti(a, b):
    """
    相加
    :param a:数字1
    :param b:数字2
    :return:结果
    """
    return a + b


print(heti(1, 5))


# 函数内部修改全局变量通过global, global a    a=10

# 函数多个返回值
def test(a, b):
    x = a // b
    y = a % b
    # return [x, y]  # {'x':x,'y':y}  (x,y)
    return x, y


result = test(13, 5)
shang, yushu = test(8, 3)
print('商是{}，余数是{}'.format(shang, yushu))


# 设置默认值
def test2(name, age, sex="男"):
    print(111)


test2('11', '22')
test2('12', age='23', sex='女')


# 可变参数函数
def add_many(iter):
    x = 0
    for n in iter:
        x = n + x
    return x


nums = [1, 2, 3, 4, 5, 6, 7]
print(add_many(nums))

print(add_many((3, 4, 6, 87, 9)))
print(add_many({5, 6, 7}))
print(add_many(range(3, 9)))


def add_n(a, b, *args):  # *args 表示可变参数
    print('a = {},b = {}'.format(a, b))
    print('args = {}'.format(args))


add_n(3, 4, 5, 6, 3, 5)

# python中如果函数重名，后一个会替换前一个函数
# 函数名可以理解为变量名，
# def test()...   test=2  test(3) //test(3)会报错



