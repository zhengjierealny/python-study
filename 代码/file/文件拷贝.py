import os
file_name = input('请输入一个文件路径:')
if os.path.isfile(file_name):

    old_file = open(file_name, encoding='utf8')
    # new_file_name = 'test.txt'

    # names = file_name.rpartition('.')
    # new_file_name = names[0] + '.bak.' + names[2]

    names = os.path.splitext(file_name)
    new_file_name = names[0] + '.bak' + names[1]

    new_file = open(new_file_name, 'w', encoding='utf8')
    new_file.write(old_file.read())
    new_file.close()
    old_file.close()
else:
    print('文件不存在')
