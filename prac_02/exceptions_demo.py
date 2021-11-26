"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0: #use while loop can avoid this problem,when user put 0 in denominator,
        # this programing will ask again until user does not put 0
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
    #when I put float,it will be valueerror
except ZeroDivisionError:
    print("Cannot divide by zero!")
    #when I put 0 in denominator,it will be ZeroDivisionError
print("Finished.")
