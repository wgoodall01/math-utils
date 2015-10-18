#LOCKER PROBLEM SOLVER

lockers = [False]
for i in range(1, 1001):
    lockers.append(True)

for mod in range(2, 1001):
    for i, val in enumerate(lockers):
        if i % mod == 0:
            lockers[i] = not lockers[i]

#for i, val in enumerate(lockers):
#    print(str(i) + ':' + str(val))


#print('###############')


for i, val in enumerate(lockers):
    if val:
        print(str(i) + ':' + str(val))
