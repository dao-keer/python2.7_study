def makeShirt(size, title):
    print 'the shirt size is ' + str(size) + ', title is ' + title

makeShirt(35, 'i love python!')
makeShirt(title='i hate you', size=2)

def printCity(city, country="China"):
    print city + ' is in ' + country

printCity('wuhan')
printCity(city='beijing')
printCity('london', 'England')