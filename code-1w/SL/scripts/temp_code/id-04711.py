from itertools import combinations
from math import log

# Simulated sensor data for wind turbine diagnostics
turbine_data = [104, 95, 112, 87, 98, 103, 115, 89, 94, 100]
thresholds = {"low": 90, "optimal": 105, "high": 110}
diagnostic_flags = set()
anomaly_log = []

# Irrelevant transformation: frequency harmonics (red herring)
frequency_spectrum = [x * 1.5 + 2 for x in turbine_data]
spectral_peaks = [y for y in frequency_spectrum if y > 100]

# Misleading statistical summary (not used in final result)
rolling_avg = sum(turbine_data[1:6]) / 5
variance_estimate = sum((x - sum(turbine_data)/len(turbine_data))**2 for x in turbine_data) / len(turbine_data)

# Auxiliary function: detects sustained high values (used)
def detect_surge(values, limit=110, duration=2):
    count = 0
    surge_periods = 0
    for v in values:
        if v > limit:
            count += 1
        else:
            if count >= duration:
                surge_periods += 1
            count = 0
    if count >= duration:  # check at end
        surge_periods += 1
    return surge_periods

# Dead function: never called (distractor)
def calculate_efficiency_curve(data):
    return [round(log(x) * 0.8, 2) for x in data if x > 0]

# Unused pattern matcher (decoy logic)
pattern_matches = []
for i in range(len(turbine_data) - 2):
    if turbine_data[i] < turbine_data[i+1] < turbine_data[i+2]:
        pattern_matches.append((i, i+2))

# Core diagnostic logic
running_highs = detect_surge(turbine_data, thresholds["high"])

temporal_gaps = 0
for i in range(1, len(turbine_data)):
    if turbine_data[i] - turbine_data[i-1] < -5:
        temporal_gaps += 1

# Generate all 3-element subsequences to check stability (real usage of itertools)
stability_windows = list(combinations([x for x in turbine_data if x > thresholds["low"]], 3))
stable_count = sum(1 for w in stability_windows if max(w) - min(w) <= 8)

# Diagnostic rules engine
if running_highs > 0:
    diagnostic_flags.add("OVERHEAT_RISK")
if temporal_gaps > 2:
    diagnostic_flags.add("FLOW_INTERRUPTION")
if stable_count < 10:
    diagnostic_flags.add("INSTABILITY_DETECTED")

criticality_score = len(diagnostic_flags) * 100 + stable_count // 3

# Data slicing to extract recovery segments (valid use of slicing)
recovery_segments = turbine_data[::3]  # every third reading
baseline_drift = abs(turbine_data[0] - turbine_data[-1])

# Secondary metric: oscillation index
oscillations = 0
for i in range(1, len(turbine_data) - 1):
    if (turbine_data[i] - turbine_data[i-1]) * (turbine_data[i+1] - turbine_data[i]) < 0:
        oscillations += 1

# Main aggregation function
def aggregate_metrics(data, config):
    # Nested logic with multiple steps
    a = sum(1 for x in data if x < config["low"])
    b = sum(1 for x in data if x > config["optimal"])
    c = sum(data) // len(data)
    d = c ^ 15  # Bitwise interference (XOR with magic number)
    
    # Conditional bit flip based on oscillation threshold
    if oscillations > 5:
        d ^= 32  # Toggle bit
    
    # Set-based filtering for anomalous triplets
    valid_triplets = {combo for combo in stability_windows if sum(combo) > 250}
    adjustment_factor = len(valid_triplets) % 7
    
    # Final composition
    intermediate = (b * 1000) + (adjustment_factor * 17) + d
    
    # Red herring: unused conditional branch
    if intermediate > 5000:
        fallback = (a + b) * baseline_drift
        # This branch does not alter output
    
    # Critical assignment
    result = intermediate - (running_highs * 250) + (temporal_gaps * 15)
    
    # Last-minute bitwise correction
    if result % 2 == 0:
        result = result ^ 1  # Ensure oddness
    
    return result

# Execute main computation
final_diagnostic = aggregate_metrics(turbine_data, thresholds)
print(f"Target result: {final_diagnostic}")