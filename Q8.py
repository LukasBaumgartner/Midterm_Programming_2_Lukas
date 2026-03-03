def days_since_birthday(birthday):
    """
    Input: birthday
    Function checks days passed since birthday,
    Only full years count
    Assumes 365 days in a year.
    :param birthday: string "DD-MM-YYYY"
    :return: number of days (int)
    """

    # slicing the year
    # Format is "DD-MM-YYYY" thus "0123456789"
    # Last does not count, thus [6:10]
    birthstring = birthday[6:10]

    # Convert year to integer
    birth_year = int(birthstring)

    # Full years completed
    full_years = 2026 - 1 - birth_year

    # Assume 365 days in a year
    days = full_years * 365

    return days


print(days_since_birthday("20-11-2005"))
# 7300 days