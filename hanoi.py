def add_pwrs(length=5, base=2):
    sum = 0;
    for i in range(0, length + 1):
        sum += base ** i

    calc = (base ** (length+1))-1

    if(sum == calc): return True
    else: return (sum, calc)