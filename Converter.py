
# CONVERTER PROJECT 

category = input("Select the category you want to make a conversion:\nWeight (w)\nTemperature (t)\nDistance (d)\n:")

if category.lower() == "w":
    weight = str(input("Select the weight unit you want to convert from:\nKilograms (k)\nPounds (p)\n:"))
    weight_unit = str(input("Select the weight unit you want to convert to:\nKilograms (k)\nPounds (p)\n:"))
    if weight or weight_unit != "k" or "p":
        print("Wrong letter selected")
    if weight == "k" and weight_unit == "p":
        kilograms = input("Insert the amount of kilograms you want to convert: ")
        weight_result = float(kilograms) * 2.205
        print("Weight is " + str(weight_result) + " lbs")
    elif weight == "p" and weight_unit == "k":
        pounds = input("Insert the amount of pounds you want to convert: ")
        weight_result2 = float(pounds) * 0.453
        print("Weight is " + str(weight_result2) + " kgs")

elif category.lower() == "t":
    temperature = input("Select the temperature unit you want to convert from:\nCelsius (c)\nFahrenheit (f)\n:")
    temperature_unit = input("Select the temperature unit you want to convert from:\nCelsius (c)\nFahrenheit (f)\n:")
    if temperature or temperature_unit != "c" or "f":
        print("Wrong letter selected")
    if temperature.lower() == "c" and temperature_unit.lower() == "f":
        Celsius = input("Insert the temperature in Celsius you want to convert: ")
        temperature_result = float(Celsius) * 1.8 + 32
        print("Temperature is " + str(temperature_result) + " degrees fahrenheit")
    if temperature.lower() == "f" and temperature_unit.lower() == "c":
        Fahrenheits = float(input("Insert the temperature in Fahrenheits you want to convert: "))
        temperature_result2 = (Fahrenheits - 32) * 0.5556
        print("Temperature is " + str(temperature_result2) + " degrees Celsius")

elif category.lower() == "d":
    distance = input("Select the distance unit you want to convert from:\nKilometers (k)\nMiles (m)")
    distance_unit = input("Select the distance unit you want to convert to:\nKilometers (k)\nMiles (m)")
    if distance or distance_unit != "k" or "m":
        print("Wrong letter selected")
    if distance == "k" and distance_unit == "m":
        kilometers = float(input("Insert the distance you want to convert to Miles: "))
        distance_result = kilometers / 1.609
        print("Distance is " + str(distance_result) + " miles")
    if distance == "m" and distance_unit == "k":
        Miles = float(input("Insert the distance you want to convert to Kilometers: "))
        distance_result2 = Miles * 1.609
        print("Distance is " + str(distance_result2) + " kilometers")

else:
    print("End")


# Comments:
# Could we implement a function instead of if's?
