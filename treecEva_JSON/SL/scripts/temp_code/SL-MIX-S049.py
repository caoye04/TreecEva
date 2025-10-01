import math

def process_data(data):
    result = []
    for key, values in data.items():
        transformed = [
            math.log(abs(x)) if x != 0 else 0 
            for x in values 
            if isinstance(x, (int, float))
        ]
        result.append({
            'key': key.upper(),
            'sum_logs': sum(transformed),
            'count': len(transformed)
        })
    return result

def calculate_weighted_score(entries):
    total = 0
    weights = [1.5, 2.0, 0.5, 3.0]
    for i, entry in enumerate(entries):
        weight = weights[i % len(weights)]
        score = entry['sum_logs'] * weight + entry['count']
        entry['weighted_score'] = score
        total += score
    return total / len(entries) if entries else 0

data_structure = {
    'alpha': [1, -2, 3, 0, 5.5],
    'beta': [0, 4, -5, 6.2, 7],
    'gamma': [2.2, -3.3, 0, 4, -5.5],
    'delta': [1.1, 2.2, 3.3, 0, -4.4]
}

processed = process_data(data_structure)
average_weighted = calculate_weighted_score(processed)

# Additional transformations
multiplier = 2
final_score = round(average_weighted * multiplier) ^ 0xF  # XOR with hexadecimal
final_score = final_score & 0xFF  # Bitwise AND to ensure 8-bit result

print(f'Result: {final_score}')