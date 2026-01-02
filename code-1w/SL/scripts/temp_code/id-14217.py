def analyze_trends(data):
    trends = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trends.append('up')
        elif data[i] < data[i-1]:
            trends.append('down')
        else:
            trends.append('same')
    return trends

# Irrelevant helper function (distractor)
def compute_variance(lst):
    mean = sum(lst) / len(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)
    return variance

# Secondary processing with slicing
def filter_outliers(seq):
    sorted_seq = sorted(seq)
    lower_bound = sorted_seq[len(sorted_seq)//4]  # Q1
    upper_bound = sorted_seq[-(len(sorted_seq)//4)]  # Q3
    return [x for x in seq if lower_bound <= x <= upper_bound]

# Main processing chain
raw_measurements = [12, 15, 10, 8, 16, 20, 18, 25, 22, 30, 5, 3]
smoothed_data = filter_outliers(raw_measurements)

# Misleading transformation
transformed = [x * 1.1 for x in raw_measurements if x > 10]
shadow_copy = transformed[::-1]  # Reversed, unused later

# Real signal extraction using conditional logic and slicing
primary_signal = [x for x in smoothed_data if x % 2 == 0]
secondary_signal = [x for x in smoothed_data if x % 2 == 1]

# State tracking variables (some irrelevant)
count_up = 0
prev = primary_signal[0]
for val in primary_signal[1:]:
    if val > prev:
        count_up += 1
    prev = val

# Dummy set operations (semi-relevant)
unique_primary = set(primary_signal)
unique_secondary = set(secondary_signal)
overlap = unique_primary & unique_secondary  # Empty in this case
exclusive_to_primary = unique_primary - unique_secondary

# Conditional expression influencing final result
dominant_set_size = len(unique_primary) if len(unique_primary) >= len(unique_secondary) else len(unique_secondary)

# Another red herring: complex but unused calculation
aggregate_metric = 0
for i, x in enumerate(smoothed_data):
    aggregate_metric += x * (0.9 ** i)

# Core logic embedded within distractions
def calculate_final_score(data_chunk):
    base = sum(data_chunk)
    adjustment = len(data_chunk) * 0.5
    
    # Use of slicing to get middle portion
    mid_section = data_chunk[len(data_chunk)//3 : 2*len(data_chunk)//3]
    bonus = sum(m for m in mid_section if m > 15)
    
    # Conditional expression
    penalty = 10 if len(overlap) > 0 else 2
    
    # Final computation
    score = base + adjustment + bonus - penalty
    return int(score)

# Processed data used in final call
processed_data = primary_signal[:len(primary_signal)//2 + 1]
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")