import os
import time
import traceback

def file_storage(file_path,suffix):
    r"""
        file_path :: The file absolute path
        suffix :: filename

        file_path=C:\Users\Desktop\video_
        filename = abc.py
        return C:\Users\Desktop\video_2020\12\12\abc.py
    """
    tm = time.localtime(time.time())
    # 获取系统当前年，月，日，小时
    year = time.strftime('%Y', tm)
    month = time.strftime('%m', tm)
    day = time.strftime('%d', tm)
    # 根据当前日期创建图片文件
    file_year = file_path + '/' + year
    file_month = file_year + '/' + month
    file_day = file_month + '/' + day
    # 判断路径是否存在，没有则创建
    if not os.path.exists(file_path):
        os.makedirs(file_path)
        os.mkdir(file_year)
        os.mkdir(file_month)
        os.mkdir(file_day)
    else:
        if not os.path.exists(file_year):
            os.mkdir(file_year)
            os.mkdir(file_month)
            os.mkdir(file_day)
        else:
            if not os.path.exists(file_month):
                os.mkdir(file_month)
                os.mkdir(file_day)
            else:
                if not os.path.exists(file_day):
                    os.mkdir(file_day)
    return os.path.join(file_day,suffix)
