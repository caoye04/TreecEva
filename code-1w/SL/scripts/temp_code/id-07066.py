def calculate_final_score(records, importance_weights):
    base_values = [rec['value'] for rec in records if rec['active']]
    adjustments = []
    temp_sum = 0
    
    for i, val in enumerate(base_values):
        if i % 2 == 0:
            adjusted = val * importance_weights.get('even_factor', 1.1)
        else:
            adjusted = val + importance_weights.get('odd_offset', 0.5)
        adjustments.append(adjusted)
        temp_sum += adjusted * 0.9  # Irrelevant accumulation

    outlier_check = [x for x in adjustments if x > 50]
    adjustment_slice = adjustments[1:-1]  # Unused slice
    
    secondary_total = 0
    for adj in adjustments:
        if adj > 40:
            secondary_total += adj ** 0.5  # Distractor computation

    # Key logic: sum adjustments and apply final multiplier
    aggregate = sum(adjustments) * 0.85
    noise_level = sum([abs(x - 45) for x in base_values]) * 0.01  # Dead calculation
    final_score = int(aggregate - 15)  # Deterministic integer result
    
    return final_score

# Data setup
data = [
    {'value': 30, 'active': True},
    {'value': 42, 'active': True},
    {'value': 38, 'active': False},  # Inactive, excluded
    {'value': 55, 'active': True},
    {'value': 25, 'active': True}
]

weights = {
    'even_factor': 1.2,
    'odd_offset': 0.7,
    'bonus': 100  # Unused key
}

intermediate_result = [x['value'] * 2 for x in data]  # Irrelevant list comprehension
placeholder = len(intermediate_result) * 5  # Unused variable

final_score = calculate_final_score(data, weights)
print(f"Result: {final_score}")