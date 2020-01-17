from datetime import datetime, timedelta
import time


class dateUtil(object):

    @staticmethod
    def get_date_str(days_delta: int = 0, hours_delta: int = 0, minutes_delta: int = 0, seconds_delta: int = 0,
                     str_format: str = '%Y-%m-%d %H:%M:%S'):
        '''
        获取日期字符串
        :param time_delta: 时间间隔(天)
        :param str_format: 格式化字符串
        :return:
        '''
        return (datetime.today() + timedelta(days=days_delta) + timedelta(hours=hours_delta) + timedelta(
            minutes=days_delta) + timedelta(seconds=seconds_delta)).strftime(str_format)

    @staticmethod
    def timestamp_millis():
        '''
        毫秒级时间戳(十三位)
        '''
        return int(time.time() * 1000)

    @staticmethod
    def date_str_2_dateArray(date_str, str_format: str = '%Y-%m-%d %H:%M:%S'):
        '''
        毫秒级时间戳(十三位)
        '''
        return time.strptime(date_str, str_format);

    @staticmethod
    def date_2_millisecond(dateArray):
        return int(time.mktime(dateArray))

    def after(self):
        pass


if __name__ == '__main__':
    print(int(time.mktime(dateUtil.date_str_2_date(dateUtil.get_date_str()))))
