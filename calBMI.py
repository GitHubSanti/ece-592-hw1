"""
@author Santiago Sepulveda

This script is run by running 'py [file directory location]\calBMI.py' from terminal.

Purpose of file is to accomplish the following:

Take the user input for weight in lbs, Height in feet
    Print weight in Kgs, print height in meters
    Calculate Body mass Index = Weight(Kg) / (height (m))^2
    Print BMI

Output should look like
    Weight = ____lbs =  _____ Kg, 
    Height  = ____ feet = ______ m, 
    BMI = _____

"""  

if __name__ == "__main__":    
    weight = input("please provide weight in lbs: ")
    height = input("please provide height in feet: ")

    # Ensure string inputs for weight and height are floats or integers
    try:
        float(weight)
        float(height)
    except ValueError:
        print("Invalid entry")
        exit(-1)

    # For input of zero height or zero weight, print “Invalid weight or height”
    if (float(weight) == 0 or float(weight) == 0.0) or (float(height) == 0 or float(height) == 0.0):
        print("Invalid weight or height")
        exit(0)

    # Convert weight and height to kg and m
    weight_kg = round(float(weight)/2.20462,3)
    height_m = round(float(height)/3.28084,3)

    # Calculate BMI
    BMI = round(weight_kg/height_m**2,3)

    print("Weight = ",weight,"lbs = ",weight_kg," Kg,")
    print("Height  = ",height ,"feet = ",height_m," m,")
    print("BMI = ",BMI)
