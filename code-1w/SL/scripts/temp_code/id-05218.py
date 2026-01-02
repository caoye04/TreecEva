import itertools

def validate_code(code):
    # Validates if code has alternating digits and letters
    return all(c.isdigit() if i % 2 == 0 else c.isalpha() for i, c in enumerate(code)) and len(code) == 6

def calculate_bonus(sales_list):
    base_bonus = sum(sales_list) * 0.05
    extra = 0
    if len(sales_list) > 5:
        extra += 100
    peak_day = max(sales_list)
    if peak_day > 800:
        extra += 50
    return base_bonus + extra

def analyze_trend(data):
    # Irrelevant trend analysis (distractor)
    increasing = sum(1 for i in range(1, len(data)) if data[i] > data[i-1])
    decreasing = sum(1 for i in range(1, len(data)) if data[i] < data[i-1])
    return 'upward' if increasing > decreasing else 'downward'

def filter_relevant_codes(codes):
    # Only some codes are valid
    return [c for c in codes if validate_code(c)]

def compute_stability_index(seq):
    # Another distractor function
    diffs = [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))]
    return round(sum(diffs) / len(diffs), 2) if diffs else 0

def evaluate_performance(product_codes, sales_data):
    # Main logic starts here
    valid_codes = filter_relevant_codes(product_codes)
    
    # Simulate daily performance tracking
    daily_scores = []
    for day_sales in sales_data:
        bonus = calculate_bonus(day_sales)
        trend = analyze_trend(day_sales)  # Computed but not used directly
        stability = compute_stability_index(day_sales)  # Distractor computation
        score = bonus + len(valid_codes) * 10
        if trend == 'upward':
            score += 20
        daily_scores.append(score)
    
    # Aggregate total using itertools.chain to flatten
    all_sales_flat = list(itertools.chain(*sales_data))
    global_avg = sum(all_sales_flat) / len(all_sales_flat)
    
    # Final adjustment based on average performance
    adjustment_factor = 1.1 if global_avg > 600 else 0.9
    final_score = sum(daily_scores) * adjustment_factor
    
    # Extra string processing (semi-relevant)
    code_string = ''.join(valid_codes)
    uppercase_count = sum(1 for c in code_string if c.isupper())
    final_score -= uppercase_count * 2  # Small correction

    # Red herring: unused variable
    hypothetical_max = len(valid_codes) * 1000
    
    return int(final_score)

# Input data
product_codes = ['A1B2C3', 'X9Y8Z7', 'invalid', 'M5N4O3', '12X34Y']
sales_data = [
    [500, 620, 700, 810, 780, 850],
    [400, 550, 600, 610, 590, 620],
    [700, 720, 740, 730, 760, 780]
]

# Execution point of interest
final_score = evaluate_performance(product_codes, sales_data)
print(f"Result: {final_score}")