def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

while True:
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Quit")

    choice = input("Enter your choice (1/2/3/4/5/6/7): ")

    if choice == "7":
        break

    if choice in ["1", "2", "3", "4", "5", "6"]:
        temperature = float(input("Enter the temperature: "))

        if choice == "1":
            result = celsius_to_fahrenheit(temperature)
            print(f"{temperature} Celsius is {result} Fahrenheit")
        elif choice == "2":
            result = fahrenheit_to_celsius(temperature)
            print(f"{temperature} Fahrenheit is {result} Celsius")
        elif choice == "3":
            result = celsius_to_kelvin(temperature)
            print(f"{temperature} Celsius is {result} Kelvin")
        elif choice == "4":
            result = kelvin_to_celsius(temperature)
            print(f"{temperature} Kelvin is {result} Celsius")
        elif choice == "5":
            result = fahrenheit_to_kelvin(temperature)
            print(f"{temperature} Fahrenheit is {result} Kelvin")
        elif choice == "6":
            result = kelvin_to_fahrenheit(temperature)
            print(f"{temperature} Kelvin is {result} Fahrenheit")
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4/5/6/7).")

print("Thank you for using the Temperature Converter!")
