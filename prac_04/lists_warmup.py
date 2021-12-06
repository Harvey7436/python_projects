numbers = [3, 1, 4, 1, 5, 9, 2]
'''
numbers[0] = 3
numbers[-1] = 2
numbers[3] = 1
numbers[:-1] = 3, 1, 4, 1, 5, 9
numbers[3:4] = 1
5 in numbers = Ture
7 in numbers = False
"3" in numbers = False
numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
'''
#1. Change the first element of numbers to "ten" (the string, not the number 10)#
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[0] ='ten'
print(f"{numbers}")

#2. Change the last element of numbers to 1
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[-1] = 1
print(f"{numbers}")

#3. Get all the elements from numbers except the first two (slice)
numbers = [3, 1, 4, 1, 5, 9, 2]
i = numbers[2:]
print(f"{i}")

#4. Check if 9 is an element of numbers
numbers = [3, 1, 4, 1, 5, 9, 2]
x = 9 in numbers
print(f"{x}")

