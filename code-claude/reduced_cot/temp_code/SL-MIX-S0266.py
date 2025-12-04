def process_text(text):
    # Process text to extract numeric values
    words = text.lower().split()
    extracted = [int(word) for word in words if word.isdigit()]
    return extracted

def calculate_average(numbers):
    # Calculate average of numbers
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def calculate_product(data):
    # Calculate product of values in data
    result = 1
    for item in data:
        result *= item
    return result

# Sample text containing some numeric values
raw_text = "The 3 scientists examined 7 samples over 2 weeks"
processed_data = process_text(raw_text)

# Perform operations on the data
total_sum = sum(processed_data)
max_value = max(processed_data) if processed_data else 0

# Create a set of unique values and apply transformations
unique_values = set(processed_data)
transformed = list(map(lambda x: x**2 - 1, unique_values))

# Filter data based on condition
threshold = 5
filtered_data = [x for x in processed_data if x < threshold]

# Apply string operations to generate more data
text_values = "4,1,9,16"
bonus_data = [int(x) for x in text_values.split(',')]

# Calculate statistics that won't affect final result
average = calculate_average(processed_data)
median_position = len(processed_data) // 2
potential_median = sorted(processed_data)[median_position] if processed_data else 0

# Calculate the product of filtered data
product_value = calculate_product(filtered_data)

# Generate output string
output = f"Analysis complete with {len(processed_data)} values"
result_message = f"Result: {product_value}"

print(result_message)