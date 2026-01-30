while True:
    print("\n--- Unit Converter ---")
    print("1. Kilometers to Meters")
    print("2. Meters to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        km = float(input("Enter kilometers: "))
        print("Meters:", km * 1000)

    elif choice == "2":
        m = float(input("Enter meters: "))
        print("Kilometers:", m / 1000)

    elif choice == "3":
        c = float(input("Enter Celsius: "))
        print("Fahrenheit:", (c * 9/5)+32)

    elif choice == "4":
        f = float(input("Enter Fahrenheit: "))
        print("Celsius:", (f - 32)*5/9)

    elif choice == "5":
        print("Exiting. Goodbye!")
        break

    else:
        print("Invalid choice.")
