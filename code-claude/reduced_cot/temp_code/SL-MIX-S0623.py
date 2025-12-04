import itertools

def calculate_product_pairs(numbers):
    # Generate all possible pairs from the list
    all_pairs = list(itertools.combinations(numbers, 2))
    # Calculate products of pairs
    products = [a * b for a, b in all_pairs]
    return products

# Primary sensor readings (temperature values)
primary_readings = {23, 25, 28, 30, 32}

# Secondary sensor readings (temperature values)
secondary_readings = {22, 25, 29, 30, 33}

# Find common readings between sensors
shared_elements = primary_readings.intersection(secondary_readings)

# Count of overlapping readings
overlap_count = len(shared_elements)

# Calculate temperature adjustment factor
adjustment_factor = 2

# Apply lambda function to adjust temperatures
adjusted_primary = set(map(lambda x: x + adjustment_factor, primary_readings))

# For reporting purposes
average_reading = sum(primary_readings) / len(primary_readings)

print(f"Result: {overlap_count}")