from collections import defaultdict, Counter

def preprocess_records(raw_entries):
    # Irrelevant transformation: counts per category (not used in final score)
    category_count = defaultdict(int)
    for entry in raw_entries:
        category_count[entry['category']] += 1

    # Relevant processing: extract and scale values
    scaled_values = []
    for entry in raw_entries:
        base = entry['value'] * 0.85
        if entry['flag']:
            base *= 1.2
        scaled_values.append(base)
    
    return scaled_values


def analyze_distribution(values):
    # Distractor function: computes statistical spread but only mean is used
    count_stats = Counter([round(v) for v in values])
    total = sum(values)
    mean = total / len(values) if values else 0
    variance = sum((v - mean) ** 2 for v in values) / len(values)
    std_dev = variance ** 0.5

    # Semi-relevant: identifies outliers but not used beyond filtering hint
    threshold = mean + std_dev
    filtered = [v for v in values if v <= threshold]

    return mean, filtered


def calculate_final_score(data_list):
    temp_offset = 0
    for i in range(3):
        temp_offset += (i * i)  # Dead computation, never used

    # Actual logic: scoring based on transformed data
    adjusted_sum = 0
    multiplier = len(data_list) % 4 + 1
    
    for idx, val in enumerate(data_list):
        if idx % 2 == 0:
            adjusted_sum += val * 1.1
        else:
            adjusted_sum += val * 0.9

    # Final adjustment using list comprehension (idiomatic python)
    penalties = [0.5 for x in data_list if x < 10]
    total_penalty = sum(penalties)

    result = (adjusted_sum - total_penalty) * multiplier
    return int(result)

# Main execution
raw_data = [
    {'value': 12, 'category': 'A', 'flag': True},
    {'value': 8,  'category': 'B', 'flag': False},
    {'value': 15, 'category': 'A', 'flag': True},
    {'value': 7,  'category': 'C', 'flag': True},
    {'value': 20, 'category': 'B', 'flag': False}
]

# Step 1: Preprocess the raw records
processed_data = preprocess_records(raw_data)

# Step 2: Analyze distribution (some output used, some ignored)
distribution_mean, cleaned_data = analyze_distribution(processed_data)

# Step 3: Calculate final score using processed data
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")