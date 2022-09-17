
# CONVERTER


def weight():
    while True:
        # Selects the conversion method
        conversion = input("Select a conversion method:"
                           "\nKilograms to pounds (1)"
                           "\nPounds to kilograms (2)"
                           "\nGrams to kilograms  (3)"
                           "\nKilograms to grams  (4)"
                           "\nReturn              (5)"
                           "\n>> ")

        # Converts kilograms to pounds
        if conversion == "1":
            try:
                kilograms = float(input("Insert the amount of kilograms: "))
                result = kilograms * 2.205
                print(str(result) + " pounds")
                break

            # Prints error message and asks you to enter the value again
            except ValueError:
                print("\n\nPlease enter a valid number\n")
                continue

        # Converts pounds to kilograms
        elif conversion == "2":
            try:
                pounds = float(input("Insert the amount of pounds: "))
                result = pounds / 2.205
                print(str(result) + " kilograms")
                break

            except ValueError:
                print("\n\nPlease enter a valid number\n")
                continue

        # Converts grams to kilograms
        elif conversion == "3":
            try:
                pounds = float(input("Insert the amount of grams: "))
                result = pounds / 1000
                print(str(result) + " kilograms")
                break

            except ValueError:
                print("\n\nPlease enter a valid number\n")
                continue

        # Converts kilograms to grams
        elif conversion == "4":
            try:
                pounds = float(input("Insert the amount of kilograms: "))
                result = pounds * 1000
                print(str(result) + " grams")
                break

            except ValueError:
                print("\n\nPlease enter a valid number\n")
                continue

        # Goes back one step in case of miss input
        elif conversion == "5":
            start()

        # Prints error message and prompts you to select category again
        else:
            print("\n\nPlease choose a conversion category\n")
            weight()


def distance():
    while True:
        conversion = input("Select a conversion method:"
                           "\nKilometers to miles (1)"
                           "\nMiles to kilometers (2)"
                           "\nMeters to miles     (3)"
                           "\nMiles to meters     (4)"
                           "\nReturn              (5)"
                           "\n>> ")
        while True:
            if conversion == "1":       # Converts kilometers to miles
                try:
                    kilometers = float(input("Insert the amount of kilometers: "))
                    result = kilometers / 1.609
                    print(str(result) + " miles")
                    break
                except ValueError:
                    print("\n\nPlease enter a valid number")
                    continue

            elif conversion == "2":     # Converts miles to kilometers
                try:
                    miles = float(input("Insert the amount of miles: "))
                    result = miles * 1.609
                    print(str(result) + " kilometers")
                    break
                except ValueError:
                    print("\n\nPlease enter a valid number")
                    continue

            elif conversion == "3":     # Converts meters to miles
                try:
                    miles = float(input("Insert the amount of meters: "))
                    result = miles / 1609
                    print(str(result) + " miles")
                    break
                except ValueError:
                    print("\n\nPlease enter a valid number")
                    continue

            elif conversion == "4":     # Converts miles to meters
                try:
                    miles = float(input("Insert the amount of miles: "))
                    result = miles * 1609
                    print(str(result) + " meters")
                    break
                except ValueError:
                    print("\n\nPlease enter a valid number")
                    continue

            elif conversion == "5":     # Goes back one step in case of miss input
                restart()
                return


            else:
                print("\n\nPlease choose a conversion category")
                restart_distance()


def temperature():
    while True:
        conversion = input("Select a conversion method:"
                           "\nCelsius to fahrenheit (1)"
                           "\nFahrenheit to celsius (2)"
                           "\nKelvin to celsius     (3)"
                           "\nCelsius to kelvin     (4)"
                           "\nReturn                (5)"
                           "\n>> ")
        while True:
            if conversion == "1":       # Converts celsius to fahrenheit
                try:
                    celsius = float(input("Insert the amount of celsius: "))
                    result = celsius * 1.8 + 32
                    print(str(result) + " fahrenheit")
                    break
                except ValueError:
                    print("\n\nPlease enter a valid number")
                    restart_temperature()
                    return

            elif conversion == "2":     # Converts fahrenheit to celsius
                try:
                    fahrenheit = float(input("Insert the amount of fahrenheits: "))
                    result = fahrenheit - 32 * 0.5556
                    print(str(result) + " celsius")
                except ValueError:
                    print("\n\nPlease enter a valid number")
                    restart_temperature()
                    return

            elif conversion == "3":     # Converts kelvin to celsius
                try:
                    fahrenheit = float(input("Insert the amount of kelvins: "))
                    result = fahrenheit - 273.15
                    print(str(result) + " celsius")
                except ValueError:
                    print("\n\nPlease enter a valid number")
                    restart_temperature()
                    return

            elif conversion == "4":     # Converts celsius to kelvins
                try:
                    fahrenheit = float(input("Insert the amount of celsius: "))
                    result = fahrenheit + 273.15
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


def start():
    while True:
        print("\n__CONVERTER PROGRAM__")
        # Select the category for a conversion
        category = input("Select a category:\nWeight (w)\nDistance (d)\nTemperature (t)\n>> ")

        # Runs the weight conversion function
        if category.lower() == "w":
            weight()
            break

        # Runs the distance conversion function
        elif category.lower() == "d":
            distance()
            break

        # Runs the temperature conversion function
        elif category.lower() == "t":
            temperature()
            break

        else:
            print("\n\nError, please select a category for conversion")
            if input("Run again? (y)\n") == "y":
                continue

            else:
                break


# Starts the program for the first time
start()
