pets = [{
    'dog': {
        'name': 'bob',
        'age': 3
    }},
    {'cat': {
        'name': 'tom',
        'age': 1
    }}
]

for i in pets:
    print i
    for ii, vv in i.items():
        print 'category is: ' + ii
        for iii, vvv in vv.items():
            print iii + ': ' + str(vvv)

cities = {
    'wuhan': {
        'country': 'China',
        'population': '20million',
        'fact': 'a big country'
    },
    'london': {
        'country': 'England',
        'population': '2million',
        'fact': 'a small country'
    }
}

for i, v in cities.items():
    print i
    for ii, vv in v.items():
        print '\t' + ii + ': ' + vv