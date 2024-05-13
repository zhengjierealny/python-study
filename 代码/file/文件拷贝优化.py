import os

file_name = input('请输入一个文件路径:')
if os.path.isfile(file_name):

    old_file = open(file_name, 'rb')

    names = os.path.splitext(file_name)
    new_file_name = names[0] + '.bak' + names[1]

    new_file = open(new_file_name, 'wb')
    while True:

        content = old_file.read(1024)
        new_file.write(content)
        if not content:
            break

    new_file.close()
    old_file.close()
else:
    print('文件不存在')
