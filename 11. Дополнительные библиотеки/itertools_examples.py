from itertools import product

'''
print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F1 = (x or (not y)) <= (w == z)
                F2 = (x or (not y)) == (w <= z)
                if F1 == 0:
                    print(x,y,w,z)
'''

'''
for x, y, z, w in product('01', repeat=4):
    print(x, y, z, w)
'''

for item in product('ABCD', 'XYZW', 'ABCD', 'XYZW'):
    print(''.join(item))