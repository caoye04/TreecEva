def calculate_final_score(entries, limits):
    base = 0
    bonus = 0
    penalty = 0

    for i, entry in enumerate(entries):
        category = entry['type']
        value = entry['value']
        
        if category == 'revenue':
            base += value * 0.1
        elif category == 'cost':
            base -= value * 0.05
        
        # Apply bonus for early entries
        if i < 2 and value > limits['high']:
            bonus += 5
        
        # Track penalties for very low values
        if value < limits['low']:
            penalty += 2
    
    total = base + bonus - penalty
    return round(total, 3)

# Simulated business performance data
business_data = [
    {'type': 'revenue', 'value': 1200},
    {'type': 'cost', 'value': 300},
    {'type': 'revenue', 'value': 800},
    {'type': 'cost', 'value': 150}
]

thresholds = {
    'high': 750,
    'low': 100
}

# Irrelevant auxiliary variables (mild interference)
dummy_list = [x**2 for x in range(5)]
useless_sum = sum(dummy_list)

final_score = calculate_final_score(business_data, thresholds)
print(f"Result: {final_score}")