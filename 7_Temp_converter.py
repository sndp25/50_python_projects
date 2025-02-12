print("Select the unit")
choice = int(input("(1)Celsius\n(2)Fahrenheit\n(3)Kelvin\n>>"))
value = float(input("Value: "))

if choice == 1:
    # Convert from Celsius to Fahrenheit and Kelvin
    celsius = value
    fahrenheit = (value * 9/5) + 32
    kelvin = value + 273.15
    print(f"Celsius: {celsius}°C")
    print(f"Fahrenheit: {fahrenheit}°F")
    print(f"Kelvin: {kelvin}K")

elif choice == 2:
    # Convert from Fahrenheit to Celsius and Kelvin
    fahrenheit = value
    celsius = (value - 32) * 5/9
    kelvin = (value - 32) * 5/9 + 273.15
    print(f"Celsius: {celsius}°C")
    print(f"Fahrenheit: {fahrenheit}°F")
    print(f"Kelvin: {kelvin}K")

elif choice == 3:
    # Convert from Kelvin to Celsius and Fahrenheit
    kelvin = value
    celsius = value - 273.15
    fahrenheit = (value - 273.15) * 9/5 + 32
    print(f"Celsius: {celsius}°C")
    print(f"Fahrenheit: {fahrenheit}°F")
    print(f"Kelvin: {kelvin}K")

else:
    print("Invalid choice. Please select 1, 2, or 3.")
