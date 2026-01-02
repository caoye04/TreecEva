def final_outcome(data):
    processed = data[1:-1]  # Slice to remove first and last elements
    total = sum(processed)
    threshold = 10
    is_valid = len(processed) > 2 and total % 7 == 0
    adjustment = 5 if is_valid else -3
    return total + adjustment

raw_data = [3, 6, 8, 7, 9, 1]
modified_data = raw_data[::-1]  # Reverse the list
balance = final_outcome(modified_data)
print(f"Result: {balance}")