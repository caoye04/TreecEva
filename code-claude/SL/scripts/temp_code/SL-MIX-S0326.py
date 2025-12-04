def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_factors(num):
    # Calculate all factors (not just prime)
    return [i for i in range(1, num + 1) if num % i == 0]

# Main process starts
target_number = 120
alternative_number = 60

# Get all factors (distraction)
all_factors = get_factors(target_number)
alt_factors = get_factors(alternative_number)

# Generate prime factors
prime_factors = []
temp_num = target_number

# Track some statistics (distraction)
factor_count = 0
largest_prime = 0

# Find prime factors
for i in range(2, target_number + 1):
    while temp_num % i == 0 and is_prime(i):
        prime_factors.append(i)
        temp_num //= i
        factor_count += 1
        largest_prime = max(largest_prime, i)
    if temp_num == 1:
        break

# Some distraction calculations
prime_sum = sum(prime_factors)
factor_product = 1
for f in all_factors[:3]:  # Only use first 3 factors
    factor_product *= f

# Prepare a mapping (distraction)
factor_mapping = {factor: index for index, factor in enumerate(all_factors)}

# Calculate unique prime factors
unique_elements = len(set(prime_factors))

# More calculations (distraction)
composite_value = unique_elements * factor_count - largest_prime

# Generate sequence based on factors (distraction)
sequence = [i*i for i in all_factors if i % 2 == 0]

print(f"Result: {unique_elements}")