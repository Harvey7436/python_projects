OUTPUT_FILE = "name.txt"
out_file = open(OUTPUT_FILE, 'w')
name = input("hi,what is your name:")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Your name is", name)

OUTPUT_FILE = "numbers.txt"
out_file = open(OUTPUT_FILE, 'w')
A = 17
B = 42
C = 400
print(A, file=out_file)
print(B, file=out_file)
print(C, file=out_file)
out_file.close()
total = A + B
print("The sum of the first two numbers is", total)
total_number = A + B + C
print("The sum of all numbers is",total_number)



