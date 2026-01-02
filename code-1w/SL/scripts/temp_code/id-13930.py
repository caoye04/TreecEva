def analyze_productivity(records):
    totals = []
    weights = [0.1, 0.2, 0.3, 0.4]
    phantom_sum = 0
    
    for i, record in enumerate(records):
        base = sum(record) / len(record)
        adjusted = base * weights[i % 4]
        totals.append(adjusted)
        
        # Distractor: irrelevant accumulation
        for j in range(3):
            phantom_sum += i * j

    return sum(totals)


def calculate_rating(contributions, impact_levels):
    rating = 0
    temp_buffer = []
    
    for idx, (contrib, impact) in enumerate(zip(contributions, impact_levels)):
        if impact <= 0:
            continue
            temp_buffer.append(contrib)  # Dead code after continue
        
        # Real logic path
        scaled_contrib = contrib * impact
        if scaled_contrib > 50:
            rating += 10
        else:
            rating += 5
        
        # Early termination based on condition
        if rating >= 35:
            break

    # Secondary processing with distraction
    temp_result = 0
    for x in range(5):
        temp_result += x ** 2  # Irrelevant computation

    final_penalty = 0
    for level in impact_levels:
        if level == 3:
            final_penalty += 2

    return rating - final_penalty

# Main execution
productivity_records = [
    [80, 75, 90],
    [60, 88, 70],
    [95, 85, 100],
    [70, 65, 60]
]

contributions = [12, 8, 15, 5, 20]
impact_levels = [3, 2, 4, 0, 3]

phantom_data = [{'id': i, 'val': i*3} for i in range(10)]
accum = 0
for item in phantom_data:
    accum += item['val'] // 2  # Misleading accumulation

interim = analyze_productivity(productivity_records)

# Key statement
final_score = calculate_rating(contributions, impact_levels)

print(f"Result: {final_score}")