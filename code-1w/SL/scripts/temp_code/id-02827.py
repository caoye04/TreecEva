import math

# Simulated sensor fusion system for environmental monitoring
def acquire_data():
    raw_entries = [127, 255, 64, 192, 32, 224, 16, 96]
    scaling_factor = 0.75
    adjusted = [x * scaling_factor for x in raw_entries]
    return adjusted

# Irrelevant preprocessing - red herring
def smooth_noise(data):
    smoothed = []
    for i in range(len(data)):
        if i == 0:
            smoothed.append((data[i] + data[min(i+1, len(data)-1)]) / 2)
        elif i == len(data) - 1:
            smoothed.append((data[i] + data[i-1]) / 2)
        else:
            smoothed.append((data[i-1] + data[i] + data[i+1]) / 3)
    return smoothed

# Distractor function - never actually used in final computation
def compute_entropy(arr):
    total = sum(arr)
    probabilities = [x/total for x in arr if x > 0]
    entropy = -sum(p * math.log2(p) for p in probabilities)
    return round(entropy, 4)

# Real processing begins here
def filter_outliers(data, threshold=100):
    return [x for x in data if x > threshold]

# Signal transformation with slicing and lambda
transform_signal = lambda readings: [math.sin(x / 10) for x in readings][::2]  # Take every second element

# Secondary irrelevant transformation
def augment_data(signal):
    extended = signal + [signal[-1] * 0.9, signal[-2] * 1.1]
    return [round(x, 3) for x in extended]

# Core analysis logic (used)
def analyze_readings(filtered):
    base_score = sum(filtered)
    adjustment = 0
    
    # Complex conditional branching with nested logic
    if len(filtered) > 3:
        adjustment += 15
        temp_slice = filtered[1:3]
        if sum(temp_slice) > 50:
            adjustment *= 2
            
        # Bit manipulation decoy
        binary_flag = 0b1010
        mask = 0b1100
        masked = binary_flag & mask
        if masked == 12:
            adjustment += 5
    else:
        adjustment -= 10
    
    # Another layer of logic
    multiplier = 1
    for val in filtered:
        if val > 60:
            multiplier += 0.1
    
    intermediate = base_score * multiplier + adjustment
    
    # Final trap: this block looks important but is logically unreachable due to data shape
    if any(x < 0 for x in filtered):
        correction = -intermediate * 0.1
    else:
        correction = 8.5
    
    result = intermediate + correction
    return int(round(result))

# Unused recursive distractor
def recursive_sum(arr, n=None):
    if n is None:
        n = len(arr)
    if n <= 0:
        return 0
    return arr[n-1] + recursive_sum(arr, n-1)

# Main execution flow
sensor_log = acquire_data()  # Initial data acquisition
refined_log = smooth_noise(sensor_log)  # Looks important, but not used later
processed_signals = filter_outliers(sensor_log, threshold=80)  # Actual relevant data path
processed_signals = transform_signal(processed_signals)  # Apply real transformation

# Dead code assignment - misleading
augmented_output = augment_data(processed_signals)

# Key statement
final_diagnostic = analyze_readings(processed_signals)

print(f"Result: {final_diagnostic}")