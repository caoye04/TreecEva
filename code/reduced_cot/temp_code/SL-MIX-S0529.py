def validate_data_entries(entries):
    valid_count = 0
    temp_check = len(entries)  # temporary variable for length check
    
    for entry in entries:
        if entry.strip() and entry.isdigit():
            valid_count += 1
    
    # Process additional entries
    additional_data = ["42", "", "test", "789"]
    additional_entries = sum(1 for item in additional_data if item.strip() and item.isdigit())
    
    # Final calculation
    total_valid = valid_count + additional_entries
    print(f"Result: {total_valid}")

# Main execution
initial_entries = ["123", "", "456", "abc", "789"]
validate_data_entries(initial_entries)