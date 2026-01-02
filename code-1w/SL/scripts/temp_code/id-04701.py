from collections import defaultdict, Counter

def analyze_frequencies(values):
    # Irrelevant frequency analysis (distractor)
    freq = Counter(values)
    unique_count = len(freq)
    mode = freq.most_common(1)[0][1] if freq else 0
    return unique_count

def preprocess_records(raw_entries):
    temp_result = []
    for entry in raw_entries:
        if entry < 0:
            temp_result.append(abs(entry) * 2)
        elif entry % 3 == 0 and entry > 5:
            temp_result.append(entry + 1)
        else:
            temp_result.append(entry)
    return temp_result

def filter_and_group(data):
    grouped = defaultdict(list)
    outlier_sum = 0
    total_filtered = 0

    for val in data:
        category = 'A' if val < 10 else 'B' if val < 20 else 'C'
        grouped[category].append(val)

        # Red herring: tracking outliers that are never used
        if val > 25:
            outlier_sum += val
            total_filtered += 1

    # Semi-relevant transformation
    processed = []
    for key in ['A', 'B', 'C']:
        if grouped[key]:
            avg = sum(grouped[key]) / len(grouped[key])
            processed.append(round(avg))
    return processed

def calculate_final_score(metrics):
    base = 0
    adjustments = [3, -1, 2]
    for i, m in enumerate(metrics):
        if i % 2 == 0:
            base += m * (i + 1)
        else:
            base -= m // 2
    # Apply adjustment from unused path
    noise_factor = sum(adjustments)  # This is constant but looks dynamic
    final = base + noise_factor
    return final

# Main execution flow
raw_data = [12, -4, 9, 6, 21, 3, 18, 7, 27, 5]

# Step 1: Preprocess the records
intermediate_data = preprocess_records(raw_data)

# Step 2: Analyze frequencies (unused result - distractor)
analysis_result = analyze_frequencies(intermediate_data)

# Step 3: Filter and group into categories
processed_data = filter_and_group(intermediate_data)

# Step 4: Calculate final score based on aggregated metrics
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")