import math

def analyze_signal_strength(signal_packet, threshold=0.75):
    if len(signal_packet) == 0:
        return 0
    filtered_readings = [x for x in signal_packet if x > threshold]
    return sum(filtered_readings) / len(signal_packet)


def compute_phase_shift(frequency, amplitude):
    # Irrelevant computation - decoy function
    if frequency <= 0:
        return 0.0
    shift = (amplitude * math.sin(frequency)) / (frequency + 1e-9)
    return round(shift, 6)


def evaluate_consistency(log_entries):
    # Dead code path - never called
    count = 0
    for entry in log_entries:
        if isinstance(entry, str) and 'ERROR' in entry:
            count += 1
    return count

# Simulated sensor data stream
raw_data_stream = [0.42, 0.81, 0.33, 0.94, 0.67, 0.51, 0.78, 0.91, 0.29]

# Baseline calibration offset (used later)
baseline_offset = 2.15

# Misleading intermediate transformation
transformed = [round(math.log(x + 1), 4) for x in raw_data_stream if x > 0.5]
decoy_aggregate = sum(transformed) / len(transformed) if transformed else 0.0

# Key processing chain with relevant logic embedded
processing_chain = []
for val in raw_data_stream:
    if val < 0.5:
        continue
    adjusted = val * 1.2
    if adjusted > 1.0:
        adjusted = 1.0
    processed_val = math.pow(adjusted, 1.5)
    processing_chain.append(processed_val)

# Red herring: unused control flow with bit manipulation
flag_state = 0b1010
if flag_state & 0b1000:
    temp_flag = flag_state ^ 0b1111
    flag_state = temp_flag | 0b0101

# Simulate historical averages (distractor)
historical_averages = [0.61, 0.72, 0.68, 0.77, 0.65]
avg_historical = sum(historical_averages) / len(historical_averages)

# Core aggregation function that determines final result
def aggregate_metrics(data_list, offset):
    if not data_list:
        return offset
    total = sum(data_list)
    count = len(data_list)
    mean_val = total / count
    # Apply non-linear correction based on offset
    corrected = mean_val * (1 + math.sin(offset))
    # Final adjustment using bitwise-inspired scaling (conceptual, not actual bits)
    scale_factor = 3 if int(offset) & 1 else 5
    return corrected * scale_factor

# Secondary decoy calculation
snapshot_moment = 3.14159
harmonic_distortion = math.cos(snapshot_moment) * 100

# Critical execution point
final_diagnostic = aggregate_metrics(processing_chain, baseline_offset)

# Output the required result
print(f"Target result: {final_diagnostic}")