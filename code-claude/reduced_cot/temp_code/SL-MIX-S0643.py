# Calculate sum of prime numbers in a temperature range

# Temperature readings for different hours
temperatures = [12, 15, 17, 19, 23, 21, 18, 16]

# Helper function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Filter temperatures that are prime numbers
prime_temps = [temp for temp in temperatures if is_prime(temp)]

# Apply correction factor for sensor calibration
correction = 2
adjusted_temps = list(map(lambda x: x - correction, prime_temps))

# Filter values above threshold
threshold = 14
lambda_filter = filter(lambda x: x > threshold, adjusted_temps)

# Calculate sum of filtered values
filtered_sum = sum(lambda_filter)

# Display result
print(f"Result: {filtered_sum}")