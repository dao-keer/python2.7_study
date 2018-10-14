# -*- encoding: utf-8 -*-
places = ['xiamen', 'dongjin', 'bali', 'lundun', 'luoshanji', 'lasiweijiasi']
print places
#sorted临时排序方法，返回排序后的列表，原列表并未被改变，reverse=True代表倒序排列
print sorted(places)
print places
print sorted(places, reverse=True)
print places
#列表的reverse（）方法表示倒序排列此列表，返回None，但列表已经被改变
places.reverse()
print places
places.reverse()
print places
places.sort()
print places
places.sort(reverse=True)
print places

countries = ['中国', '日本', '美国', '巴西', '加拿大', '法国', '墨西哥']
countries.append('澳大利亚')
print str(countries).decode("string_escape")
countries.insert(0, '印度')
print str(countries).decode("string_escape")
print str(countries.pop(0)).decode("string_escape")
print str(countries).decode("string_escape")
countries.remove('日本')
print str(countries).decode("string_escape")
print len(countries)
countries.sort()
print str(countries).decode("string_escape")
print str(sorted(countries, reverse=True)).decode("string_escape")
countries.sort()
print str(countries).decode("string_escape")
countries.sort(reverse=True)
print str(countries).decode("string_escape")
print len(countries)
