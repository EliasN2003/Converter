
# CONVERTER


def restart():      # Used to restart the starting function.
    start()
    return


def restart_weight():       # Used to restart the weight function so it doesn't restart itself.
    weight()
    return


def restart_distance():     # Used to restart the distance function so it doesn't restart itself.
    distance()
    return


def restart_temperature():      # Used to restart the temperature function so it doesn't restart itself.
    temperature()
    return


def weight():
    # Selects the conversion method
    conversion = input("Select a conversion method:"
                       "\nKilograms to pounds (1)"
                       "\nPounds to kilograms (2)"
                       "\nGrams to kilograms  (3)"
                       "\nKilograms to grams  (4)"
                       "\nReturn              (5)"
                       "\n>> ")

    if conversion == "1":       # Converts kilograms to pounds
        try:
            kilograms = float(input("Insert the amount of kilograms: "))
            result = float(kilograms) * 2.205
            print(str(result) + " pounds")
        except ValueError:
            print("\n\nPlease enter a valid number\n")     # Prints error message and asks you to enter the value again.
            restart_weight()
            return

    elif conversion == "2":     # Converts pounds to kilograms
        try:
            pounds = float(input("Insert the amount of pounds: "))
            result = float(pounds) / 2.205
            print(str(result) + " kilograms")
        except ValueError:
            print("\n\nPlease enter a valid number\n")
            restart_weight()
            return

    elif conversion == "3":     # Converts grams to kilograms
        try:
            pounds = float(input("Insert the amount of grams: "))
            result = float(pounds) / 1000
            print(str(result) + " kilograms")
        except ValueError:
            print("\n\nPlease enter a valid number\n")
            restart_weight()
            return

    elif conversion == "4":     # Converts kilograms to grams
        try:
            pounds = float(input("Insert the amount of kilograms: "))
            result = float(pounds) * 1000
            print(str(result) + " grams")
        except ValueError:
            print("\n\nPlease enter a valid number\n")
            restart_weight()
            return

    elif conversion == "5":     # Goes back one step in case of miss input
        restart()
        return


    else:
        print("\n\nPlease choose a conversion category\n")     # Prints error message and prompts you to select category again.
        restart_weight()
        return


def distance():
    conversion = input("Select a conversion method:"
                       "\nKilometers to miles (1)"
                       "\nMiles to kilometers (2)"
                       "\nMeters to miles     (3)"
                       "\nMiles to meters     (4)"
                       "\nReturn              (5)"
                       "\n>> ")
    if conversion == "1":       # Converts kilometers to miles
        try:
            kilometers = float(input("Insert the amount of kilometers: "))
            result = float(kilometers) / 1.609
            print(str(result) + " miles")
        except ValueError:
            print("\n\nPlease enter a valid number")
            restart_distance()
            return

    elif conversion == "2":     # Converts miles to kilometers
        try:
            miles = float(input("Insert the amount of miles: "))
            result = float(miles) * 1.609
            print(str(result) + " kilometers")
        except ValueError:
            print("\n\nPlease enter a valid number")
            restart_distance()
            return

    elif conversion == "3":     # Converts meters to miles
        try:
            miles = float(input("Insert the amount of meters: "))
            result = float(miles) / 1609
            print(str(result) + " miles")
        except ValueError:
            print("\n\nPlease enter a valid number")
            restart_distance()
            return

    elif conversion == "4":     # Converts miles to meters
        try:
            miles = float(input("Insert the amount of miles: "))
            result = float(miles) * 1609
            print(str(result) + " meters")
        except ValueError:
            print("\n\nPlease enter a valid number")
            restart_distance()
            return

    elif conversion == "5":     # Goes back one step in case of miss input
        restart()
        return


    else:
        print("\n\nPlease choose a conversion category")
        restart_distance()
        return


def temperature():
    conversion = input("Select a conversion method:"
                       "\nCelsius to fahrenheit (1)"
                       "\nFahrenheit to celsius (2)"
                       "\nKelvin to celsius     (3)"
                       "\nCelsius to kelvin     (4)"
                       "\nReturn                (5)"
                       "\n>> ")
    if conversion == "1":       # Converts celsius to fahrenheit
        try:
            celsius = float(input("Insert the amount of celsius: "))
            result = float(celsius * 1.8) + 32
            print(str(result) + " fahrenheit")
        except ValueError:
            print("\n\nPlease enter a valid number")
            restart_temperature()
            return

    elif conversion == "2":     # Converts fahrenheit to celsius
        try:
            fahrenheit = float(input("Insert the amount of fahrenheits: "))
            result = float(fahrenheit - 32) * 0.5556
            print(str(result) + " celsius")
        except ValueError:
            print("\n\nPlease enter a valid number")
            restart_temperature()
            return

    elif conversion == "3":     # Converts kelvin to celsius
        try:
            fahrenheit = float(input("Insert the amount of kelvins: "))
            result = float(fahrenheit) - 273.15
            print(str(result) + " celsius")
        except ValueError:
            print("\n\nPlease enter a valid number")
            restart_temperature()
            return

    elif conversion == "4":     # Converts celsius to kelvins
        try:
            fahrenheit = float(input("Insert the amount of celsius: "))
            result = float(fahrenheit) + 273.15
            print(str(result) + " kelvins")
        except ValueError:
            print("\n\nPlease enter a valid number")
            restart_temperature()
            return

    elif conversion == "5":     # Goes back one step in case of miss input
        restart()
        return


    else:
        print("\n\nPlease choose a conversion category")
        restart_temperature()
        return


def start():
    print("\n__CONVERTER PROGRAM__")
    category = input("Select a category:\nWeight (w)\nDistance (d)\nTemperature (t)\n>> ")  # Select the category for a conversion

    if category.lower() == "w":     # Runs the weight conversion function
        weight()

    elif category.lower() == "d":     # Runs the distance conversion function
        distance()

    elif category.lower() == "t":     # Runs the temperature conversion function
        temperature()

    else:
        print("\n\nError, please select a category for conversion")
        if input("Run again? (y)\n") == "y":
            restart()       # Restarts the program
            return


start()     # Starts the program for the first time.

