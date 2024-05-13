# r:只读,文件不存在会报错
# w 只能写不能读,文件已存在会覆盖原来文件，不存在会创建文件
# b 以二进制形式打开文件,可以操作非文本
# a 追加模式,在最后追加内容，文件不存在会创建，文件存在会追加
# rb 已二进制读取 wb 二进制写入
# file = open('xxx.txt', 'r')
# print(file.read())
# file = open('xxx.txt', 'w')
file = open('xxx.txt', 'wb')
file.write('1111'.encode('utf-8'))
file.close()
