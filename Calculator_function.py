
import math


def evaluate_expression(expression):
    # Calculating the result of a string expression
    try:
        # The eval function executes the incoming string expression.
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        # Returns the result of the expression calculation
        return result
    except Exception as e:
        # If any exception occurs, an error message is returned
        return "Error: " + str(e)


def compute_sin(angle):
    # Calculate the sine of an angle
    try:
        angle = float(angle) # Converts the incoming angle to a float.
        # Converting angles from degrees to radians.
        # Calculate the sine of the angle
        return math.sin(math.radians(angle))
    except Exception as e:
        # Returns an error message telling the user what went wrong
        return "Error: " + str(e)

def compute_cos(angle):
    # Calculate the cosine of the angle
    try:
        angle = float(angle) #  Converts the incoming angle to a float.
        # Converting angles from degrees to radians.
        # Calculate the cosine of the angle
        return math.cos(math.radians(angle))
    except Exception as e:
        # Returns an error message telling the user what went wrong
        return "Error: " + str(e)
    
def compute_tan(angle):
    # Calculate the tangent of the angle
    try:
        angle = float(angle)
        return math.tan(math.radians(angle))
    except Exception as e:
        return "Error: " + str(e)
    
def compute_arcsin(value):
    # Calculate the arcsine value
    try:
        value = float(value)
        # Checks if the value is within the legal range. 
        # The domain of definition of the sine is [-1, 1].
        if value < -1 or value > 1:
            return "Error: arcsin argument must be between -1 and 1"
        return math.degrees(math.asin(value))
    except Exception as e:
        return "Error: " + str(e)
    
def compute_arccos(value):
    # Calculating the inverse cosine
    try:
        value = float(value)
        # Checks if the value is within the legal range. 
        # The domain of definition of the s is [-1, 1].
        if value < -1 or value > 1:
            return "Error: arccos argument must be between -1 and 1"
        return math.degrees(math.acos(value))
    except Exception as e:
        return "Error: " + str(e)
 
def compute_arctan(value):
    # Calculating the Arctangent
    try:
        value = float(value)
        return math.degrees(math.atan(value))
    except Exception as e:
        return "Error: " + str(e)

def compute_square(value):
    # Calculate the square value
    try:
        return float(value) ** 2
    except Exception as e:
        return "Error: " + str(e)

def compute_sqrt(value):
    # Calculate square root
    try:
        value = float(value)
        # Checks if the value is negative, 
        # negative numbers do not have a real square root
        if value < 0:
            return "Error: sqrt is not defined for negative numbers"
        return math.sqrt(float(value))
    except Exception as e:
        return "Error: " + str(e)
    
