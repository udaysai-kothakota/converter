def length_converter():
    print("\nLength Units: meter(m), kilometer(km), centimeter(cm)")
    value = float(input("Enter value: "))
    from_unit = input("From unit: ").lower()
    to_unit = input("To unit: ").lower()

    # convert to meters first
    if from_unit == "km":
        value *= 1000
    elif from_unit == "cm":
        value /= 100

    # convert from meters to target
    if to_unit == "km":
        result = value / 1000
    elif to_unit == "cm":
        result = value * 100
    else:
        result = value

    print(f"✅ Result: {result} {to_unit}")


def weight_converter():
    print("\nWeight Units: kilogram(kg), gram(g), pound(lb)")
    value = float(input("Enter value: "))
    from_unit = input("From unit: ").lower()
    to_unit = input("To unit: ").lower()

    # convert to kg
    if from_unit == "g":
        value /= 1000
    elif from_unit == "lb":
        value *= 0.453592

    # convert from kg
    if to_unit == "g":
        result = value * 1000
    elif to_unit == "lb":
        result = value / 0.453592
    else:
        result = value

    print(f"✅ Result: {result} {to_unit}")


def temperature_converter():
    print("\nTemperature Units: Celsius(C), Fahrenheit(F), Kelvin(K)")
    value = float(input("Enter value: "))
    from_unit = input("From unit: ").upper()
    to_unit = input("To unit: ").upper()

    # convert to Celsius first
    if from_unit == "F":
        value = (value - 32) * 5/9
    elif from_unit == "K":
        value = value - 273.15

    # convert from Celsius
    if to_unit == "F":
        result = (value * 9/5) + 32
    elif to_unit == "K":
        result = value + 273.15
    else:
        result = value

    print(f"✅ Result: {result} {to_unit}")


def time_converter():
    print("\nTime Units: second(s), minute(min), hour(hr)")
    value = float(input("Enter value: "))
    from_unit = input("From unit: ").lower()
    to_unit = input("To unit: ").lower()

    # convert to seconds
    if from_unit == "min":
        value *= 60
    elif from_unit == "hr":
        value *= 3600

    # convert from seconds
    if to_unit == "min":
        result = value / 60
    elif to_unit == "hr":
        result = value / 3600
    else:
        result = value

    print(f"✅ Result: {result} {to_unit}")


def main():
    while True:
        print("\n==== UNIT CONVERTER ====")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Time")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            length_converter()
        elif choice == "2":
            weight_converter()
        elif choice == "3":
            temperature_converter()
        elif choice == "4":
            time_converter()
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()