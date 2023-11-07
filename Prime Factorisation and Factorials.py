# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to find the prime factors of a number
def prime_factors(x):
    factors = []
    if is_prime(x):
        return f"You entered a prime number. So, its prime factorization is 1 x {x}"
    for i in range(2, x // 2 + 1):
        while x % i == 0:
            factors.append(str(i))
            x //= i
    if x > 1:
        factors.append(str(x))
    return f"The Prime Factorization of {x} is {' x '.join(factors)}"

# Function to calculate the factorial of a number
def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x - 1)

user_number = "Unknown"

while user_number != "":
    mode_type = input("Enter 'pf' to find the prime factorization of a number and 'f' to find the number's factorial: ").lower()
    user_number = input("Please enter your number (To exit, simply press ENTER): ")

    if user_number != "":
        the_number = int(user_number)
        if mode_type in ["factorial", "f"]:
            if the_number > 0:
                print(f"The factorial of {the_number} is {factorial(the_number)}")
            else:
                print("The number you entered does not have a factorial.")
        elif mode_type in ["prime factorization", "pf"]:
            print(prime_factors(the_number))
        else:
            print("I didn't understand what you entered. Please try again.")
    else:
        print("You ended the game. Game Over!")
