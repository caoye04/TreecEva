def analyze_sequence(seq):
    temp_sum = 0
    for i in range(len(seq)):
        if i % 2 == 0:
            temp_sum += seq[i] * 1.5
        else:
            temp_sum -= seq[i] * 0.5
    return temp_sum

sequence = [3, 7, 2, 8, 4, 6]
raw_total = sum(sequence)
adjusted_total = raw_total * 1.1

# Misleading intermediate transformations
decoy_values = [x ** 2 for x in sequence if x < 5]
offset = len(decoy_values) * 2.5
shadow_copy = sequence[::-1]

processed_data = []
for val in sequence:
    if val > 5:
        processed_data.append(val * 1.2)
    elif val == 5:
        processed_data.append(0)
    else:
        processed_data.append(val * 1.8)

# Secondary distraction: string-based filtering (irrelevant to final result)
data_tags = ['L', 'H', 'L', 'H', 'L', 'H']
tagged_sum = 0
for tag, num in zip(data_tags, sequence):
    if tag == 'H':
        tagged_sum += num

# Another red herring: dictionary frequency count
freq_map = {}
for num in sequence:
    freq_map[num] = freq_map.get(num, 0) + 1
unique_count = len(freq_map)

# Actual computation chain
baseline = analyze_sequence(processed_data)
penalty = 0
for idx, item in enumerate(processed_data):
    if idx > 0 and item > processed_data[idx-1]:
        penalty += 1.5

adjusted_baseline = baseline - penalty
inflation_factor = 1.05
interim_result = adjusted_baseline * inflation_factor

scaling_constant = 2.0 if len(processed_data) > 5 else 1.5
final_score = int(interim_result * scaling_constant)

Result: final_score