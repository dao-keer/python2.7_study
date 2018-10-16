def cityCountry(city, country='China'):
    print city + ', ' + country

cityCountry('wuhan')
cityCountry('london', 'England')
cityCountry('shanghai')

def makeAlbum(singer, music, count=0):
    return {'name': singer, 'music': music, 'count': count}

print makeAlbum('liudehua', 'benxiaohai')
print makeAlbum('zhangxueyou', 'elangchuanshuo', 10)

flag = True
while flag:
    name=raw_input('enter the singer name? ')
    if name == 'quit':
        break
    music=raw_input('enter the music name? ')
    if music == 'quit':
        break
    print makeAlbum(name, music)
