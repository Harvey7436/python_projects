def main():
    numbers = get_number()
    result(numbers)

def get_number():
    numbers = []
    for i in range(5):
        number = int(input("NEnter a number: "))
        numbers.append(number)
    return numbers

def result(numbers):
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the number is {}".format(sum(numbers)/len(numbers)))

    print_name()


def print_name():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
                 'InterpreterInterface', 'StartServer', 'bob']
    name = input("Username: ")
    if name in usernames:
        print("Access granted")
    else:
        print("Acess denied")


main()