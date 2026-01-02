def evaluate_performance(codes, data):
    # Mapping product categories by code patterns
    luxury_prefix = {'LX', 'PRM', 'ULT'}
    budget_set = {'ECO', 'BAS', 'STD'}
    
    # Irrelevant tracking variables (distractors)
    total_entries = len(data)
    invalid_count = 0
    peak_sale = float('-inf')
    normalized_factor = 0.0
    
    # Precompute thresholds
    average_sale = sum(entry['amount'] for entry in data) / total_entries if total_entries > 0 else 0
    adjustment_rate = 1.1 if average_sale > 200 else 0.9
    
    # Categorize and score
    premium_count = 0
    volume_map = {}
    category_tally = {'luxury': 0, 'standard': 0}
    
    for code in codes:
        prefix = code[:3]
        base_key = code[3:]
        
        # Dummy normalization (not used later)
        if prefix in luxury_prefix:
            normalized_factor += 0.25
        elif prefix in budget_set:
            normalized_factor -= 0.15
        
        # Actual categorization
        if prefix in luxury_prefix:
            category_tally['luxury'] += 1
            premium_count += 1
        else:
            category_tally['standard'] += 1

        # Track volumes by suffix (semi-relevant)
        if base_key in volume_map:
            volume_map[base_key] += 1
        else:
            volume_map[base_key] = 1

    # Compute performance metrics from sales data
    high_performers = 0
    cumulative_delta = 0.0
    volatility_index = 0.0
    
    for record in data:
        amount = record['amount']
        region = record['region'].upper()
        
        # Update peak (distractor)
        if amount > peak_sale:
            peak_sale = amount
        
        # Logical condition affecting performance
        if amount > average_sale * 1.2:
            high_performers += 1
            
        # Volatility metric (unused in final result)
        deviation = abs(amount - average_sale)
        volatility_index += deviation * 0.01

    # Simulated case conversion for region classification (irrelevant path)
    region_classes = set()
    for record in data:
        rc = record['region'].lower()
        if rc in ['north', 'south']:
            region_classes.add(rc.title())
        else:
            region_classes.add('Other')
    
    # Core logic: performance score
    base_score = premium_count * 25 + high_performers * 15
    
    # Apply adjustment based on average sale trend
    if adjustment_rate > 1.0:
        base_score = int(base_score * adjustment_rate)
    
    # Penalty for low volume diversity
    unique_products = len(volume_map)
    if unique_products < 4:
        base_score -= 10
    
    # Final computation
    stability_bonus = 5 if category_tally['luxury'] >= 2 else 0
    final_score = base_score + stability_bonus
    
    # Dead code: unused diagnostic print
    # debug_info = f'Score breakdown: {base_score=}, {stability_bonus=}'
    
    return final_score

# Input data
product_codes = ['LX7A', 'PRM9B', 'STD3X', 'ULT1Z', 'ECO5M', 'LX8K']
sales_data = [
    {'amount': 250, 'region': 'North'},
    {'amount': 180, 'region': 'South'},
    {'amount': 320, 'region': 'East'},
    {'amount': 150, 'region': 'West'},
    {'amount': 275, 'region': 'north'},
    {'amount': 190, 'region': 'SOUTH'}
]

# Execution point
final_score = evaluate_performance(product_codes, sales_data)
print(f"Target result: {final_score}")