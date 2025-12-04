from collections import Counter, defaultdict
import math

def preprocess_data(raw_data):
    # Normalize and clean data
    processed = []
    for item in raw_data:
        if item % 3 == 0:
            processed.append(item * 2)
        elif item % 5 == 0:
            processed.append(item // 2)
        else:
            processed.append(item + 3)
    return processed

def analyze_distribution(data):
    # Count occurrences and calculate distribution metrics
    counts = Counter(data)
    total = sum(counts.values())
    entropy = -sum((count/total) * math.log2(count/total) for count in counts.values())
    return counts, entropy

def extract_patterns(data):
    # Find patterns in the sequence (not relevant to final result)
    patterns = defaultdict(int)
    for i in range(len(data) - 1):
        pair = (data[i], data[i+1])
        patterns[pair] += 1
    return patterns

def calculate_priority(data, threshold):
    # Filter data based on threshold
    filtered = [x for x in data if x > threshold]
    
    # Calculate primary score components
    base_score = sum(filtered) if filtered else 0
    multiplier = len(filtered) / len(data) if data else 0
    
    # Apply logarithmic scaling and normalization
    if base_score > 0:
        log_component = math.log10(base_score)
    else:
        log_component = 0
    
    # Calculate weighted score
    weighted_score = base_score * multiplier
    
    # These operations don't affect the final result
    complexity_factor = sum(1 for x in filtered if x % 2 == 0) / len(filtered) if filtered else 0
    variance_metric = sum((x - (sum(filtered)/len(filtered)))**2 for x in filtered) / len(filtered) if filtered else 0
    
    # Return the actual priority score (only this matters)
    return int(weighted_score + log_component * 5)

# Main processing pipeline
raw_data = [12, 5, 18, 7, 10, 15, 22, 9, 30, 25]
processed_data = preprocess_data(raw_data)

# These operations create distractions
sorted_data = sorted(processed_data)
reversed_data = sorted_data[::-1]
even_numbers = [x for x in processed_data if x % 2 == 0]
odd_numbers = [x for x in processed_data if x % 2 != 0]

# Calculate statistics (distraction)
counts, entropy = analyze_distribution(processed_data)
patterns = extract_patterns(processed_data)

# More distracting calculations
maximum = max(processed_data)
minimum = min(processed_data)
range_value = maximum - minimum
mean_value = sum(processed_data) / len(processed_data)

# Generate misleading intermediate results
potential_threshold = int(mean_value + range_value / 4)
false_threshold = int(mean_value - entropy)
decoy_score = sum(odd_numbers) - sum(even_numbers)

# The actual filtering and priority calculation
threshold = 15  # The actual threshold used
filtered_data = [x for x in processed_data if x > threshold]
priority_score = calculate_priority(filtered_data, threshold)

# More misleading calculations after the answer is determined
adjusted_score = priority_score * (1 + entropy/10)
final_metric = (priority_score + decoy_score) / 2

print(f"Result: {priority_score}")