x,y,z = input('Expression: ').strip().lower().split(' ')
x = float(x)
z = float(z)
# print(x,y,z)

if y == '+':
    print(x+z)
elif y == '-':
    print(x-z)
elif y == '*':
    print(x*z)
else:
    if z != 0:
        print(x/z)    
    else:
        print('z must be different from 0')
