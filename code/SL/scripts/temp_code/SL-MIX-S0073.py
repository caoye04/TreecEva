text_data = "programming_evaluation"
filter_chars = "aeiou"

# Process main text data
unique_chars = set(text_data)
filter_set = set(filter_chars)
common_chars = unique_chars.intersection(filter_set)

# Additional character processing
additional_text = "benchmark_test"
additional_chars = set(additional_text)

# Final calculation
final_count = len(unique_chars.union(additional_chars)) - len(common_chars)

# Temporary variable for intermediate step (minimal interference)
temp_check = len(text_data) + len(additional_text)

print(f"Result: {final_count}")