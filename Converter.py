
# CONVERTER

category = input("Select a category:\nWeight (w)\nDistance (d)\nTemperature (t)\n>> ")  # Select the category for a conversion


def weight():
    # Selects the conversion
    conversion = input("\nSelect a conversion method:\nKilograms to pounds (1)\nPounds to kilograms (2)\n>> ")

    if conversion == "1":       # Converts kilograms to pounds
        try:
            kilograms = float(input("Insert the amount of kilograms: "))
            result = float(kilograms) * 2.205
            print(str(result) + " pounds")
        except ValueError:
            print("Error, please enter a valid number")
            run_again = input("Run again? (y),(n)\n")
            if run_again == "y":
                weight()

    elif conversion == "2":     # Converts pounds to kilograms
        try:
            pounds = float(input("Insert the amount of pounds: "))
            result = float(pounds) / 2.205
            print(str(result) + " kilograms")
        except ValueError:
            print("Error, please enter a valid number")
            run_again = input("Run again? (y),(n)\n")
            if run_again == "y":
                weight()


def distance():
    conversion = input("Select a conversion method:\nKilometers to miles (1)\nMiles to kilometers (2)\n>> ")
    if conversion == "1":       # Converts kilometers to miles
        try:
            kilometers = float(input("Insert the amount of kilometers: "))
            result = float(kilometers) / 1.609
            print(str(result) + " miles")
        except ValueError:
            print("Error, please enter a valid number")
            run_again = input("Run again? (y),(n)\n")
            if run_again == "y":
                weight()

    elif conversion == "2":     # Converts miles to kilometers
        try:
            miles = float(input("Insert the amount of miles: "))
            result = float(miles) * 1.609
            print(str(result) + " kilometers")
        except ValueError:
            print("Error, please enter a valid number")
            run_again = input("Run again? (y),(n)\n")
            if run_again == "y":
                weight()


def temperature():
    conversion = input("Select a conversion method:\nCelsius to fahrenheit (1)\nFahrenheit to celsius (2)\n>> ")
    if conversion == "1":       # Converts celsius to fahrenheit
        try:
            celsius = float(input("Insert the amount of celsius: "))
            result = float(celsius * 1.8) + 32
            print(str(result) + " fahrenheit")
        except ValueError:
            print("Error, please enter a valid number")
            run_again = input("Run again? (y),(n)\n")
            if run_again == "y":
                weight()

    elif conversion == "2":     # Converts fahrenheit to celsius
        try:
            fahrenheit = float(input("Insert the amount of fahrenheits: "))
            result = float(fahrenheit - 32) * 0.5556
            print(str(result) + " celsius")
        except ValueError:
            print("Error, please enter a valid number")
            run_again = input("Run again? (y),(n)\n")
            if run_again == "y":
                weight()


if category.lower() == "w":     # Runs the weight function
    weight()

elif category.lower() == "d":     # Runs the distance function
    distance()

elif category.lower() == "t":     # Runs the temperature function
    temperature()

# Error message
else:
    print("Incorrect input")




# Comments:
# Take care of errors
# Make it restart when it ends




