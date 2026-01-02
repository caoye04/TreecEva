import math

# Simulated sensor array data with noise injection
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.1, 23.7]
pressure_readings = [101.3, 102.1, 100.9, 103.5, 101.8, 102.6, 99.7, 101.2]
humidity_readings = [45, 47, 50, 44, 46, 48, 51, 43]

# Irrelevant auxiliary data (distractor)
legacy_system_flags = ['A', 'B', 'C', 'D', 'E']
user_preferences = {'theme': 'dark', 'notifications': True, 'auto_save': False}

# Noise injection function (dead code path - never called)
def inject_noise(data, factor=0.1):
    return [x + random.uniform(-factor, factor) for x in data]

# Signal processing pipeline
smoothing_kernel = [0.25, 0.5, 0.25]

# Apply moving average smoothing using slicing (relevant)
def smooth_signal(signal):
    if len(signal) < 3:
        return signal
    smoothed = []
    for i in range(1, len(signal) - 1):
        weighted = (signal[i-1] * 0.25) + (signal[i] * 0.5) + (signal[i+1] * 0.25)
        smoothed.append(weighted)
    return smoothed

# Extract features from multiple sensor streams (tuple unpacking)
def extract_features(temp, press, humid):
    avg_temp = sum(temp) / len(temp)
    avg_press = sum(press) / len(press)
    variance_humid = sum((x - sum(humid)/len(humid))**2 for x in humid) / len(humid)
    return avg_temp, avg_press, variance_humid

# Misleading diagnostic function (decoy - uses different logic)
def legacy_diagnostic(data):
    threshold = 45
    count = 0
    for x in data:
        if x > threshold:
            count += 1
        else:
            count -= 1
    return count * 2

# Critical data transformation chain
raw_combinations = []
for t, p, h in zip(temperature_readings, pressure_readings, humidity_readings):
    # Composite calculation: thermal-pressure index
    tpi = (t * 1.8 + 32) * (p / 100)  # Convert to Fahrenheit internally
    raw_combinations.append(tpi)

# Smooth the combined signal
filtered_combinations = smooth_signal(raw_combinations)

# Secondary processing: normalize around mean
mean_combination = sum(filtered_combinations) / len(filtered_combinations)
scaled_combinations = [x - mean_combination for x in filtered_combinations]

# Bit manipulation for digital filtering (simulated)
def apply_bit_filter(value):
    # Convert to fixed-point integer representation
    fixed = int(abs(value) * 1000)
    # Apply XOR mask and bit shifts (irrelevant to final result but looks important)
    masked = (fixed ^ 0xFF) >> 2
    return (masked & 0x3FFF) * (1 if value >= 0 else -1)

# Apply filter (but result not used in final computation - red herring)
bit_filtered = [apply_bit_filter(x) for x in scaled_combinations]

# Actual relevant processing: find peak deviation
peak_deviation = max(scaled_combinations) - min(scaled_combinations)

# String-based state encoding (slicing and string methods - distractor)
current_state = "operational"
state_code = current_state.upper()[1:4]  # 'PER'
encoded_flag = ''.join([str(ord(c) % 5) for c in state_code])  # '202'

# Lambda for dynamic threshold (actually used)
determine_threshold = lambda base, factor: base * (1 + math.sin(0.5)) * factor
adaptive_threshold = determine_threshold(peak_deviation, 0.8)

# Set of critical indices (set usage - relevant)
critical_indices = set()
for i, val in enumerate(scaled_combinations):
    if abs(val) > adaptive_threshold:
        critical_indices.add(i)

critical_count = len(critical_indices)

# Data restructuring via slicing and packing
segment_a = scaled_combinations[:3]
segment_b = scaled_combinations[-3:]
reconstructed = segment_b[::-1] + [adaptive_threshold] + segment_a  # Reverse and combine

# Final analysis function using multiple concepts
def analyze_signal(signal_data):
    # Complex nested logic with multiple steps
    n = len(signal_data)
    if n == 0:
        return 0.0
    
    # Step 1: Compute rolling product of absolute values
    roll_product = 1.0
    for x in signal_data[:4]:
        roll_product *= abs(x) + 0.1  # Avoid zero
    
    # Step 2: Count sign changes (logical comparisons)
    sign_changes = 0
    for i in range(1, len(signal_data)):
        if (signal_data[i] > 0) != (signal_data[i-1] > 0):
            sign_changes += 1
    
    # Step 3: Apply logarithmic scaling
    log_component = math.log(roll_product) if roll_product > 0 else 0
    
    # Step 4: Weighted combination with bit-level heuristic (misleading name)
    magic_constant = 2.71828
    confusion_term = (critical_count << 2) ^ 5  # Uses external variable but masked
    actual_weight = 0.3 * log_component + 0.7 * sign_changes
    
    # Final computation - only part of inputs are truly relevant
    final_score = actual_weight * magic_constant - len(legacy_system_flags)
    
    # Key insight: the answer depends only on sign_changes, log_component, and constants
    return round(final_score, 6)

# Processed data fed to analyzer
processed_data = reconstructed

# Execution point of interest
final_diagnostic = analyze_signal(processed_data)

# Print result as required
print(f"Target result: {final_diagnostic}")