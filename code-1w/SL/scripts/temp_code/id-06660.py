import math

# Simulated sensor network diagnostics with red herrings and complex logic

def collect_readings():
    raw_data = [32, 15, 44, 7, 23, 61, 19]
    offset = 5
    adjusted = [x + offset for x in raw_data]
    return adjusted

# Irrelevant transformation - distractor
def transform_coordinates(x, y):
    radius = math.sqrt(x*x + y*y)
    angle = math.atan2(y, x)
    return radius, angle

# Unused helper function - dead code path
def validate_checksum(data):
    checksum = sum(data) % 256
    return checksum == 0

# Decoy analysis with misleading intermediate result
def superficial_analysis(data):
    peak = max(data)
    avg = sum(data) / len(data)
    variance = sum((x - avg) ** 2 for x in data) / len(data)
    # This looks important but is never used
    normalized = [round((x - avg) / (math.sqrt(variance) + 1e-8), 2) for x in data]
    return {'peak': peak, 'trend': avg > 30}

# Real processing begins here
readings = collect_readings()

# Apply non-linear scaling - relevant
scaled_readings = [int(x * math.log(x + 1)) for x in readings]

# Filter anomalies using set operations - relevant concept
expected_range = set(range(20, 200))
anomalies = set(scaled_readings) - expected_range
filtered_readings = [x for x in scaled_readings if x in expected_range]

# Bit manipulation decoy - irrelevant
def obscure_value(val):
    shifted = (val << 3) & 0xFF
    toggled = shifted ^ 0b10101010
    return toggled >> 1

obscured_values = [obscure_value(x) for x in filtered_readings]  # Dead end

# Conditional expression chain - relevant
status_flags = [
    'critical' if x < 30 else \
    'warning' if x < 60 else \
    'normal' if x < 100 else 'unknown'
    for x in filtered_readings
]

# Counting and grouping - relevant
flag_counts = {}
for flag in status_flags:
    flag_counts[flag] = flag_counts.get(flag, 0) + 1

# Primary analysis pipeline
processed_logs = []
for i, val in enumerate(filtered_readings):
    record = {
        'id': i,
        'value': val,
        'class': status_flags[i]
    }
    processed_logs.append(record)

# Red herring: unused complex structure
historical_trends = {
    'baseline': [42, 45, 40],
    'drift_pattern': [(1, 0.1), (2, 0.3), (3, 0.2)],
    'decay_factor': 0.95
}

# Real final analysis function
def analyze_readings(logs):
    normal_count = sum(1 for log in logs if log['class'] == 'normal')
    warning_count = sum(1 for log in logs if log['class'] == 'warning')
    critical_count = sum(1 for log in logs if log['class'] == 'critical')
    
    # Complex conditional expression
    severity_score = (
        100 if critical_count > 0 else \
        70 if warning_count > 2 else \
        30 if warning_count > 0 else \
        10
    )
    
    # Final diagnostic computation
    total_valid = len(logs)
    completeness = total_valid / 10.0  # Base metric
    
    # Actual answer derived here
    final_diagnostic = int(severity_score * completeness)
    
    # This print is required
    print(f"Result: {final_diagnostic}")
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = analyze_readings(processed_logs)