import math

# Simulated sensor fusion module for autonomous drone navigation

def preprocess_readings(raw):
    filtered = [x for x in raw if -100 <= x <= 100]
    shifted = [x + 5 for x in filtered]
    return shifted[:len(shifted)//2]

# Irrelevant helper - decoy function (dead code path)
def compress_signal(data):
    return [d ^ 7 for d in data][::2]

# Another red herring: audio processing stub (never called)
def analyze_tone(sequence):
    magnitude = sum(abs(s) for s in sequence)
    return magnitude * 0.3 if magnitude > 50 else magnitude * 0.7

# Sensor calibration logic (partially relevant)
def calibrate_sensor(baseline, factor=1.1):
    adjusted = []
    for i in range(len(baseline)):
        if i % 2 == 0:
            adjusted.append(baseline[i] * factor)
        else:
            adjusted.append(baseline[i] / factor)
    return [round(a, 2) for a in adjusted]

# Data validation with string distraction
validation_log = "error_code_45: checksum_mismatch; retry_init=true"
if "retry" in validation_log:
    retry_count = 3
else:
    retry_count = 0

# Extraneous timing variables
latency_offset = 12.8
jitter_buffer = [0.1, 0.4, 0.2]
smoothing_factor = 0.85

# Primary data inputs
raw_timing_pulses = list(range(90, 111))  # 90 to 110 inclusive

# Apply preprocessing (only this matters)
timing_data = preprocess_readings(raw_timing_pulses)

# Flag generation with bit manipulation distraction
flags = set()
for val in timing_data:
    if val > 95:
        flags.add(val & 7)  # Bitwise AND with 7
    if val < 98:
        flags.discard((val - 90) // 2) if (val - 90) // 2 in flags else None

# Unused data structure - misleading container
status_registry = {
    'active': [],
    'pending': tuple(range(5)),
    'failed': {x for x in [1, 3, 5]}
}

# Decoy assignment - looks important but unused
consistency_score = sum(timing_data) / len(timing_data) if timing_data else 0

# String slicing used in fake checksum (irrelevant)
checksum_probe = f"CHK{sum(jitter_buffer):.1f}X"
version_tag = checksum_probe[3:5]  # Slicing distraction

# Core aggregation logic (key)
def aggregate_metrics(readings, flag_set):
    base = sum(readings)
    modifier = 0
    
    # Multiple conditional layers (nesting depth 3)
    if len(flag_set) > 3:
        for f in flag_set:
            if f % 2 == 1:
                if f > 2:
                    modifier += f ** 2
                else:
                    modifier += 10
    else:
        modifier = len(readings)
    
    # Combinatorics distraction
    pair_count = 0
    for i in range(len(readings)):
        for j in range(i+1, len(readings)):
            if abs(readings[i] - readings[j]) == 5:
                pair_count += 1
    
    # Final computation (actual answer path)
    entropy_component = math.log(len(flag_set) + 1) if flag_set else 0
    temporal_weight = len(readings) * 0.7
    
    # Critical calculation
    result = int(base - modifier + temporal_weight - entropy_component)
    
    # Distractor: irrelevant rounding chain
    intermediate = round(result * 1.01, 4)
    final = round(intermediate - 0.5, 0)
    
    return int(final)

# Trigger key computation
final_diagnostic = aggregate_metrics(timing_data, flags)

# Output requirement
print(f"Target result: {final_diagnostic}")