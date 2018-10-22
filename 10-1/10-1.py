with open('./learn_python.txt') as file_object:
    print file_object.read()

with open('./learn_python.txt') as file_object:
    for line in file_object.readlines():
        print line.rstrip()

with open('./learn_python.txt') as file_object:
    res = []
    for line in file_object.readlines():
        res.append(line)

print res

with open('./learn_python.txt') as file_object:
    print file_object.read().replace('python', 'javascript')

