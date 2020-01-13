# import random

# my_randoms = list()
# for i in range(10):
#     my_randoms.append(random.randrange(1, 6))

import random
"""
Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
"""

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))

# Generate a list of numbers 1..10
numbers_1_to_10 = range(1, 11)

# Iterate from 1 to 10
for number in numbers_1_to_10:
    the_numbers_match = False

    # Iterate your random number list here
    for random in my_randoms: 
        if number == random:
            the_numbers_match = True

    # Does my_randoms contain number? Change the boolean.
    if the_numbers_match == True:
        print(f'{number} is in the random list')
    else: print(f'{number} is not in the random list')