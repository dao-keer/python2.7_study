# -*- encoding: utf-8 -*-

myName = "I am dao-keer"
print myName

#title函数以首字母大写的方式显示每个单词，对于双引号里的单引号有bug
print myName.title()

myName = myName.title()
print myName

#upper()将字符串全部改为大写
myName = myName.upper()
print myName

#将字符串全部改为小写
myName = myName.lower()
print myName

msg = "i was abc'def'g 20"
print msg.title()
