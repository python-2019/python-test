import os


class fileUtil(object):
    """
    文件工具类
    """

    @staticmethod
    def copy(src_file, dest_file):
        """
        复制文件
        :param src_file: 源文件
        :param dest_file: 目的文件
        """
        while True:
            read = src_file.read(10240)
            if len(read) == 0:
                break
            dest_file.write(read)

    @staticmethod
    def open(file_path, mode='r+', encoding='utf-8'):
        """
        打开文件
        :param file_path: 文件地址
        :return:
        """
        return open(file_path, mode, encoding=encoding)

    @staticmethod
    def save_str_2_file(str, dest_file):
        """
        文件写入
        :param str:
        :param dest_file:
        :return:
        """
        dest_file.write(str)
        dest_file.flush()

    @staticmethod
    def get_file_list_base(dir):
       return os.listdir(dir)


if __name__ == '__main__':
    file_util_open = fileUtil.open("c", mode="a+")
    print(file_util_open.name)
    fileUtil.save_str_2_file("asdadsad撒多所多所", file_util_open)
