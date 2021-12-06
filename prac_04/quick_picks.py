def main():
    import random
    number_picks = int(input("How many quick picks you want?: "))
    for i in range(number_picks):
        constants = []
        for x in range(6):
            pick_number = random.randint(1, 45)
            while pick_number in constants:
                pick_number = random.randint(1, 45)
            constants.append(pick_number)
        constants.sort()
        print(" ".join("{:2}".format(number) for number in constants))

main()