import random

print(random.randint(5, 20))  # line 1
# The smallest number you have ever seen is 5, the largest number 20.
print(random.randrange(3, 10, 2))  # line 2
# The smallest number you have ever seen is 3 and the largest number is 9.
# Line 2 does not produce a 4, I only saw 3, 5, 7, 9 in my attempts.
print(random.uniform(2.5, 5.5))  # line 3
# You see a very long number on line 3 with many digits after the decimal point
# The smallest number you have ever seen is 2.5965037507598776, and the largest number is 5.469005171016135.


import random

print(random.randint(1, 100))
