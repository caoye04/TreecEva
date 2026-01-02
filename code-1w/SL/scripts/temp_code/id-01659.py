import math

# Simulated sensor data with noise and irrelevant entries
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 18.7, 26.4, 20.2]
signal_strengths = [88, 92, 75, 83, 90, 70, 95, 87]
error_flags = [False, True, False, False, True, False, False, True]

def analyze_trend(data):
    # Irrelevant function - not used in main logic
    if len(data) < 2:
        return 0
    return sum(data[i+1] - data[i] for i in range(len(data)-1))

def filter_noise(values, threshold=20):
    # Correct filtering: only values >= threshold are valid signals
    return [v for v in values if v >= threshold]

def amplify_signal(x):
    # Applies logarithmic amplification to meaningful signals
    return math.log(x) * 1.5 if x > 0 else 0

# Unused transformation - red herring
corrupted_data = [x * 2 + 1 for x in temperature_readings if x < 20]

# Misleading intermediate calculation
baseline_offset = sum(temperature_readings) / len(temperature_readings) - 20

# Dummy state tracking (distractor)
current_mode = "CALIBRATING"
if baseline_offset > 1:
    current_mode = "STABLE"
else:
    current_mode = "ADJUSTING"

# Signal processing chain begins
raw_input_stream = signal_strengths  # Actual source of interest

# Apply non-uniform scaling (distraction)
weighted_values = []
for i, val in enumerate(raw_input_stream):
    weight = 1.1 if i % 2 == 0 else 0.9
    weighted_values.append(val * weight)

# Filter out low-strength signals — relevant step
filtered_data = filter_noise(weighted_values, threshold=80)

# Another distraction: hypothetical fail-safe
redundant_check = any(x < 50 for x in raw_input_stream)
backup_state = {"active": False, "retry_count": 3}

# Core transformation function
def process_signals(signals):
    accumulator = 0.0
    for s in signals:
        # Nonlinear transformation applied to each
        transformed = amplify_signal(s)
        # Accumulate with rounding to simulate precision loss
        accumulator += round(transformed, 4)
    
    # Additional complexity: conditional bonus factor
    if len(signals) > 3:
        accumulator *= 1.1
    else:
        accumulator *= 0.95
    
    # Final truncation to integer
    return int(accumulator)

# Dead code path - never executed but looks important
def emergency_override():
    return sum(corrupted_data) // 2

# Key execution point
temp_diagnostic = [math.ceil(math.sqrt(x)) for x in filtered_data]
final_output = process_signals(filtered_data)

# Output result as required
print(f"Result: {final_output}")