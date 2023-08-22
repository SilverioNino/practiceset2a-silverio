def is_leap_year(year):
    """
    Determine whether a given year is a leap year or not.
    
    Parameters:
    year (int): The year to check.
    
    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False






