
# Palindrome test
# The code is given

# First we need to assign word to the possible choices

word = "7489617719749244646336564429479177169847"

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome(word))

# After trying all the options
# word = "7489617719749244646336564429479177169847" is not a Palindrome