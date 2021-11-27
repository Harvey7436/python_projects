def main():
    print("""C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit""")
    choice = input("Please enter your choice: ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Please enter the temperature you want to convert: "))
            fahrenheit = celsius * 9.0 / 5 + 32
            print(f"{celsius:.2f}celsius=>{fahrenheit:.2f}fahrenheit")
        elif choice == "F":
            fahrenheit = float(input("Please enter the temperature you want to convert: "))
            celsius = 5 / 9 * (fahrenheit - 32)
            print(f"{fahrenheit:.2f}celsius=>{celsius:.2f}fahrenheit")
        else:
            print("Invalid option")
        choice = input("Please enter your choice: ").upper()
    print("Thank you for using.")

main()