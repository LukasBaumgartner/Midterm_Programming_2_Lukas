# Downlaod text

import requests

def download_book(url):
    """
    Download Frankenstein from Gutenberg URL
    :param url: The URL to download
    :return: None
    """
    response = requests.get(url)
    print(response.status_code)
    with open("Frankenstein.txt", "w", encoding="utf-8") as file:
        file.write(response.text)

download_book("https://www.gutenberg.org/cache/epub/84/pg84.txt")

def longest_un_word(filename):
    """
    Input: filename (string)
    Function made to find the longest word starting with "un"
    I will use Frankenstein book as a text file
    :param filename: string
    :return: longest word starting with "un" (string)
    """

    # I first assign the longest word as an empty string - will change later, and identify all punctuations that may interfere with my code to catch the words
    longest_word = ""
    punctuation = ",.?!:;\\()-[]\"'"

    # Now I need to run the appropiate code to remove capitalization, punctuation, and seperate words
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.lower()

            for p in punctuation:
                line = line.replace(p, "")
            words = line.split()

            # Check for start of "un"
            for word in words:

                if len(word) >= 2:
                    if word[0:2] == "un":

                        # Check that it is longer than current word in string
                        if len(word) > len(longest_word):
                            longest_word = word

    return longest_word

print(longest_un_word("Frankenstein.txt"))
# Longest word is unenforceability