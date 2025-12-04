# Processing sensor data with bitwise filtering

values = [24, 18, 33, 16, 42, 9, 51]

# Initialize processing parameters
mask = 8  # Bit mask for checking specific sensor flag
threshold = 20
valid_count = sum(1 for v in values if v > threshold)

# Apply bitwise filtering to identify sensors with specific flag set
filtered_count = len(list(filter(lambda x: x & mask > 0, values)))

# Additional data analysis
data_slice = values[1:5]  # Extract middle section
average = sum(data_slice) / len(data_slice)

# Format and display results
result_text = "Sensor analysis complete".upper()
print(f"Result: {filtered_count}")