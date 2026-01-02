from collections import defaultdict, Counter
import math

# Simulated sensor data from a spacecraft subsystem
temperature_readings = [23.5, 24.1, 25.3, 26.0, 25.8, 25.1, 24.7, 24.3, 23.9]
pressure_levels = [101.3, 102.1, 103.5, 104.0, 103.8, 103.0, 102.4, 101.9, 101.5]

# Irrelevant baseline calibration (distractor)
calibration_offset = sum([abs(t - p / 4.3) for t, p in zip(temperature_readings, pressure_levels)])
baseline_reference = math.floor(calibration_offset * 1.7) % 7

# System event log with timestamps and status codes
system_log = [
    {'time': 1001, 'event': 'OK', 'code': 0},
    {'time': 1003, 'event': 'WARN', 'code': 2},
    {'time': 1005, 'event': 'OK', 'code': 0},
    {'time': 1008, 'event': 'ERROR', 'code': 5},
    {'time': 1010, 'event': 'OK', 'code': 0}
]

# Thermal trace derived from temperature readings (relevant)
thermal_trace = []
for i, temp in enumerate(temperature_readings):
    adjusted = temp + 0.3 * math.sin(i)
    thermal_trace.append(round(adjusted, 2))

# Dead code path - never called (red herring)
def legacy_diagnostic(seq):
    return sum(x ** 0.5 for x in seq if x > 20) // len(seq)

# Auxiliary function for noise reduction (partially relevant)
def smooth_signal(signal):
    smoothed = [signal[0]]
    for i in range(1, len(signal) - 1):
        smoothed.append((signal[i-1] + signal[i] + signal[i+1]) / 3)
    smoothed.append(signal[-1])
    return [round(x, 2) for x in smoothed]

# Misleading intermediate diagnostic (decoy)
surface_stability = 0
for reading in thermal_trace:
    if reading > 25.0:
        surface_stability += 1.5
    elif reading < 24.0:
        surface_stability -= 0.8

# Unused complex structure (distractor)
data_cube = defaultdict(lambda: defaultdict(dict))
for idx, val in enumerate(thermal_trace):
    quadrant = idx // 2
    data_cube['temp'][quadrant][idx] = val
    data_cube['flags'][quadrant][idx] = 'HIGH' if val > 25.0 else 'LOW'

# Another decoy function that looks important but isn't used
def compute_entropy(values):
    counts = Counter([int(v * 2) for v in values])
    total = len(values)
    return -sum((count/total) * math.log2(count/total) for count in counts.values())

# Actual core logic disguised among distractions
def analyze_thermal_peaks(trace):
    peaks = []
    for i in range(1, len(trace) - 1):
        if trace[i] > trace[i-1] and trace[i] > trace[i+1]:
            peaks.append(trace[i])
    return peaks

# Secondary analysis on logs (partial relevance)
def count_critical_events(log_entries):
    critical = 0
    for entry in log_entries:
        if entry['code'] >= 4:
            critical += 1
    return critical

# Main computation chain (highly interdependent)
def derive_coherence_index(trace, log):
    # Step 1: Smooth the trace
    processed = smooth_signal(trace)
    
    # Step 2: Find deviation from ideal cooling curve
    ideal_cooling = [26.0 - i*0.2 for i in range(len(processed))]
    deviations = [abs(a - b) for a, b in zip(processed, ideal_cooling)]
    
    # Step 3: Compute weighted variance
    mean_dev = sum(deviations) / len(deviations)
    variance = sum((d - mean_dev)**2 for d in deviations) / len(deviations)
    
    # Step 4: Adjust by event frequency
    event_penalty = count_critical_events(log) * 0.4
    
    # Step 5: Apply non-linear transformation
    coherence = max(0, 10 - math.sqrt(variance) * 2 - event_penalty)
    
    return round(coherence, 4)

# Complex conditional mask (mixed relevance)
mask_threshold = 24.5
activation_map = [1 if t > mask_threshold else 0 for t in thermal_trace]
disruption_score = sum(activation_map) * 0.7

# Decoy variable with plausible name (misleading)
apparent_anomaly = len(analyze_thermal_peaks(thermal_trace)) > 2

# Primary diagnostic function combining multiple concepts
def compute_integrity_score(thermal_data, event_log):
    # Nesting Level 1
    if len(thermal_data) == 0:
        return 0.0
    
    # Nesting Level 2
    peak_analysis = analyze_thermal_peaks(thermal_data)
    base_score = 50.0
    
    # Nesting Level 3
    if len(peak_analysis) > 0:
        avg_peak = sum(peak_analysis) / len(peak_analysis)
        
        # Nesting Level 4
        if avg_peak > 25.5:
            base_score -= 15.0
        elif avg_peak > 25.0:
            base_score -= 8.0
    
    # Incorporate coherence index
    coherence = derive_coherence_index(thermal_data, event_log)
    final_score = base_score + (coherence * 3.5)
    
    # Final adjustment based on event log length
    if len(event_log) >= 5:
        final_score *= 1.1
    
    return round(final_score, 4)

# Irrelevant bit manipulation sequence (red herring)
status_word = 0xABCD
shifted = ((status_word << 3) & 0xFFFF) ^ 0x5A5A
checksum_hack = bin(shifted).count('1') % 4

# Key execution point
final_diagnostic = compute_integrity_score(thermal_trace, system_log)

# Print result as required
print(f"Result: {final_diagnostic}")