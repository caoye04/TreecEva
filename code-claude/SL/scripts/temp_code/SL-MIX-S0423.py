# Network packet filtering and encryption system

raw_data = [45, 23, 78, 12, 56, 89, 34]
key = 15

# Filter out values above threshold
threshold = 50
filtered_data = [value for value in raw_data if value < threshold]

# Apply some preliminary transformations
processed = [value + 2 for value in filtered_data]
temp_result = sum(processed)

# Encrypt the filtered data using XOR with key
encrypted_value = sum([x ^ key for x in filtered_data])

# Additional operations for verification
verification_code = len(filtered_data) * 3
checksum = encrypted_value % verification_code

print(f"Result: {encrypted_value}")