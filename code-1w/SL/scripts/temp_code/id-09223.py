def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    count = 0
    for i in range(len(sequence) - 2):
        if sequence[i] < sequence[i+1] > sequence[i+2]:
            count += 1
    return count

# Irrelevant signal processing function (dead end)
def smooth_data(signal):
    filtered = [signal[0]]
    for i in range(1, len(signal)-1):
        filtered.append((signal[i-1] + signal[i] + signal[i+1]) / 3)
    filtered.append(signal[-1])
    return filtered

# Unused transformation path
def transform_grid(matrix):
    rotated = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    flipped = [row[::-1] for row in rotated]
    return flipped

# Decoy state tracker
current_state = {'mode': 'idle', 'level': 0, 'active': False}
state_history = []

for step in range(3):
    current_state['level'] += step * 2
    state_history.append(current_state.copy())
    current_state['active'] = not current_state['active']

# Real computation begins here
raw_input = [8, 1, 6, 3, 9, 2, 7]
detected_peaks = analyze_pattern(raw_input)
signal_strength = sum(x**2 for x in raw_input if x % 2 == 1)

# Distractor: fake normalization
normalization_factor = max(raw_input) if raw_input else 1
temp_normalized = [x / normalization_factor for x in raw_input]

# Meaningful conditional expression using string method to determine mode
data_type = 'complex' if '9' in str(signal_strength) else 'basic'

# Intermediate values with mixed relevance
base_power = detected_peaks * 100
adjustment = len(temp_normalized) * 5 if data_type == 'complex' else 10
adjusted_power = base_power + adjustment - 12  # Key adjustment

# Threat level determined via dictionary lookup and conditional logic
lookup_table = {0: 1, 1: 3, 2: 7, 3: 15, 4: 31}
threat_level = lookup_table.get(detected_peaks, 63)

# Red herring: unused recursive function
def calculate_depth(n):
    if n <= 1:
        return 1
    return calculate_depth(n-1) + calculate_depth(n-2)

# Decoy list transformation
shadow_buffer = raw_input[:]
for _ in range(2):
    shadow_buffer = [a ^ b for a, b in zip(shadow_buffer, shadow_buffer[1:] + [0])]

# Final processing with conditional expression
previous_result = None
def process_outcome(power, threat):
    global previous_result
    temp_result = (power * 2) // threat
    if temp_result % 2 == 0:
        result = temp_result + 5
    else:
        result = temp_result - 3
    previous_result = result  # logged but not used further
    return float(result) if 'complex' in data_type.upper() else result

# Critical execution point
final_score = process_outcome(adjusted_power, threat_level)

# Output the required result
print(f"Target result: {final_score}")