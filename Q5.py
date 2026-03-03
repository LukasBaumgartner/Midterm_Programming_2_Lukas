import random

# Now to make a list of 10 random numbers between 1 and 100
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Now that numbers have been generated, we must change them to the specfications
# Continue by removing the numbers greater than 50 from the list and replacing them with a random number that is between 20 and 30. Also replace the number lower than 50 with "XX".
# Print the list at the end

for i in range(len(random_numbers)):

    # if number > 50, we must replace with number 20-30
    if random_numbers[i] > 50:
        random_numbers[i] = random.randint(20, 30)

    # else if numbers are < 50, replace with "XX" string
    elif random_numbers[i] < 50:
        random_numbers[i] = "XX"

# Number exactly =50 does not need additional code, as nothing happens (is not classified into if)

# Print result
print(random_numbers)

# My personal result (will change as numbers are random) was:
# ['XX', 22, 'XX', 'XX', 25, 29, 'XX', 'XX', 30, 27]