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
    print("Choose an option:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Quit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 7:
        break
    
    if choice < 1 or choice > 6:
        print("Invalid choice. Please choose a valid option.")
        continue
    
    value = float(input("Enter the temperature value: "))
    
    if choice == 1:
        result = celsius_to_fahrenheit(value)
        print(f"{value} Celsius = {result} Fahrenheit")
    elif choice == 2:
        result = fahrenheit_to_celsius(value)
        print(f"{value} Fahrenheit = {result} Celsius")
    elif choice == 3:
        result = celsius_to_kelvin(value)
        print(f"{value} Celsius = {result} Kelvin")
    elif choice == 4:
        result = kelvin_to_celsius(value)
        print(f"{value} Kelvin = {result} Celsius")
    elif choice == 5:
        result = fahrenheit_to_kelvin(value)
        print(f"{value} Fahrenheit = {result} Kelvin")
    elif choice == 6:
        result = kelvin_to_fahrenheit(value)
        print(f"{value} Kelvin = {result} Fahrenheit")
