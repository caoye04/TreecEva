import math

# Sensor simulation and analysis system for environmental monitoring

def generate_signals(baseline, count):
    """Generate synthetic sensor signals with noise (irrelevant distractor)"""
    return [baseline + math.sin(i) * 0.1 for i in range(count)]


def compute_entropy(data):
    """Calculate Shannon entropy - misleading intermediate computation"""
    total = sum(data)
    probs = [x / total for x in data]
    return -sum(p * math.log2(p) for p in probs if p > 0)


def filter_outliers(data, threshold=2.0):
    """Remove values beyond z-score threshold - unused function (dead code path)"""
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val)**2 for x in data) / len(data))**0.5
    return [x for x in data if abs((x - mean_val)/std_dev) <= threshold]


def transform_coordinates(x, y):
    """Convert Cartesian to polar - irrelevant geometric transformation"""
    r = (x**2 + y**2)**0.5
    theta = math.atan2(y, x)
    return r, theta

# Irrelevant global constants
MAX_BUFFER_SIZE = 1024
CALIBRATION_FACTOR = 0.873
REFERENCE_VOLTAGE = 3.3

# Simulated raw sensor inputs (with decoy entries)
raw_readings = [
    12.4, 13.1, 11.9, 14.2, 13.8, 12.9, 13.5, 14.0, 13.3, 12.7,
    15.1, 10.2, 13.6, 13.0, 12.5, 13.9, 14.1, 13.4, 12.8, 13.7
]

# Misleading preprocessing chain
smoothed = [round(raw_readings[i] * 0.7 + raw_readings[i+1] * 0.3, 2) 
             for i in range(len(raw_readings)-1)]

delta_changes = [smoothed[i+1] - smoothed[i] for i in range(len(smoothed)-1)]

# Decoy statistical measures
mean_change = sum(delta_changes) / len(delta_changes)
variance = sum((x - mean_change)**2 for x in delta_changes) / len(delta_changes)
entropy_value = compute_entropy(smoothed)  # Computed but not used

# Actual relevant processing begins here
window_size = 3
processed_data = []

for i in range(0, len(raw_readings) - window_size + 1, window_size):
    window = raw_readings[i:i+window_size]
    avg = sum(window) / window_size
    if avg >= 13.0:
        processed_data.append(int(avg + 0.5))  # Round to nearest integer
    else:
        processed_data.append(int(avg))

# Additional irrelevant list comprehension (distractor)
power_levels = [int(10 * math.log10(x/1e-3)) for x in raw_readings if x > 0]

# Unused recursive helper (red herring)
def recursive_sum(arr, idx=0):
    if idx >= len(arr):
        return 0
    return arr[idx] + recursive_sum(arr, idx + 1)

# Key analysis function that produces the target result
def analyze_readings(data):
    """Analyze processed sensor readings to produce diagnostic code"""
    status_flags = []
    
    for val in data:
        if val > 13:
            status_flags.append(3)
        elif val == 13:
            status_flags.append(2)
        else:
            status_flags.append(1)
    
    # Apply bitwise transformation (relevant operation)
    result = 0
    for i, flag in enumerate(status_flags):
        result += flag << i  # Bit shifting accumulation
    
    # Final transformation using integer division and modulo
    checksum = sum(status_flags) * 17
    final_code = (result ^ checksum) // 3
    
    return final_code

# Critical execution point
final_diagnostic = analyze_readings(processed_data)

# Print required output
print(f"Target result: {final_diagnostic}")