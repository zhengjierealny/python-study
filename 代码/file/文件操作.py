file = open('xxx.txt', encoding='utf-8')
print(file.read())

# 路径
# 绝对路径 C:\Users\realny\Desktop\python sutdy\代码\file\xxx.txt
# windows系统里文件之间用\分隔  在非windows系统用/分隔
# 相对路径

file = open('C:\\Users\\realny\\Desktop\\python sutdy\\代码\\file\\xxx.txt', encoding='utf-8')
# ==file = open(r'C:\Users\realny\Desktop\python sutdy\代码\file\xxx.txt', encoding='utf-8')
print(file.read())

file = open('demo/xxx.txt', encoding='utf-8')
print(file.read())  # readline()只读一行 file.read(1024)读取前1024个内容

file = open('../xxx.txt', encoding='utf-8')
print(file.read())

# file = open('xxx.mp4', 'rb') 读取视频
