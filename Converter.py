# CONVERTER

category = input("Select a category:\nWeight (w)\nDistance (d)\nTemperature (t)\n>> ")  # Select the category for a conversion


def weight():
    # Selects the conversion
    conversion = input("\nSelect a conversion method:\nKilograms to pounds (1)\nPounds to kilograms (2)\n>> ")

    if conversion == "1":       # Converts kilograms to pounds
        kilograms = float(input("Insert the amount of kilograms: "))
        result = float(kilograms) * 2.205
        print(str(result) + " pounds")

    elif conversion == "2":     # Converts pounds to kilograms
        pounds = float(input("Insert the amount of pounds: "))
        result = float(pounds) / 2.205
        print(str(result) + " kilograms")

    else:
        print("Incorrect input")


def distance():
    conversion = input("Select a conversion method:\nKilometers to miles (1)\nMiles to kilometers (2)\n>> ")
    if conversion == "1":
        kilometers = float(input("Insert the amount of kilometers: "))
        result = float(kilometers) / 1.609
        print(str(result) + " miles")

    elif conversion == "2":
        miles = float(input("Insert the amount of miles: "))
        result = float(miles) * 1.609
        print(str(result) + " kilometers")


def temperature():
    conversion = input("Select a conversion method:\nCelsius to fahrenheit (1)\nFahrenheit to celsius (2)\n>> ")
    if conversion == "1":
        celsius = float(input("Insert the amount of celsius: "))
        result = float(celsius) * 1.8 + 32
        print(str(result) + " fahrenheit")

    elif conversion == "2":
        fahrenheit = float(input("Insert the amount of fahrenheit: "))
        result = float(fahrenheit - 32) * 0.5556
        print(str(result) + " celsius")


if category.lower() == "w":     # Runs the weight function
    weight()

elif category.lower() == "d":     # Runs the distance function
    distance()

elif category.lower() == "t":     # Runs the temperature function
    temperature()

else:
    print("Error")






# Comments:
# Take care of errors
