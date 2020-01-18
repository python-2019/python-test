from datetime import datetime, timedelta
import time


class dateUtil(object):
    """
    日期相关操作
    """

    @staticmethod
    def get_date_str(date, days_delta: int = 0, hours_delta: int = 0, minutes_delta: int = 0,
                     seconds_delta: int = 0,
                     str_format: str = '%Y-%m-%d %H:%M:%S'):
        """
        获取日期字符串
        :param time_delta: 时间间隔(天)
        :param str_format: 格式化字符串
        :return:
        """
        return (date + timedelta(days=days_delta) + timedelta(hours=hours_delta) + timedelta(
            minutes=days_delta) + timedelta(seconds=seconds_delta)).strftime(str_format)

    @staticmethod
    def get_now_date_str(days_delta: int = 0, hours_delta: int = 0, minutes_delta: int = 0,
                     seconds_delta: int = 0,
                     str_format: str = '%Y-%m-%d %H:%M:%S'):
        """
        获取 当前日期字符串
        :param time_delta: 时间间隔(天)
        :param str_format: 格式化字符串
        :return:
        """
        return dateUtil.get_date_str(datetime.today())

    @staticmethod
    def timestamp_millis():
        """
        毫秒级时间戳(十三位)
        """
        return int(time.time() * 1000)

    @staticmethod
    def timestamp_seconds():
        """
        秒级时间戳(十位)
        """
        return int(time.time())

    @staticmethod
    def date_str_2_dateArray(date_str, str_format: str = '%Y-%m-%d %H:%M:%S'):
        """
        毫秒级时间戳(十三位)
        """
        return time.strptime(date_str, str_format);

    @staticmethod
    def date_2_millisecond(dateArray):
        """
        时间数组转时间戳
        :param dateArray: 
        :return: 
        """
        return int(time.mktime(dateArray))

    @staticmethod
    def after_millis(start, end):
        """
         end时间戳 是否在start后面
        
        :param start: 预期小的时间
        :param end: 预期大的时间
        :return: 布尔值
        """
        return start < end

    @staticmethod
    def after_date_str(start, end):
        """
        end字符串时间  是否大于start

        :param start: 字符串时间
        :param end: 字符串时间
        :return:
        """
        start_millis = dateUtil.date_2_millisecond(dateUtil.date_str_2_dateArray(start))
        end_millis = dateUtil.date_2_millisecond(dateUtil.date_str_2_dateArray(end))
        return dateUtil.after_millis(start_millis, end_millis)


if __name__ == '__main__':
    date_str = dateUtil.get_now_date_str()
    print(date_str)
