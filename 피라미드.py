def ee(size):
    for i in reversed(range(size)):
        print('%s%s'%(' '*(size-(i-1)),'*'*((i*2)-1)))

def ll(size):
    for i in range(size):
        if i == size-1:
            print ('%s%s'%(' '*(size-(i-1)),'*'*((i*2)-1)))
            return ee(size)
        print ('%s%s'%(' '*(size-(i-1)),'*'*((i*2)-1)))

ll(5)


a=eval(input)
x=n-abs(i-n)

for y in range(1,n*2):
    print(''.join('*')if n-abs(n-x)-abs(n-y)>0 else "")for
 x in range(1,n*2)
