def is_prime(n):
    """Check if a number is prime"""
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

def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def process_data(data_points):
    """Process data points with various transformations"""
    processed = []
    for point in data_points:
        # Apply complex transformation
        transformed = (point * 3) % 100
        # This calculation is never used
        potential = transformed ** 2 - 50
        
        # Only add points that meet certain criteria
        if transformed > 30 and transformed < 80:
            processed.append(transformed)
    
    # Sort for better analysis (not actually needed)
    return sorted(processed)

def analyze_sequence(values, threshold=50):
    """Analyze a sequence of values"""
    above_threshold = [x for x in values if x > threshold]
    below_threshold = [x for x in values if x <= threshold]
    
    # Calculate various metrics (most aren't used)
    metrics = {
        "mean_above": sum(above_threshold) / len(above_threshold) if above_threshold else 0,
        "mean_below": sum(below_threshold) / len(below_threshold) if below_threshold else 0,
        "ratio": len(above_threshold) / len(below_threshold) if below_threshold else float('inf'),
        "product_first_three": values[0] * values[1] * values[2] if len(values) >= 3 else 0
    }
    
    return metrics

def calculate_special_value(data, factor):
    """Calculate a special value based on prime positions in data"""
    # Find indices of prime numbers in the sequence
    prime_indices = [i for i, x in enumerate(data) if is_prime(i)]
    
    # Extract values at prime indices
    prime_values = [data[i] for i in prime_indices if i < len(data)]
    
    # Apply some transformations that don't affect the result
    transformed = [(x + 5) * 2 for x in prime_values]
    reversed_values = prime_values[::-1]
    
    # This is just a distraction
    fibonacci_sum = sum(calculate_fibonacci(i % 10) for i in range(len(prime_values)))
    
    # The actual calculation we care about
    result = 1
    for i, val in enumerate(prime_values):
        if i % factor == 0:  # Only use every 'factor'th value
            result *= val
    
    return result

# Generate some test data
raw_data = [12, 19, 28, 37, 46, 55, 64, 73, 82, 91]

# Apply some preprocessing
scaled_data = [x // 2 + 5 for x in raw_data]

# This is a misleading calculation
misleading_sum = sum(x for x in scaled_data if x % 2 == 0)

# Process the data
processed_data = process_data(scaled_data)

# Analyze the processed data (unused)
analysis_results = analyze_sequence(processed_data)

# Filter the data in a specific way
filtered_data = [x for x in processed_data if x % 2 == 1 or x % 3 == 0]

# Calculate a value based on a different filter (not used)
alternate_data = [x for x in processed_data if x % 4 == 0]
alternate_result = sum(alternate_data) if alternate_data else 0

# The key calculation
prime_product = calculate_special_value(filtered_data, 3)

# Print the result
print(f"Result: {prime_product}")