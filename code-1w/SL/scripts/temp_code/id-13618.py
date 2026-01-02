def analyze_product_codes(codes):
    # Initialize tracking variables
    ascii_offsets = [ord(c) - ord('A') for c in 'ABCDE']
    temp_buffer = [0] * len(ascii_offsets)
    for i in range(len(temp_buffer)):
        temp_buffer[i] = ascii_offsets[i] * 2 + i  # Distractor: unused transformed offsets

    # Extract and process product IDs
    raw_ids = [int(code[1:-1]) for code in codes if len(code) > 2 and code[0] == 'P' and code[-1] == 'X']
    
    # Compute intermediate statistics (some irrelevant)
    mean_id = sum(raw_ids) / len(raw_ids) if raw_ids else 0
    variance_proxy = sum((x - mean_id) ** 2 for x in raw_ids) if raw_ids else 0  # Semi-relevant but not used

    # Identify high-value products
    thresholds = {'low': 50, 'medium': 100, 'high': 200}
    category_flags = []
    for pid in raw_ids:
        if pid > thresholds['high']:
            category_flags.append('H')
        elif pid > thresholds['medium']:
            category_flags.append('M')
        else:
            category_flags.append('L')
    
    # Compute product of ID and category weight
    weighted_products = []
    for i, pid in enumerate(raw_ids):
        weight = 3 if category_flags[i] == 'H' else (2 if category_flags[i] == 'M' else 1)
        weighted_products.append(pid * weight)
    
    # Apply filtering condition: only keep products where weighted value has odd digit sum
    def digit_sum(n):
        return sum(int(d) for d in str(abs(n)))
    
    relevant_products = [wp for wp in weighted_products if digit_sum(wp) % 2 == 1]
    
    # Additional distraction: string analysis on original codes
    char_frequency = {}
    for code in codes:
        for char in code:
            if char.isalpha():
                char_frequency[char] = char_frequency.get(char, 0) + 1
    total_letters = sum(char_frequency.values())  # Unused aggregation
    
    # Critical assignment point
    filtered_sum = sum(relevant_products)
    return filtered_sum

# Input data
product_codes = ['P105X', 'P75X', 'P210X', 'P45X', 'P180X', 'P90X']
result = analyze_product_codes(product_codes)
print(f"Result: {result}")