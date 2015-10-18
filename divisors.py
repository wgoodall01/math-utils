# Divisors of a Positive Integer

import math

#nums = [6, 20, 100, 41, 32, 360, 648]  # Add more numbers here to analyze

#for n in nums:
#   amalyze(n)


def analyze(num):
    count = 0
    print()
    print(':::Factors:::')
    
    for mod in range(1, num + 1):
        if (num % mod == 0):
            count += 1
            print('Factor:' + str(mod))

    print()
    print('Number of factors:' + str(count))
    print()


    if count == 2:
        print(str(num) + ' is a prime number.')
        print('It has no factors other than itself and 1.')
    elif count % 2 == 0:  # even
        print(str(num) + ' has an even number of factors.')
        print(str(num) + ' is not a perfect square.')
    else:               # odd
        print(str(num) + ' has an odd number of factors.')
        print(str(num) + ' is a perfect square.')
        print()
        print(str(num) + ' has ' + str(math.sqrt(num)) +
              ' (its square root) as a factor,' + 
              ' making the number of factors odd.')

    print('\n' + (('#' * 30) + '\n') * 2)

    return count



# param = 1
# while param != 0:
#     param = int(input('Number is: '))
#     analyze(param)

