def convestion(Choice):
    if Choice==1:
        print("Choose the type of Conversion You want to perform \n1)Kilograms to grams: \n2)Grams to kilograms: \n3)Grams to milligrams: \n4)Milligrams to grams:")
        choice=int(input("Enter your choice (1/2/3/4): "))
        if choice == 1:
            kg=float(input("Enter the weght in kg:"))
            print(f"your weight in grams is {KilogramsToGrams(kg)}gm")
        elif choice == 2:
            gm=float(input("Enter the weight in gm:"))
            print(f"your weight in kilograms is {GramsToKilograms(gm)}kg")
        elif choice == 3:
            gm=float(input("Enter the weight in gm:"))
            print(f"your weight in milligrams is {GramsToMilligrams(gm)}mg")
        elif choice == 4:
            mg=float(input("Enter the weight in mg:"))
            print(f"your weight in grams is {MilligramsToGrams(mg)}gm")
    elif Choice==2:
        print("Choose the type of Conversion You want to perform \n1) Pounds to ounces: \n2) Ounces to pounds:  \n3) Ounces to grams: \n4)Grams to ounces: ")
        choice2=int(input("Enter your choice (1/2/3/4): "))
        if choice2 == 1:
            lbs=float(input("Enter the weight in lbs:"))
            print(f"your weight in ounces is {PoundsToOunces(lbs)}oz")
        elif choice2 == 2:
            oz=float(input("Enter the weight in oz:"))
            print(f"your weight in pounds is {OuncesToPounds(oz)}lbs")
        elif choice2 == 3:
            oz=float(input("Enter the weight in oz:"))
            print(f"your weight in grams is {OuncesToGrams(oz)}gm")
        elif choice2 == 4:
            gm=float(input("Enter the weight in gm:"))
            print(f"your weight in ounces is {GramsToOunces(gm)}oz")
    elif Choice==3:
        print("Choose the type of Conversion You want to perform \n1) Kilograms to pounds: \n2) Pounds to kilograms: \n3) Grams to ounces: \n4) Ounces to grams:")
        choice3=int(input("Enter your choice (1/2/3/4): "))
        if choice3 == 1:
            kg=float(input("Enter the weight in kg:"))
            print(f"your weight in pounds is {KilogramsToPounds(kg)}lbs")
        elif choice3 == 2:
            lbs=float(input("Enter the weight in lbs:"))
            print(f"your weight in kilograms is {PoundsToKilograms(lbs)}kg")
        elif choice3 == 3:
            gm=float(input("Enter the weight in gm:"))
            print(f"your weight in ounces is {GramsToOuncesMetricToImperial(gm)}oz")
        elif choice3 == 4:
            oz=float(input("Enter the weight in oz:"))
            print(f"your weight in grams is {OuncesToGramsMetricToImperial(oz)}gm")
    return

def KilogramsToGrams(kg):
    return kg*1000
def GramsToKilograms(gm):
    return gm/1000
def GramsToMilligrams(gm):
    return gm*1000
def MilligramsToGrams(mg):
    return mg/1000

def PoundsToOunces(lbs):
    return lbs*16
def OuncesToPounds(oz):
    return oz/16
def OuncesToGrams(oz):
    return oz*28.3495
def GramsToOunces(gm):
    return gm/28.3495

def KilogramsToPounds(kg):
    return kg*2.20462
def PoundsToKilograms(lbs):
    return lbs/2.20462
def OuncesToGramsMetricToImperial(oz):
    return oz/0.035274
def GramsToOuncesMetricToImperial(gm):
    return gm*0.035274

def main():
    while True:
        print("\nWelcome to the weight conversion program")
        print("Choose the type of conversion you want to perform \n1) Metric Conversions: \n2) Imperial Conversions: \n3) Metric to Imperial Conversions:\n4)Exit")
        Choice=int(input("Enter your choice (1/2/3/4): "))
        if Choice>=1 and Choice<=3:
            convestion(Choice)
        elif Choice==4:
            print("Thank you for visiting the weight conversion program")
            break
        else:
            print("Invalid choice. Please choose a valid option")

main()