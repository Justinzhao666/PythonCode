#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

from email.mime.text import MIMEText
# 构造邮件内容
msg = MIMEText('hello send by justin chiu ...','plain','utf-8')

from_addr = input('From:')
password = input('Password:')

to_addr = input('To:')
smtp_server = input('SMTP Server:')

import smtplib
server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
