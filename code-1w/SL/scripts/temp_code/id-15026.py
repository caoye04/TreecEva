def analyze_pattern(sequence):
    count_vowels = 0
    temp_sum = 0
    for char in sequence:
        if char in 'aeiou':
            count_vowels += 1
        temp_sum += ord(char)
    return count_vowels, temp_sum

# Simulate sensor data integrity check
def verify_checksum(data_string):
    checksum = 0
    for i, char in enumerate(data_string):
        checksum += (i + 1) * ord(char)
    return checksum % 100 == 42

# Main processing pipeline
def calculate_adjusted_score(base_value, factor):
    adjusted = base_value
    if adjusted > 50:
        adjusted -= factor * 3
    else:
        adjusted -= factor * 1.5
    
    # Apply exponential decay if special condition met
    binary_flag = bin(adjusted).count('1')
    if binary_flag % 2 == 0:
        adjusted = adjusted * 0.95
    
    return int(adjusted)

# System initialization
raw_data_stream = "sensor_log_2077"
error_count = 0
packet_loss_rate = 0.03

# Extract embedded numeric pattern
numeric_segment = ''.join([c for c in raw_data_stream if c.isdigit()])
sequence_id = int(numeric_segment) if numeric_segment else 0

# Analyze string characteristics
vowel_count, ascii_total = analyze_pattern(raw_data_stream)

# Generate intermediate metrics (some are distractions)
distraction_matrix = [
    [sequence_id * 2, vowel_count ** 2],
    [ascii_total // 100, len(raw_data_stream)]
]

redundant_calc_1 = distraction_matrix[0][0] + distraction_matrix[1][1]
redundant_calc_2 = distraction_matrix[0][1] * 0.75

# Determine operational mode based on string property
mode_flag = len(raw_data_stream) % 4

# Core calculation variables
base_metric = ascii_total // 10
raw_score = base_metric + sequence_id - vowel_count

# Hidden dependency: modify score if checksum passes
if verify_checksum(raw_data_stream):
    raw_score += 5

# Penalty system with conditional weighting
penalty_factor = mode_flag if mode_flag > 2 else 2

# Critical statement
final_score = calculate_adjusted_score(raw_score, penalty_factor)

# Logging irrelevant diagnostics
current_timestamp = 1638429120
log_entry = f"Error:{error_count}|Time:{current_timestamp}|Score:{final_score}"
diagnostic_key = log_entry.split('|')[2].split(':')[1]

# Output result as required
print(f"Result: {final_score}")