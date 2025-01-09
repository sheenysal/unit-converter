def convert_units():
    print("Unit Converter")
    print("1. Length (meters to kilometers)")
    print("2. Weight (grams to kilograms)")
    print("3. Temperature (Celsius to Fahrenheit)")

    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        meters = float(input("Enter length in meters: "))
        print(f"{meters} meters is {meters / 1000} kilometers.")
    elif choice == '2':
        grams = float(input("Enter weight in grams: "))
        print(f"{grams} grams is {grams / 1000} kilograms.")
    elif choice == '3':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C is {(celsius * 9 / 5) + 32}°F.")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    convert_units()
