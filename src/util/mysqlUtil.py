import pymysql


class mysqlUtil(object):

    @staticmethod
    def getConn(db, host="localhost", username="root", password="root", port=3306):
        """
          获取连接
        :param db:
        :param host:
        :param username:
        :param password:
        :param port:
        :return: 连接
        """
        return pymysql.connect(host, user=username, passwd=password, db=db, port=port);

    @staticmethod
    def getDefaultConn():
        """
          获取连接 默认配置
        :param db:
        :param host:
        :param username:
        :param password:
        :param port:
        :return: 连接
        """
        return pymysql.connect('localhost', user="root", passwd="root", db="tima-test");

    @staticmethod
    def execute_and_fetchall(conn, sql):
        """
        返回所有查询结果
        :param conn: 数据库连接
        :param sql: sql
        :return: tuple
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @staticmethod
    def execute_and_fetchone(conn, sql):
        """
        返回一条查询结果
        :param conn: 数据库连接
        :param sql: sql
        :return: tuple
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchone()

    @staticmethod
    def execute_and_fetchmany(conn, sql,size):
        """
        返回指定条数查询结果
        :param conn: 数据库连接
        :param sql: sql
        :return: tuple
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchmany(size)


# TEST
if __name__ == '__main__':
    conn = mysqlUtil.getDefaultConn()
    fetchall = mysqlUtil.execute_and_fetchall(conn, "select * from dept")
    for one in fetchall:
        print(one)
        print(one[2])
        print(type(one))
