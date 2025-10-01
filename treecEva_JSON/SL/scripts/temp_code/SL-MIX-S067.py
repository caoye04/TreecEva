import math

def transform_data(data):
    transformed = []
    for key, values in data.items():
        sub_result = []
        for v in values:
            if isinstance(v, int) and v > 0:
                sub_result.append(math.log(v) * 2)
            elif isinstance(v, str):
                sub_result.append(len(v) ** 2)
            else:
                sub_result.append(0)
        transformed.append((key, sum(sub_result)))
    return dict(transformed)

def aggregate_results(mapped_data):
    total = 0
    for key, value in mapped_data.items():
        if key.startswith('group'):
            total += int(value) & 0xFF
        else:
            total += value
    return total

# Main execution
nested_data = {
    'groupA': [10, 'hello', -5, 2.5],
    'groupB': ['world', 100, None, 3],
    'other': [4, 'test', 6, 'longstring']
}

mapped = transform_data(nested_data)
aggregated = aggregate_results(mapped)

# Bitwise manipulation with previous result
shifted = aggregated << 2
masked = shifted & 0x1FF

# Final calculation combining multiple operations
final_result = (masked ^ 0xAA) + int(math.sqrt(144)) - (7 * 3)

print(f"Result: {final_result}")