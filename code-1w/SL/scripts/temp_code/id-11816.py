def evaluate_performance(codes, data):
    # Irrelevant transformation: normalize codes (not used in final logic)
    normalized_codes = [c.strip().upper() for c in codes if len(c) > 2]
    filtered_codes = set([c for c in normalized_codes if c.startswith('P')])

    # Misleading metric calculation
    avg_length = sum(len(c) for c in codes) / len(codes) if codes else 0
    size_penalty = 1 if avg_length > 5 else 0.5

    # Core logic: count valid sales with specific patterns
    valid_sales = 0
    total_revenue = 0.0
    bonus_flag = False

    for entry in data:
        prod_id = entry['id']
        amount = entry['amount']
        region = entry['region']

        # Check if product ID has exactly one digit and ends with 'X'
        digit_count = sum(1 for ch in prod_id if ch.isdigit())
        ends_with_x = prod_id.endswith('X') or prod_id.endswith('x')

        # Distractor: regional adjustment (unused in final score)
        region_multiplier = 1.1 if region == 'NORTH' else 1.0
        adjusted_amount = amount * region_multiplier

        if digit_count == 1 and ends_with_x:
            valid_sales += 1
            total_revenue += amount  # Use original amount, not adjusted

        # Dead code path: never reached due to condition above
        if len(prod_id) > 10 and 'TEST' in prod_id:
            valid_sales -= 1  # Counter-logic that doesn't trigger

    # Another distractor: unused quality score
    quality_score = len(filtered_codes) * 2 if valid_sales > 0 else 0

    # Final scoring logic
    base_score = valid_sales * 100
    revenue_bonus = int(total_revenue // 50)  # Integer division bonus
    final_score = base_score + revenue_bonus - int(size_penalty * 10)

    return final_score

# Input data
product_codes = ['PX1', 'pY2', 'PROD3', 'p4X', 'Px0z']
sales_data = [
    {'id': 'A7X', 'amount': 120.0, 'region': 'SOUTH'},
    {'id': 'BXy', 'amount': 85.5, 'region': 'NORTH'},
    {'id': 'L3X', 'amount': 200.0, 'region': 'EAST'},
    {'id': 'TX1', 'amount': 45.0, 'region': 'WEST'},
    {'id': 'M9X', 'amount': 310.5, 'region': 'NORTH'}
]

# Execution point
final_score = evaluate_performance(product_codes, sales_data)
print(f"Result: {final_score}")