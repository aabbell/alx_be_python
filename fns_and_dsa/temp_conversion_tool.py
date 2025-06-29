FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{celsius}°C")

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print (f"{fahrenheit}°F")

def user():
    num = int(input("Enter the temperature to convert: "))
    temp = str(input("Is this temperature in Celsius or Fahrenheit? (C/F):"))
    if temp == 'F':
        convert_to_celsius(num)
    elif temp == 'C':
        convert_to_fahrenheit(num)
    else:
        print("Invalid temperature. Please enter a numeric value.")

user()
