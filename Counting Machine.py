import sys

# Function to check if a number is prime
def is_prime(num):
    if num > 1:
        if num == 2:
            return True
        elif num % 2 == 0:
            return False
        else:
            for n in range(2, int(num / 2) + 1):
                if num % n == 0:
                    return False
            return True
    else:
        return False

# Function to check if a number is a floating-point number
def is_float(x):
    return x != int(x)

# Function to count perfect squares or perfect cubes
def count_powers(type, start, end):
    if type == "squares":
        thing = "perfect squares"
        power_num = 2
    else:
        thing = "perfect cubes"
        power_num = 3

    if start < 0:
        print("\nPlease enter a whole number.")
        return

    if start == 0:
        start = 1

    print()
    count = 0
    for i in range(int(start), int(end) + 1):
        if i ** power_num <= int(end):
            print(i ** power_num)
            count += 1

    print("\nCounting Complete!")
    print(f"Thus, there are {count} {thing} between {start} and {end}\n")

# Function to count normal numbers
def count_normal_numbers(start, end):
    print()
    for i in range(start, end + 1):
        print(i)
    print("\nCounting complete!")

print("Welcome to the COUNTING Machine!")
print("To exit, press Ctrl + C at any time. \n")
done = False

while not done:
    number_of_nums = 0
    count_type = input("Choose the type of counting you want to do ('p' for prime, 's' for squares, 'c' for cubes, 'b' for binary, and 'n' for normal): ").lower()
    input_first_number = input("Please enter the number you wish to start from (default number is 0): ")
    input_last_number = input("Please enter the number you wish to end at: ")

    if input_first_number == "":
        input_first_number = 0

    if input_last_number == "":
        print("\nYou did not enter any number. Please try again.")
        continue

    input_first_number = float(input_first_number) if is_float(input_first_number) else int(float(input_first_number))
    input_last_number = float(input_last_number) if is_float(input_last_number) else int(float(input_last_number))

    if input_first_number > input_last_number:
        print("\nThe first number you entered is more than the second number. Please try again.")
    elif is_float(input_first_number) or is_float(input_last_number):
        print("One of the numbers you entered is a decimal. Please try again. \n")
    else:
        if count_type in ["s", "squares", "c", "cubes"]:
            count_powers(count_type, input_first_number, input_last_number)
        elif count_type in ["normal", "n"]:
            count_normal_numbers(int(input_first_number), int(input_last_number))
        elif count_type in ["prime", "p"]:
            print()
            for num in range(int(input_first_number), int(input_last_number) + 1):
                if is_prime(num):
                    print(num)
                    number_of_nums += 1
            print("\nCounting Complete!")
            print(f"Thus, between {int(input_first_number)} and {int(input_last_number)}, there are {number_of_nums} prime number(s).\n")
        elif count_type in ["binary", "b"]:
            if input_first_number < 0:
                print("I can't find binary numbers for negatives. Please enter a whole number. \n")
            else:
                for num in range(int(input_first_number), int(input_last_number) + 1):
                    print(num, ">>>", bin(num)[2:])
                print("\nCounting Complete!")
        else:
            print("\nI can't understand the counting type you entered. Please try again. \n")

    again_or_not = input("To count again, press the 'enter' key: ")
    print()
    if again_or_not != "":
        print("You ended the game. Game Over!")
        done = True
