# You are only allowed to work inside the functions that I provided to you!

def prerequisites () :
    """
        Are you willing to submit this lesson, if yes then change to True?

        Returns:
            bool: True or False.
    """
    return True

def task1 (initialString: str) -> str:
    """
    This function should return the updated string by adding your fullName to it.

    Parameters:
    initialString (str): some random string.

    Returns:
    str: updated string.
    """

    # Perform the task below, change the code inside the try block.:
    try : 
        newString = initialString + "Unknown Profile"
    except: 
        newString = "Error"
    finally:
        return newString
    
def task2(val : int) -> str:
    """
    Perform a calculation: multiply value by 4 and add 20 to the result.
    Return the final value.

    Returns:
    str: result of the calculation.
    """
    result = None

    # Perform the task below, change the code inside the try block.:
    try : 
        # Even though the result is int, you should return it as a string.
        result = str(val * 4 + 20)
    except:
        result= "Error"
    finally:
        return result
    
def task3(age: int) -> str:
    """
    Check if the given age is eligible for voting (age >= 18).

    Parameters:
    age (int): age of a person.

    Returns:
    str: True if eligible, False otherwise.
    """

    # Perform the task below, change the code inside the try block.:
    try : 
        is_eligible = "True" if age >= 18 else "False"
    except:
        is_eligible = "Error"
    finally:
        return is_eligible
