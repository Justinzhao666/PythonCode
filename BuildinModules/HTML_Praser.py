#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

from html.parser import HTMLParser
from html.entities import name2codepoint

# 继承自HTMLParser 对其方法进行重写
class MyHTMLParser(HTMLParser):
    # 处理开始
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)
    # 处理结束
    def handle_endtag(self, tag):
        print('</%s>' % tag)
    # 处理单个标签的 <br/> 这类的
    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)
    # 处理数据
    def handle_data(self, data):
        print(data)
    # 处理注释
    def handle_comment(self, data):
        print('<!--', data, '-->')
    # 处理特殊字符--英文表示的特殊字符 &nbsp
    def handle_entityref(self, name):
        print('&%s;' % name)
    # 处理特殊字符--数字表示的特殊字符 &#1234
    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()

# 使用feed方法进行解析
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')