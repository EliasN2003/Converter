
# CONVERTER


def weight():
    while True:
        # Selects the conversion method
        conversion = input("\nSelect a conversion method:"
                           "\nKilograms to pounds (1)"
                           "\nPounds to kilograms (2)"
                           "\nGrams to kilograms  (3)"
                           "\nKilograms to grams  (4)"
                           "\nReturn              (5)"
                           "\n>> ")
        while True:
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
                break


def distance():
    while True:
        conversion = input("\nSelect a conversion method:"
                           "\nKilometers to miles (1)"
                           "\nMiles to kilometers (2)"
                           "\nMeters to miles     (3)"
                           "\nMiles to meters     (4)"
                           "\nReturn              (5)"
                           "\n>> ")
        while True:
            # Converts kilometers to miles
            if conversion == "1":
                try:
                    kilometers = float(input("Insert the amount of kilometers: "))
                    result = kilometers / 1.609
                    print(str(result) + " miles")
                    break
                except ValueError:
                    print("\n\nPlease enter a valid number")
                    continue

            # Converts miles to kilometers
            elif conversion == "2":
                try:
                    miles = float(input("Insert the amount of miles: "))
                    result = miles * 1.609
                    print(str(result) + " kilometers")
                    break
                except ValueError:
                    print("\n\nPlease enter a valid number")
                    continue

            # Converts meters to miles
            elif conversion == "3":
                try:
                    miles = float(input("Insert the amount of meters: "))
                    result = miles / 1609
                    print(str(result) + " miles")
                    break
                except ValueError:
                    print("\n\nPlease enter a valid number")
                    continue

            # Converts miles to meters
            elif conversion == "4":
                try:
                    miles = float(input("Insert the amount of miles: "))
                    result = miles * 1609
                    print(str(result) + " meters")
                    break
                except ValueError:
                    print("\n\nPlease enter a valid number")
                    continue

            # Goes back one step in case of miss input
            elif conversion == "5":
                start()


            else:
                print("\n\nPlease choose a conversion category\n")
                break


def temperature():
    while True:
        conversion = input("\nSelect a conversion method:"
                           "\nCelsius to fahrenheit (1)"
                           "\nFahrenheit to celsius (2)"
                           "\nKelvin to celsius     (3)"
                           "\nCelsius to kelvin     (4)"
                           "\nReturn                (5)"
                           "\n>> ")
        while True:
            # Converts celsius to fahrenheit
            if conversion == "1":
                try:
                    celsius = float(input("Insert the amount of celsius: "))
                    result = celsius * 1.8 + 32
                    print(str(result) + " fahrenheit")
                    break
                except ValueError:
                    print("\n\nPlease enter a valid number")
                    continue

            # Converts fahrenheit to celsius
            elif conversion == "2":
                try:
                    fahrenheit = float(input("Insert the amount of fahrenheits: "))
                    result = fahrenheit - 32 * 0.5556
                    print(str(result) + " celsius")
                    break
                except ValueError:
                    print("\n\nPlease enter a valid number")
                    continue

            # Converts kelvin to celsius
            elif conversion == "3":
                try:
                    fahrenheit = float(input("Insert the amount of kelvins: "))
                    result = fahrenheit - 273.15
                    print(str(result) + " celsius")
                    break
                except ValueError:
                    print("\n\nPlease enter a valid number")
                    continue

            # Converts celsius to kelvins
            elif conversion == "4":
                try:
                    fahrenheit = float(input("Insert the amount of celsius: "))
                    result = fahrenheit + 273.15
                    print(str(result) + " kelvins")
                    break
                except ValueError:
                    print("\n\nPlease enter a valid number")
                    continue

            # Goes back one step in case of miss input
            elif conversion == "5":
                start()


            else:
                print("\n\nPlease choose a conversion category")
                break


def start():
    while True:
        print("\n__CONVERTER PROGRAM__")
        # Select the category for a conversion
        category = input("Select a category:\nWeight (w)\nDistance (d)\nTemperature (t)\nQuit (enter)\n>> ")

        # Runs the weight conversion function
        if category.lower() == "w":
            weight()

        # Runs the distance conversion function
        elif category.lower() == "d":
            distance()

        # Runs the temperature conversion function
        elif category.lower() == "t":
            temperature()

        # Quits the program if you don't select a category
        else:
            quit()


# Starts the program for the first time
start()
