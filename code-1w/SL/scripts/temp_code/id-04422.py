import itertools

# Simulated sensor array data from a distributed monitoring system
def process_sensor_readings(raw_readings, threshold=0.75):
    filtered_data = [x for x in raw_readings if abs(x) > threshold]
    normalized = [round(x / max(raw_readings), 4) for x in filtered_data]
    return normalized

# Legacy function – retained for compatibility but not used in current logic
def deprecated_analysis(data):
    return sum([d**2 for d in data if d > 0]) / len(data)

# Core transformation pipeline
def generate_features(mapped_signals):
    transformed = []
    for i, val in enumerate(mapped_signals):
        if i % 3 == 0:
            transformed.append(val * 1.8 + 32)  # Irrelevant conversion (Fahrenheit)
        elif i % 3 == 1:
            transformed.append(val * 2.54)  # Another red herring (cm conversion)
        else:
            transformed.append(abs(val) ** 0.5)  # Actual useful feature: square root magnitude
    return transformed

# Advanced correlation engine (over-engineered but contains key logic)
def compute_interleaved_ranks(data_sequence):
    ranked = list(itertools.accumulate(sorted(data_sequence, reverse=True)))
    cycle = itertools.cycle([1, -1])
    signed_ranks = [rank * next(cycle) for rank in ranked[:len(data_sequence)]]
    
    # Distractor: complex but unused structure
    decoy_mapping = {i: (val, val ** 2, abs(val) < 1e-3) for i, val in enumerate(signed_ranks)}
    
    # Real usage: only the sum matters
    return sum(signed_ranks)

# Unused helper – looks important but doesn't contribute
def validate_consistency(arr):
    return all(a <= b for a, b in zip(arr, arr[1:]))

# Main diagnostic calculator
def aggregate_metrics(features, offset):
    base_score = 0
    for idx, f in enumerate(features):
        if idx % 4 == 0:
            base_score += f * 3
        elif idx % 4 == 2:
            base_score -= f * 1.5
        else:
            base_score += f * 0.75
    return int(base_score - offset)

# --- Execution Workflow ---

# Simulated input: synthetic signal from remote telemetry
raw_input_stream = [0.12, -0.88, 0.45, 1.32, -2.05, 0.09, 1.67, -0.73, 3.11, 0.24, -1.42]

# Step 1: Filter and normalize sensor data
processed_frame = process_sensor_readings(raw_input_stream, threshold=0.7)

# Step 2: Apply transformation chain (contains multiple paths)
engineered_features = generate_features(processed_frame)

# Step 3: Compute auxiliary metric (looks critical but unused)
baseline_diagnostic = deprecated_analysis(processed_frame)

# Step 4: Generate side-channel analysis (distractor computation)
sideband_ranks = compute_interleaved_ranks(processed_frame)

# Step 5: Derive offset using set operations (actual relevant step)
unique_magnitudes = set(round(abs(x), 2) for x in processed_frame)
sign_set = set(1 if x > 0 else -1 for x in processed_frame)
overlap_count = len(unique_magnitudes & sign_set)  # Always 0, but included for confusion

# Real offset calculation hidden among distractors
magnitude_sum = sum(unique_magnitudes)
dynamic_offset = int(magnitude_sum * len(unique_magnitudes)) // 2

# Misleading branch (dead code path)
if len(sign_set) > 2:
    dynamic_offset += 100  # Never executed

# Final computation
final_diagnostic = aggregate_metrics(engineered_features, dynamic_offset)

# Output result
print(f"Result: {final_diagnostic}")