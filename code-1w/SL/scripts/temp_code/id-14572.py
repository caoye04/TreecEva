def analyze_investment_flow(transactions, user_weights):
    base_offset = 10
    cumulative_shift = 0
    temp_results = []
    intermediate_products = []

    for idx, (amount, weight) in enumerate(zip(transactions, user_weights)):
        shifted_amount = amount + (base_offset * (idx % 3))
        weighted_value = shifted_amount * weight
        
        if shifted_amount > 50:
            temp_results.append(weighted_value)
            
        # Dead code path – misleading computation
        if weight < 0.5:
            hypothetical = shifted_amount ** 0.5
            intermediate_products.append(hypothetical)

    # Irrelevant set operation – distractor
    unique_temps = set(temp_results)
    temp_sum = sum(unique_temps)

    adjustment_factor = 0.8 if len(temp_results) > 3 else 1.0
    adjusted_values = [val * adjustment_factor for val in temp_results]

    # Slicing to simulate data windowing – semi-relevant but not final
    windowed = adjusted_values[1:4] if len(adjusted_values) > 3 else adjusted_values

    aggregate_total = 0
    for v in windowed:
        aggregate_total += v
        # Bitwise red herring – no impact on result
        debug_flag = v & 1

    # Key filtering logic with slicing and conditional logic
    filtered_contributions = []
    for val in temp_results:
        normalized = val / (max(temp_results) + 1e-8)
        if normalized >= 0.3:
            filtered_contributions.append(int(val))

    threshold_balance = sum(filtered_contributions)
    
    # Extraneous final computation – does not affect answer
    final_score = threshold_balance ^ 255 if threshold_balance > 100 else threshold_balance | 10
    
    print(f"Result: {threshold_balance}")

# Inputs
transaction_data = [45, 60, 75, 52, 30]
weights = [0.7, 0.9, 1.1, 0.6, 0.4]

analyze_investment_flow(transaction_data, weights)