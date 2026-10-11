print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((x == (not y)) <= (not (w <= x))) or (not z)

                if F == 0:
                    print(x, y, z, w)
#x y z w
#0 1 1 0
#1 0 1 0
#1 0 1 1

#yxzw
