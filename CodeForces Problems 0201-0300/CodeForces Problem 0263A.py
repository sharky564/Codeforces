# Beautiful Matrix
inputs = [input() for i in range(5)]

i = 0
while inputs[i] != '1':
    i += 1

moves4 = ['0', '4', '20', '24']
moves3 = ['1', '3', '5', '9', '15', '19', '21', '23']
moves2 = ['2', '6', '8', '10', '14', '16', '18', '22']
moves1 = ['7', '11', '13', '17']
moves0 = ['12']

if str(i) in moves4:
    print('4')

if str(i) in moves3:
    print('3')

if str(i) in moves2:
    print('2')

if str(i) in moves1:
    print('1')

if str(i) in moves0:
    print('0')
