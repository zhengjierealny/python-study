from mysql import MysqlTool


if __name__ == '__main__':
    with MysqlTool() as db:
        # 查询所有数据
        sql = 'SELECT * FROM student'
        result = db.execute(sql)
        print(f"查询到的数据为：{result}")

        # # 带条件的查询
        # sql = "SELECT * FROM student WHERE age > %s"
        # args = (18,)
        # result = db.execute(sql, args)
        # print(f"年龄大于18岁的学生：{result}")
        #
        # # 单条插入
        # sql = "INSERT INTO student(name, age) VALUES (%s, %s)"
        # args = ('张三', 22)
        # db.execute(sql, args, commit=True)
        #
        # # 多条插入
        # sql = "INSERT INTO student(name, age) VALUES (%s, %s)"
        # args_list = [('李四', 20), ('王五', 21), ('赵六', 23)]
        # for args in args_list:
        #     db.execute(sql, args, commit=True)
        #
        # # 修改数据
        # sql = "UPDATE student SET age=%s WHERE name=%s"
        # args = (23, '张三')
        # db.execute(sql, args, commit=True)
        #
        # # 删除数据
        # sql = "DELETE FROM student WHERE name=%s"
        # args = ('张三',)
        # db.execute(sql, args, commit=True)
