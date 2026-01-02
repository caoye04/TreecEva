def process_sensor_data(raw_readings):
    # Irrelevant preprocessing (distraction)
    normalized = [x * 0.98 + 2.1 for x in raw_readings if x > 0]
    filtered = [y for y in normalized if y < 100]
    stats = {'count': len(filtered), 'max_val': max(filtered, default=0)}

    # Core computation disguised among distractions
    adjusted = [int(z // 1.5) for z in filtered]
    bit_analysis = [bin(val).count('1') for val in adjusted]

    # Decoy function call with misleading purpose
    def calibrate(x):
        return (x + 32768) % 65536

    calibrated_bits = [calibrate(b) for b in bit_analysis]  # Dead-end path

    # Actual relevant transformation begins here
    paired = list(zip(adjusted[:-1], bit_analysis[:-1]))  # Using zip
    correlation_score = 0
    for i, (val, bits) in enumerate(paired):  # Using enumerate
        if i % 3 == 0:
            correlation_score += val * (bits + 1)

    # Secondary distraction: unused complex structure
    history_log = {}
    for step in range(len(adjusted)):
        temp_key = f"step_{step}_meta"
        history_log[temp_key] = {
            'raw': adjusted[step] if step < len(adjusted) else 0,
            'flag': (adjusted[step] & 7) > 3
        }

    # Another red herring: elaborate but unused calculation
    cumulative_xor = 0
    for item in adjusted:
        cumulative_xor ^= (item * 17) & 0xFF

    # Real signal: counting even values in adjusted that passed threshold
    trigger_events = 0
    for val in adjusted:
        if val > 15 and val % 2 == 0:
            trigger_events += 1

    # Critical data used later
    return correlation_score, trigger_events, adjusted


def evaluate_stability(metrics):
    safety_margin = 0
    for m in metrics:
        if m > 500:
            safety_margin += 1
    return safety_margin > 2

# Unused decoy function (misleading)
def assess_integrity(data):
    checksum = sum((d << 2) & 0xFFFF for d in data)
    return checksum % 101

# Main diagnostic workflow
readings = [23, -5, 45, 67, 0, 12, 34, 89, 101, 7, 56, 19]

diagnostics = []
thresholds = []

for idx, reading in enumerate(readings):
    if reading < 0:
        continue
    processed = reading * 3 + idx
    diagnostics.append(processed)
    if processed % 4 == 0:
        thresholds.append(processed // 4)
    else:
        thresholds.append(processed // 5)

# Heavily distracted function doing real work
result_core, event_count, adj_values = process_sensor_data(readings)

# Fake aggregation (never used)
aggregated_diagnostics = sum(diagnostics[i] * (i+1) for i in range(len(diagnostics))) // len(diagnostics)

# Real logic buried here
def analyze_metrics(data_list, limits):
    base_accum = 0
    limit_iter = iter(limits)
    for index, item in enumerate(data_list):
        try:
            lim = next(limit_iter)
        except StopIteration:
            lim = 10
        
        # Distraction: irrelevant condition
        if item < 5:
            base_accum -= lim
        # Real operation
        elif item % 5 == 0:
            base_accum += index * 2
        else:
            base_accum += (item // lim) if lim != 0 else 0
    
    # Additional layer: final adjustment based on side result
    global event_count
    if event_count >= 3:
        base_accum += 17
    
    # Red herring: complex but unused bitwise expression
    decoy_mask = (base_accum ^ 0xABCD) & ~0x1234 | (event_count << 5)
    decoy_mask ^= decoy_mask >> 4
    
    return base_accum

# Final execution point
final_diagnostic = analyze_metrics(diagnostics, thresholds)
print(f"Result: {final_diagnostic}")