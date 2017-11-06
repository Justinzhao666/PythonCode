#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

# Dom解析xml十分占内存，一般使用Sax方式来解析

# Sax 解析  --start_element,end_element,data  ,这三个不是三个值！而是代表了三个事件。当遇到对应情况的时候要做的处理。
from xml.parsers.expat import ParserCreate


# 需要自己对解析的事件，写处理机制
class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()   #
parser = ParserCreate() # 用来解析xml的对象，这个parser对象有三个重要的事件如下：
parser.StartElementHandler = handler.start_element # 事件1 ： 遇到开始元素， 使用handler的开始元素方式处理该事件
parser.EndElementHandler = handler.end_element  # 事件2 ： 遇到结束元素， 使用handler的结束元素方式处理该事件
parser.CharacterDataHandler = handler.char_data  # 事件3 ： 遇到实际数据， 使用handler的实际数据方式处理该事件
parser.Parse(xml) # 约定好了规则，就开始解析xml这个字符串，

# 生成xml
def Generate_XML():
    L = []
    L.append(r'<?xml version="1.0"?>')
    L.append(r'<root>')
    L.append(('some & data').encode('utf-8'))
    L.append(r'</root>')
    return ''.join(L)


# Homework

data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
        <title>Yahoo! Weather - Beijing, CN</title>
        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
        <yweather:location city="Beijing" region="" country="China"/>
        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
        <yweather:wind chill="28" direction="180" speed="14.48" />
        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
        <item>
            <geo:lat>39.91</geo:lat>
            <geo:long>116.39</geo:long>
            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
        </item>
    </channel>
</rss>
'''

class WeatherSaxHandler(object):
    weather = []
    def start_element(self,name,attrs): #参数好像是固定的哟
        if name == 'yweather:location':
            self.city = attrs['city']
            self.country = attrs['country']
        if name == 'yweather:forecast':
            self.weather.append({'text':attrs['text'], 'low': attrs['low'],'high':attrs['high']})


def parse_weather(xml):

    handler = WeatherSaxHandler()
    parser = ParserCreate()

    parser.StartElementHandler = handler.start_element
    parser.Parse(xml)
    return {
        'city': handler.city,
        'country': handler.country,
        'today': {
            'text': handler.weather[0].get('text'),
            'low': handler.weather[0].get('low'),
            'high': handler.weather[0].get('high')
        },
        'tomorrow': {
            'text': handler.weather[0].get('text'),
            'low': handler.weather[1].get('low'),
            'high': handler.weather[1].get('high')
        }
    }

#结果正式说明list是无序的？
print(parse_weather(data))