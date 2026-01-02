import math

# Simulated sensor array data (temperature, pressure, humidity)
sensor_nodes = [
    (23.5, 101.3, 45), (24.1, 102.0, 47), (19.8, 99.8, 50), (22.7, 100.5, 44),
    (25.3, 103.1, 48), (20.9, 98.7, 52), (26.0, 104.2, 46), (21.4, 99.9, 49)
]

# Irrelevant calibration constants (distractor)
CALIBRATION_OFFSET_A = 0.037
CALIBRATION_OFFSET_B = -0.012
REFERENCE_VOLTAGE = 3.3

# System thresholds
temp_threshold = 24.0
pressure_threshold = 102.5
humidity_threshold = 50

# Derived sets (set operations used here)
high_temp_nodes = {i for i, (t, p, h) in enumerate(sensor_nodes) if t >= temp_threshold}
high_pressure_nodes = {i for i, (t, p, h) in enumerate(sensor_nodes) if p >= pressure_threshold}
high_humidity_nodes = {i for i, (t, p, h) in enumerate(sensor_nodes) if h >= humidity_threshold}

# Overlapping nodes (distraction from actual logic path)
critical_overlap = high_temp_nodes & high_pressure_nodes & high_humidity_nodes

# Masked status simulation (bit manipulation red herring)
node_status_mask = 0
for idx in range(len(sensor_nodes)):
    node_status_mask |= (1 << idx) if sensor_nodes[idx][0] > 21.0 else 0

# Unused recursive function (dead code path)
def calculate_entropy(data, base=2):
    if len(data) <= 1:
        return 0
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]
    return math.log(len(data)) + calculate_entropy(left, base) + calculate_entropy(right, base)

# Linear search for unstable nodes (some relevant, some not)
unstable_indices = []
for i, (temp, pressure, humidity) in enumerate(sensor_nodes):
    if abs(temp - 22.0) > 3.5 or pressure < 99.0 or humidity > 51:
        unstable_indices.append(i)

# Filtering logic (actual relevant path begins)
baseline_reference = sum(t for t, _, _ in sensor_nodes) / len(sensor_nodes)
filtered_data = []
for temp, pressure, humidity in sensor_nodes:
    # Conditional expression determines inclusion
    include = (temp > baseline_reference + 0.5) and (pressure > 100.0)
    
    # Decoy transformation (looks important but unused later)
    normalized_humidity = humidity / 100.0
    adjusted_pressure = pressure * (1 + 0.01 * normalized_humidity)
    
    if include:
        filtered_data.append((temp, pressure, humidity))

# Secondary filter based on set membership (set operation relevance)
eligible_index_set = {i for i, (t, p, h) in enumerate(sensor_nodes) if t >= 22.5}
filtered_data = [dp for i, dp in enumerate(filtered_data) 
                  if i in eligible_index_set or dp[1] > 103.0]

# Processing function with nested logic
def process_readings(readings):
    if not readings:
        return -999.0
    
    total_score = 0.0
    for temp, pressure, humidity in readings:
        # Complex scoring with multiple arithmetic operations
        temp_factor = (temp - 20.0) ** 1.5
        pressure_factor = math.log(pressure / 100.0)
        humidity_factor = 1 + max(0, (humidity - 40) * 0.01)
        
        # Bitwise disguise (irrelevant computation)
        magic_key = int(temp) ^ int(pressure) & 0xFF
        security_flag = (magic_key >> 4) % 3 == 0
        
        # Actual contribution (not obviously separable)
        reading_value = temp_factor * pressure_factor * humidity_factor
        
        # Conditional override (conditional expression)
        reading_value = reading_value if reading_value > 5.0 else (reading_value * 0.8)
        
        total_score += reading_value
    
    # Final aggregation
    adjustment = len(readings) * 0.25
    return total_score - adjustment

# Dummy entropy use (misleading call)
_ = [calculate_entropy([1, 2, 3]) for _ in range(2)]  # Unused list comp

# Critical execution point
final_diagnostic = process_readings(filtered_data)

# Output result
print(f"Result: {final_diagnostic}")