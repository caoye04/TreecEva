def analyze_signal(x, y):
    if x < 0:
        return (x ** 2) + y
    else:
        return (x * 2) - y

# Irrelevant helper function (dead code path)
def deprecated_normalization(data):
    return [d / max(data) for d in data]

# Unused transformation map
tf_map = {
    'A': lambda x: x + 10,
    'B': lambda x: x * 3,
    'C': lambda x: x - 5
}

# Simulated sensor data with mixed types and red herrings
raw_entries = [
    {'id': 'S1', 'val': 14, 'meta': {'type': 'temp', 'scale': 'c'}},
    {'id': 'S2', 'val': -7, 'meta': {'type': 'pressure', 'unit': 'kpa'}},
    {'id': 'S3', 'val': 21, 'meta': {'type': 'temp', 'scale': 'c'}}
]

# Extract values but include irrelevant filtering
valid_types = ['temp', 'humidity']
extracted = []
for entry in raw_entries:
    if entry['meta']['type'] in valid_types:
        extracted.append(entry['val'])
    else:
        # This branch processes pressure (irrelevant), but logs it anyway
        extracted.append(0)  # Distractor: injects noise

# Real signal processing begins here
base_readings = [18, -6, 22, 4, -14, 8]
squared_offsets = [r**2 for r in base_readings if r < 0]  # Only negative values matter
offset_correction = sum(squared_offsets) // 4 if squared_offsets else 0

# Threshold setup with decoy values
thresholds = {
    'critical': 150,
    'warning': 80,
    'info': 10,
    'unused_mode': 200  # Red herring
}

# Primary data for analysis
sensor_data = [12, -8, 16, 3, -10, 7, 25]

# Secondary derived list using enumerate and conditional expression
indexed_adjustments = [
    val * 2 if i % 3 == 0 else val + offset_correction
    for i, val in enumerate(sensor_data)
]

# Use of zip to pair with dummy labels (mostly irrelevant)
dummy_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
labeled_data = list(zip(dummy_labels, indexed_adjustments))

# Core logic buried under distractions
intermediate_results = []
for i, (label, value) in enumerate(labeled_data):
    if label in tf_map:
        transformed = tf_map[label](value)
    else:
        transformed = value + i  # Default adjustment

    # Key conditional logic using boolean chains and modular arithmetic
    if transformed > thresholds['warning'] and i % 2 == 0:
        intermediate_results.append(transformed // 2)
    elif transformed < 0:
        intermediate_results.append(abs(transformed))
    else:
        intermediate_results.append(transformed % thresholds['critical'])

# Decoy aggregation (never used)
avg_decoy = sum(intermediate_results) / len(intermediate_results) if intermediate_results else 0

# Actual processing function
def process_readings(readings, limits):
    temp_stack = []
    cumulative = 0

    for idx, reading in enumerate(readings):
        # Apply non-linear transform based on position
        adjusted = reading * (idx + 1) if reading >= 0 else abs(reading) ** 2
        
        # Conditional expression with nested logic
        status_flag = 'high' if adjusted > limits['critical'] else ('low' if adjusted < limits['info'] else 'normal')
        
        # Update cumulative only for 'normal' or specific index
        if status_flag == 'normal' or idx in {2, 5}:
            if idx % 4 == 0:
                cumulative += adjusted // 3
            else:
                cumulative += adjusted % 17
        
        # Extra stack operation (partially irrelevant)
        if adjusted % 5 == 0:
            temp_stack.append(adjusted)
    
    # Final computation uses both cumulative and stack side-effect
    residual = len(temp_stack) * 4
    return cumulative - residual

# Execute main logic
final_diagnostic = process_readings(sensor_data, thresholds)

# Print result as required
print(f"Target result: {final_diagnostic}")