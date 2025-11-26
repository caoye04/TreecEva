data_points = ['A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8', 'I9', 'J0']
cleaned_set = {item.strip().upper() for item in data_points if len(item) == 2}
digit_chars = [char for item in data_points for char in item if char.isdigit()]
digit_count = len(digit_chars)
final_count = len(cleaned_set) + digit_count
print(f"Result: {final_count}")