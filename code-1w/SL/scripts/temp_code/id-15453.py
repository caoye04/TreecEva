import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 24.9, 23.7]
humidity_readings = [45, 47, 50, 55, 60, 62, 58, 53]
pressure_readings = [1013, 1012, 1015, 1016, 1014, 1011, 1010, 1013]

# Irrelevant calibration coefficients (distractor)
calib_a, calib_b, calib_c = 0.987, 1.021, 0.00345
offset_matrix = [[1.1, -0.5], [0.3, -0.2]]

def apply_calibration(data, a, b):
    # Fake calibration that isn't used in main logic
    return [a * x + b for x in data]

def transform_pressure(p):
    # Unused transformation (dead code path)
    return [math.log(p_val - 1000) for p_val in p]

def normalize(data):
    mean = sum(data) / len(data)
    return [(x - mean) / mean for x in data]

def extract_peaks(data, threshold=2):
    peaks = []
    for i in range(1, len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1] and data[i] > threshold:
            peaks.append(i)
    return peaks

# Bitwise checksum for data integrity (partially relevant but obfuscated)
def compute_checksum(timestamps):
    chk = 0
    for t in timestamps:
        chk ^= int(t % 100) & 0xFF
    return chk | 0xABC  # Add constant interference

# Simulated timestamps (not directly used)
timestamps = [1678886400 + i*3600 for i in range(len(temperature_readings))]

# Distractor: fake metadata map
metadata_map = {
    'source': 'satellite',
    'version': '2.1',
    'checksum': compute_checksum(timestamps),
    'retries': 3
}

# Threshold configuration for diagnostics (critical)
threshold_map = {
    'temp_high': 26.0,
    'temp_low': 24.0,
    'humidity_spike': 55,
    'pressure_drop': 1012
}

# Intermediate processing with distractors
decorrelation_factor = 0.78
weight_vector = [0.5, 0.3, 0.2]

# Real processing pipeline
normalized_temp = normalize(temperature_readings)
normalized_humid = normalize(humidity_readings)

# Create processed data using list comprehension and zip (required feature)
processed_data = [
    {
        't': temp,
        'h': humid,
        'p': pressure,
        'index': idx,
        'anomaly_score': abs(normalized_temp[idx]) + 0.5 * abs(normalized_humid[idx])
    }
    for idx, (temp, humid, pressure) in enumerate(zip(temperature_readings, humidity_readings, pressure_readings))
]

# Secondary fake processing (distractor)
spectral_components = []
for i in range(4):
    component = 0
    for j in range(len(processed_data)):
        component += math.sin(processed_data[j]['t'] * (i+1))
    spectral_components.append(component)

# Another decoy function using dictionary operations
status_registry = {}
def register_status(code, msg, flags=0):
    status_registry[code] = {'message': msg, 'flag': flags, 'active': True}
    if flags & 0x1:
        return 'CRITICAL'
    return 'OK'

# Register irrelevant statuses
register_status(101, 'Sensor warmup', 0)
register_status(205, 'Data buffering', 0x1)
register_status(307, 'Calibration offset', 0)

# Core analysis logic (buried among distractions)
def count_critical_conditions(data, thresholds):
    high_temp_count = 0
    low_pressure_count = 0
    humidity_spike_count = 0
    
    for entry in data:
        if entry['t'] > thresholds['temp_high']:
            high_temp_count += 1
        if entry['t'] < thresholds['temp_low']:
            low_pressure_count += 1  # Intentional misleading name
        if entry['h'] > thresholds['humidity_spike']:
            humidity_spike_count += 1
    
    # Actual logic uses correct counting despite misleading var names
    return high_temp_count * 100 + humidity_spike_count * 10 + (low_pressure_count // 2)

# Another red herring: unused recursive function
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Real diagnostic function
steady_count = 0
def analyze_readings(data, thres_map):
    global steady_count
    total_risk = 0
    recent_stable = True
    
    # Nested logic with 4-level depth
    for i, record in enumerate(data):
        risk_level = 0
        
        if record['t'] > thres_map['temp_high']:
            risk_level += 2
            recent_stable = False
        elif record['t'] < thres_map['temp_low']:
            risk_level += 1
            
        if record['h'] > thres_map['humidity_spike']:
            risk_level += 2
            
        if i > 0 and data[i-1]['p'] > thres_map['pressure_drop'] > record['p']:
            risk_level += 3
            
        # Bit manipulation distraction (only partial relevance)
        risk_code = risk_level ^ 0x5
        risk_code = (risk_code << 1) | (risk_code >> 2)
        risk_code &= 0xF
        
        total_risk += risk_code
        
        if risk_level == 0:
            steady_count += 1
            if steady_count >= 3:
                total_risk -= 5  # stability bonus
        else:
            steady_count = 0
    
    # Final computation combining multiple concepts
    base_diagnostic = count_critical_conditions(data, thres_map)
    final_adjustment = total_risk % 7
    
    # Key answer computation
    final_diagnostic = base_diagnostic + final_adjustment
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")