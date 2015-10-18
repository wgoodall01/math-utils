import itertools
import math

def first_row(n):
    rows = []
    for i in range(0, int(n/2)):
        rows.append(2)

    if(n % 2 == 1):
        rows.append(1)

    return rows

def possibilities(row):
    if 2 not in row: return [row]

    pbts = [row]

    mod = row.copy()
    index = mod.index(2)
    mod[index:index+1] = [1, 1] # Replace the 2 with a 1, 1

    pbts.extend(possibilities(mod))

    return pbts

def n_possibilities(n):
    npos = possibilities(first_row(n))
    perms = []

    for pos in npos:
        perms.extend(list(set(itertools.permutations(pos))))

    return perms

def fib(n):
    if n == 0: return []
    if n == 1: return [1]

    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs

def fibcrazy(n):
    return 1/math.sqrt(5)*(
        (((1 + math.sqrt(5))/2)**n)-
        (((1 - math.sqrt(5))/2)**n)
    )

