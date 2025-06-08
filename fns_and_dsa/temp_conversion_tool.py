FAHRENHEIT_TO_CELSIUS_FACTOR = 0
CELSIUS_TO_FAHRENHEIT_FACTOR = 0

def convert_to_celsius(fahrenheit):
    FAHRENHEIT_TO_CELSIUS_FACTOR = (fahrenheit - 32) * 5/9
    print(f"{FAHRENHEIT_TO_CELSIUS_FACTOR}°C")

def convert_to_fahrenheit(celsius):
    CELSIUS_TO_FAHRENHEIT_FACTOR = (celsius * 9/5) + 32
    print (f"{CELSIUS_TO_FAHRENHEIT_FACTOR}°F")

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


