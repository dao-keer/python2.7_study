#!/usr/bin/env python
# -*- coding: utf-8 -*-
#直接运行.py文件，需要在文件的首行加上上面的代码，指定文件运行所需要的编译器环境，然后把文件的类型更改为可运行的文件
print "hello world!"
#编译器会依次打印输出下面三个字符串，遇到逗号会输出一个空格字符串
print "I", "love", "you"
#raw_input()函数用来接受用户的输入，会中断程序的运行
age = raw_input("please enter you age:")
print "your age is:", age
if age > 18:
    print True
else:
    print False
#如果需要打印特殊字符需要使用转义符
print "I love\npython"
#字符串默认不转义需要用 print r
print r"I love\npython"
#输出多行内容可以使用print '''...'''
print '''i
love
you'''
#如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
print "your name is %s, your age is %s" %('cyz', 25)
#两个%%可以输出一个%
print "the rate is %d%%" %7
#list是一个有序集合，索引-1返回list的最后一个元素
list1 = [1, 2, 3, 4]
print list1[0], list1[-1]
#range(n)就可以生成0-(n-1)的整数序列，不包含n，n必须是整数，若n < 0，则list为空集合
list2 = range(-10)
print list2
#列表生成
print [m + n for m in [1, 2, 3] for n in [3, 2, 1]]
