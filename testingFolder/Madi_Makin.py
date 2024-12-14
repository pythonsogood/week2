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
        newString = initialString + "Madi Makin"
    except: 
        newString = "Error"
    finally:
        return newString
