def is_prime(n):
    """Check if a number is prime."""
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

def calculate_entropy(values):
    """Calculate Shannon entropy of a sequence."""
    total = sum(values)
    if total == 0:
        return 0
    probabilities = [v/total for v in values if v > 0]
    return -sum(p * (p ** 0.5) for p in probabilities)

# Sensor data analysis for geological samples
sensor_readings = [
    [12, 45, 23, 9, 17],
    [8, 29, 31, 11, 19],
    [22, 37, 13, 41, 7],
    [5, 43, 25, 39, 15]
]

# Filtering parameters
threshold = 20
weight_factors = [0.8, 1.2, 0.7, 1.5, 0.9]

# Data processing
weighted_data = []
for reading in sensor_readings:
    weighted = [r * w for r, w in zip(reading, weight_factors)]
    weighted_data.append(weighted)

# Extract relevant slices for analysis
slice1 = [row[1:4] for row in weighted_data]  # Misleading slice
slice2 = [row[::2] for row in weighted_data]  # Key slice for later use

# Calculate statistical measures
mean_values = [sum(row)/len(row) for row in weighted_data]
max_readings = [max(row) for row in weighted_data]
min_readings = [min(row) for row in weighted_data]

# Distractor operations
entropy_values = [calculate_entropy(row) for row in weighted_data]
transposed_data = list(zip(*weighted_data))
column_sums = [sum(col) for col in transposed_data]

# Filter data based on statistical properties
filtered_indices = set()
for i, (mean, max_val) in enumerate(zip(mean_values, max_readings)):
    if mean > threshold or max_val > 50:
        filtered_indices.add(i)

# More distracting calculations
pattern_strength = sum(max_readings) - sum(min_readings)
density_factor = pattern_strength / (sum(mean_values) + 1)

# Apply complex filtering
filtered_data = []
for i, row in enumerate(weighted_data):
    if i in filtered_indices:
        filtered_data.append([x for x in row if x > threshold/2])
    else:
        # This branch is actually never taken due to our filtered_indices
        adjusted_row = [x * density_factor for x in row]
        filtered_data.append([x for x in adjusted_row if x < threshold*2])

# Extract prime numbers from slice2 (the key operation)
def extract_primes(data_slice):
    flattened = [int(val) for sublist in data_slice for val in sublist]
    return [num for num in flattened if is_prime(num)]

# Misleading function that won't be used for final result
def calculate_harmonic_series(values, limit):
    result = 0
    for i, v in enumerate(values):
        if i >= limit:
            break
        if v != 0:
            result += 1/v
    return result

# The key function that produces our answer
def calculate_prime_influence(data):
    prime_candidates = extract_primes(slice2)
    
    # Find unique primes and their product
    unique_primes = set(prime_candidates)
    product = 1
    for prime in unique_primes:
        product *= prime
    
    return product % 10000  # Keep the result manageable

# More distractor calculations
harmonic_result = calculate_harmonic_series(column_sums, 3)
correlation_index = sum(entropy_values) / pattern_strength

# The key calculation that produces our answer
prime_product = calculate_prime_influence(filtered_data)

# Final misleading calculations
final_score = (harmonic_result * correlation_index) + (prime_product / 1000)
quality_metric = (sum(column_sums) / prime_product) * pattern_strength

print(f"Result: {prime_product}")