# -*- encoding: utf-8 -*-
#append操作能作为右值，但返回None
l = ['a', 'b', 'c']
ll = l.append('d')
print l
print ll
#insert能作为右值，但返回None
ll = l.insert(0, l)
print l
print ll
#del不能作为右值
del l[0]
print l
print ll

