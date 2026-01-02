def analyze_readings(readings):
    filtered = [r for r in readings if r > 0]
    squared = [x * x for x in filtered]
    avg = sum(squared) / len(squared) if squared else 0
    threshold = 100
    high_vals = [v for v in squared if v > threshold]
    return len(high_vals), avg


def transform_sequence(seq):
    reversed_seq = seq[::-1]
    shifted = [s % 7 for s in reversed_seq]
    mapped = [abs(sh - 3) for sh in shifted]
    return mapped

readings_input = [4, -1, 6, 2, 8, -5, 3]
sequence_input = [10, 20, 30, 40, 50]

# Irrelevant transformation
irrelevant_transform = ''.join([str(i) for i in sequence_input])
dummy_stat = len(irrelevant_transform.replace('0', ''))

# Process data through analysis
count_high, mean_sq = analyze_readings(readings_input)

# Transform sequence and compute auxiliary metric
transformed = transform_sequence(sequence_input)
sum_transformed = sum(transformed)

# Simulate intermediate scoring
base_score = count_high * 10
adjustment = int(mean_sq // 10)
interim_score = base_score + adjustment

# Dummy string processing (distraction)
data_tag = "sensor_v1"
version_code = data_tag.split('_')[-1]
version_number = ord(version_code[0]) - ord('a')

# State tracking with red herring variables
tracking_log = []
for t in transformed:
    tracking_log.append(f"Item:{t}")

# Key logic chain
processed_data = {
    'level': interim_score,
    'magnitude': sum_transformed,
    'tag_val': version_number
}

# Auxiliary irrelevant calculation
phantom_value = sum([len(log) for log in tracking_log])

# Final score computation
def calculate_final_score(data):
    level = data['level']
    mag = data['magnitude']
    tag = data['tag_val']
    temp = level + mag
    # Misleading use of string method
    flag_str = "success" if temp > 50 else "warning"
    bonus = len(flag_str.upper())
    result = temp - tag + bonus
    return result

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")