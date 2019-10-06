# import needed libraries
import pytemperature

temperatures_uom_list = ["Kelvin", "Celsius", "Fahrenheit", "Rankine"]
volumes_uom_list = ["liters", "tablespoons", "cubic-inches", "cups", "cubic-feet", "gallons"]

# First validate input_uom value - is it in the specified list of temperature types or volume types?
def validate_input_uom(input_uom):
    isValid = False
    print("input_uom value is: ", format(input_uom))
    # check if input_uom is in temperatures_uom_list
    if(input_uom) in temperatures_uom_list:
        isValid = True
    elif(input_uom) in volumes_uom_list:
        isValid = True
    else:
        print("input_uom value entered is invalid")
    return isValid 

# validate if the target_uom is valid for the specified input_uom
def validate_target_uom(input_uom, target_uom):
    isValid = False
    print("input_uom value is: ", format(input_uom))
    print("target_uom value is: ", format(target_uom))
    # check if input_uom is in temperatures_uom_list
    if(input_uom) in temperatures_uom_list:
        if(target_uom) in temperatures_uom_list:
            isValid = True
    elif(input_uom) in volumes_uom_list:
        if(target_uom) in volumes_uom_list:
            isValid = True
#    else:
#       print("target_uom value entered is invalid")
    return isValid 

# conversion function to convert input_numerical_value from input_uom to target_uom
def convertInputUOM_to_TargetUOM(input_numerical_value, input_uom, target_uom):
    convertedOutput = 0
    if(input_uom) in temperatures_uom_list:
        print("Invoking convertTemperature function")
        convertedOutput = convertTemperature(input_numerical_value, input_uom, target_uom)
        return convertedOutput

def convertTemperature(input_numerical_value, input_uom, target_uom):
    outputTemp = 0.0
    if(input_uom == 'Kelvin'):
        if(target_uom == 'Celsius'):
            outputTemp = pytemperature.k2c(float(input_numerical_value))
        elif(target_uom == 'Fahrenheit'):
            outputTemp = pytemperature.k2f(float(input_numerical_value))
    if(input_uom == 'Celsius'):
        if(target_uom == 'Kelvin'):
            outputTemp = pytemperature.c2k(float(input_numerical_value))
        elif(target_uom == 'Fahrenheit'):
            outputTemp = pytemperature.c2f(float(input_numerical_value))
    if(input_uom == 'Fahrenheit'):
        if(target_uom == 'Kelvin'):
            outputTemp = pytemperature.c2k(float(input_numerical_value))
        elif(target_uom == 'Celsius'):
            outputTemp = pytemperature.c2f(float(input_numerical_value))
    return outputTemp

# def convertVolume(input_numerical_value, input_uom, target_uom):


def inputs(input_numerical_value, input_uom, target_uom, student_numeric_response):
    programConversionOutput = 0
    print("The inputs are: {0}, {1}, {2}, {3}".format(input_numerical_value, input_uom, target_uom, student_numeric_response))
    # validate input_uom
    isInput_UOM_Valid = validate_input_uom(input_uom)
    print("is input_uom value valid?:", format(isInput_UOM_Valid))
    # validate target_uom only if input_uom is valid
    if(isInput_UOM_Valid):
        isTarget_UOM_Valid = validate_target_uom(input_uom, target_uom)
        print("is target_uom value valid?:", format(isTarget_UOM_Valid))
        # invoke convert function only if input_uom and target_uom are valid
        if(isTarget_UOM_Valid):
            programConversionOutput = convertInputUOM_to_TargetUOM(input_numerical_value, input_uom, target_uom)
            print("Program conversion output is", format(programConversionOutput))

    

input_numerical_value = input("Please enter input_numerical_value: ")
input_uom = input("Please enter input_uom: ")
target_uom = input("Please enter target_uom: ")
student_numeric_response = input("Please enter student_numeric_response: ")

inputs(input_numerical_value, input_uom, target_uom, student_numeric_response)



#1.	The teacher must be able to provide an input numerical value, an input unit of measure, a target unit of measure, and a student’s numeric response.
#2.	The system indicates that the response is correct, incorrect, or invalid. To be considered correct, the student’s response must match an authoritative answer after both the student’s response and authoritative answer are rounded to the tenths place. 
