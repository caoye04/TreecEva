from itertools import groupby

def calculate_final_score(raw_data):
    # Preprocess: split and clean entries
    cleaned = [entry.strip() for entry in raw_data.split(',')]
    
    # Extract numeric values from strings like 'P98' -> 98
    numbers = [int(''.join(filter(str.isdigit, x))) for x in cleaned]
    
    # Group consecutive values and sum each group
    grouped_sums = [sum(group) for _, group in groupby(numbers, key=lambda x: x // 10)]
    
    # Apply weighting: higher weight to later groups
    weighted = sum(val * (i + 1) for i, val in enumerate(grouped_sums))
    
    # Final adjustment based on total distinct digits present
    all_digits = ''.join(set(''.join(map(str, numbers))))
    digit_bonus = sum(int(d) for d in all_digits)
    
    final_score = weighted + digit_bonus
    return final_score

# Input data
data = "P98, Q99, R45, S46, T12, U13, V98"
result = calculate_final_score(data)
print(f"Result: {result}")