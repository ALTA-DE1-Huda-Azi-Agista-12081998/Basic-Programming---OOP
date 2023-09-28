def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes_grid(width, height, start):
    result = ""  # This is where we'll build our grid.

    current_number = start  # We start with the given starting number.

    # Loop through each row
    for i in range(height):
        row = ""  # This is where we'll build the numbers for each row.
        
        # Loop through each column in the row
        for j in range(width):
            # Find the next prime number
            while not is_prime(current_number):
                current_number += 1

            # Add the prime number to the row
            row += str(current_number) + ", "
            current_number += 1  # Move to the next number

        # Add the row to the result, removing the trailing comma and space
        result += row.rstrip(", ") + "\n"

    return result

# Sample Test Cases
output1 = generate_primes_grid(2, 3, 13)
print(output1)
# Output:
# 17, 19
# 23, 29
# 31, 37

output2 = generate_primes_grid(5, 2, 1)
print(output2)
# Output:
# 2, 3, 5, 7, 11
# 13, 17, 19, 23, 29
