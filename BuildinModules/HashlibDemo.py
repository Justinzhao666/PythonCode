
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())


#将上面的那个字符串分为多位两个部分来对其update结果是一样的哦
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())


#SHA1 加密
sha1 = hashlib.sha1()
sha1.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())


# homework
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    str = md5.hexdigest()
    try:
        if db[user].__eq__(str):
            print('OK')
            return True
        else:
            print('Fail')
            return False
    except:
        print('No such Key')
        return False

name = input('username:')
pwd = input('password:')
login(name,pwd)

