
# Write a function that checks if the passed parameter is a valid URL or not using things we used in class
# A URL is valid if:
# It starts with http:// or https://
# The following domain must not be: empty, have at least one dot.
# There is no space anywhere in URL.

def is_valid_url(url):
    """
    Input: url (string)
    Create a function that checks if the parameter is a valid URL.
    checks for:
    - string
    - start of: "http://" or "https://"
    - contain at least one dot "."
    - contain no spaces
    :param url: string
    :return: True if valid, False otherwise
    """

    # Begin by checking if URL is a string
    if type(url) != str:
        return False

    # 2) Check for space
    if url.count(" ") != 0:
        return False

    # 3) Check prefix
    starts_http = False
    starts_https = False

    if len(url) >= 7:
        if url[0:7] == "http://":
            starts_http = True

    if len(url) >= 8:
        if url[0:8] == "https://":
            starts_https = True

    if starts_http == False and starts_https == False:
        return False

    # 4) Check for at least one dot
    if url.count(".") == 0:
        return False

    return True

# Testing code
print(is_valid_url("https://google.com"))   # True
print(is_valid_url("http://ie.edu"))        # True
print(is_valid_url("google.com"))           # False
print(is_valid_url("https://google com"))   # False
print(is_valid_url(123))                    # False