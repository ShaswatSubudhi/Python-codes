def conversion(chooice,temprature):
    if chooice ==1:
        CelsiusToFahrenheit(temprature)
    elif chooice ==2:
        FahrenheitToCelsius(temprature)
    elif chooice ==3:
        CelsiusToKelvin(temprature)
    elif chooice ==4:
        KelvinToCelsius(temprature)
    elif chooice ==5:
        FahrenheitToKelvin(temprature)
    elif chooice ==6:
        KelvinToFahrenheit(temprature)
    return

def CelsiusToFahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"your temprature in Fahrenheit is {fahrenheit}F")
    return

def FahrenheitToCelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    print(f"your temprature in Celsius is {celsius}C")
    return

def CelsiusToKelvin(celsius):
    kelvin = celsius + 273.15
    print(f"your temprature in Kelvin is {kelvin}K")
    return

def KelvinToCelsius(kelvin):
    celsius = kelvin - 273.15
    print(f"your temprature in Celsius is {celsius}C")
    return

def FahrenheitToKelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273.
    print(f"your temprature in Kelvin is {kelvin}K")
    return

def KelvinToFahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    print(f"your temprature in Fahrenheit is {fahrenheit}F")
    return

def main():
    print("Temperature Conversion Program")
    while True:
        print("\nChoose the type of Conversion You want to perform \n1) Celsius to Fahrenheit: \n2) Fahrenheit to Celsius: \n3) Celsius to Kelvin: \n4) Kelvin to Celsius: \n5) Fahrenheit to Kelvin:  \n6) Kelvin to Fahrenheit:")
        print("Enter 0 to exit the program")
        choice=int(input("Enter your choice (0/1/2/3/4/5/6): "))
        if choice == 0:
            break
        elif choice>=1 and choice<=6:
            temprature=float(input("Enter the temprature you want to convert: "))
            conversion(choice, temprature)
        else:
            print("Invalid choice. Please try again.")
main()
