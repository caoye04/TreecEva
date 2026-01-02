import math

def simulate_sensor_noise(level, size):
    # Irrelevant simulation function (dead path)
    return [math.sin(i * level) + 0.1 for i in range(size)]

def compute_checksum(data):
    # Misleading checksum operation
    return sum(d % 7 for d in data) * 3

def decode_sequence(seq):
    # Unused decoding logic (red herring)
    return [int(s[::-1]) for s in seq if s.isdigit()]

def extract_features(raw_log):
    # Processes log but only one part matters
    lines = raw_log.strip().split('\n')
    temperatures = []
    timestamps = []
    for line in lines:
        parts = line.split(',')
        if 'TEMP' in line and len(parts) > 2:
            try:
                temp = float(parts[1].strip())
                temperatures.append(temp)
            except ValueError:
                continue
        elif 'TS' in line:
            timestamps.append(parts[0])
    return temperatures, timestamps

def normalize_signal(signal):
    mean = sum(signal) / len(signal)
    return [(x - mean) * 1.5 for x in signal]

def filter_outliers(data, threshold=2.0):
    mean = sum(data) / len(data)
    std = (sum((x - mean)**2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean) <= threshold * std], std

def rolling_average(series, window=3):
    # Distractor: not used in final computation
    result = []
    for i in range(len(series) - window + 1):
        result.append(sum(series[i:i+window]) / window)
    return result

def analyze_pattern(buffer):
    # Core logic buried in noise
    if len(buffer) < 5:
        return -999
    
    # Step 1: Apply logarithmic transformation to stabilize variance
    transformed = [math.log(abs(x) + 1) for x in buffer]
    
    # Step 2: Detect trend reversals (sign changes in differences)
    diffs = [transformed[i+1] - transformed[i] for i in range(len(transformed)-1)]
    reversals = 0
    for i in range(1, len(diffs)):
        if diffs[i-1] * diffs[i] < 0:  # Sign change
            reversals += 1
    
    # Step 3: Weighted score based on reversal density and magnitude
    base_score = reversals * 100
    magnitude_factor = sum(abs(d) for d in diffs) / len(diffs)
    
    # Step 4: Apply conditional bonus
    if magnitude_factor > 0.5 and reversals >= 3:
        base_score += 227  # Critical bonus
    
    return int(base_score)

# Simulated diagnostic log input
log_input = '''
TS001,TEMP:-23.5,STATUS:NORMAL
TS002,TEMP:45.0,STATUS:OK
TS003,TEMP:67.8,STATUS:OK
TS004,TEMP:-89.1,STATUS:WARNING
TS005,TEMP:12.3,STATUS:NORMAL
'''

# Extract temperature values (key data source)
temps, _ = extract_features(log_input)

# Irrelevant noise generation
noise_patch = simulate_sensor_noise(0.77, len(temps))
checksum_val = compute_checksum([int(t*2) for t in temps])

# Core processing begins here
raw_buffer = [int(t) for t in temps]  # Convert to integers

# Normalize signal (has side effect of modifying distribution)
normalized_temp = normalize_signal(raw_buffer)

# Filter outliers — returns cleaned version and std
cleaned_buffer, spread = filter_outliers(normalized_temp, threshold=1.8)

# Additional distraction: string-based processing
temp_strings = [f'TEMP{int(abs(t))}' for t in raw_buffer]
reversed_checksum = sum(int(s[::-1][:2]) for s in temp_strings if s.endswith('5'))

# Buffer entropy calculation (misleading name)
entropy_buffer = [abs(int(c * 2.1)) for c in cleaned_buffer]

# Decoy usage
if len(entropy_buffer) % 2 == 0:
    entropy_buffer.append(7)

# Key statement
final_diagnostic = analyze_pattern(entropy_buffer)

# Output result
print(f"Result: {final_diagnostic}")