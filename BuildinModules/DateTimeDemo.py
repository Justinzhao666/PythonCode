#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates
import re
from datetime import datetime
#datetime 模块里面有个datetime类

#获取当前时间
now = datetime.now()
print(now)
print(type(now))

#获取指定日期和时间
dt = datetime(2015,4,19,12,20)
print(dt)

#datetime是有时区概念的
#转datetime为timestamp（计算机中时间的数字表示方式）
# timestamp 距离一个时区0时的秒数，为一个数字
time = dt.timestamp()
print(dt.timestamp())

#将timestamp转为datetime
print(datetime.fromtimestamp(time))  #转为本地时间
print(datetime.utcfromtimestamp(time)) #转为utc时间标准的时间-----针对国际上的0时 UTC的0时

#str 和 datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S') #string to time
print('str 转datetime：%s'%cday)
print('datetime to string : %s '%datetime.now().strftime('%a, %b %d %H:%M')) #string from time

#datetime 运算,需要导入这个类，然后直接加减所要的时间就行了
from datetime import timedelta
now1 = datetime.now()
print(now1 + timedelta(hours=2))
print(now1 - timedelta(hours=2))
print(now1 + timedelta(days=1,hours=2))


# 本地时间转为UTC时间
from datetime import timezone
utc_8 = timezone(timedelta(hours=8))  # 创建utc时区为8
now2 = datetime.now()
dt = now2.replace(tzinfo= utc_8)  #将datetime的时区属性设置为utc_8
print(dt)


#时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc) # 加上这个replace 就是在显示日期的时候后面会加上时区的信息
print(utc_dt)  #utcnow()获取到了utc的时区信息
#下面想要获得哪个时区只要在对应的时区和utc的差值上进行加减，就可以计算出该时区信息
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9))) #使用astimezone的方法可以自由的进行时区的转换
print('日本时间：%s'%tokyo_dt)


def to_timestamp(dt_str, tz_str):#先转成对应的时区
    dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    num = re.match('UTC(.*)\:00',tz_str) #*号 是表示前面的数量级
    num1 = int(num.group(1))
    print(num1)
    utc_info = timezone(timedelta(hours=int(num.group(1))))
    dt = dt.replace(tzinfo=utc_info)
    return dt.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
print(t1)
# assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
print(t2)
# assert t2 == 1433121030.0, t2

print('Pass')


