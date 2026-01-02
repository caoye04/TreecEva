from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timing_data = [120, 150, 130, 90, 200, 180, 160, 110, 95, 105]
failure_flags = [False, True, False, False, True, False, True, False, False, True]

# Irrelevant telemetry (distractor variables)
voltage_readings = [3.2, 3.3, 3.1, 3.4, 3.25, 3.18, 3.35, 3.28, 3.21, 3.19]
cpu_temps = [68, 72, 65, 70, 75, 69, 73, 67, 71, 74]
log_timestamps = ['00:01', '00:02', '00:03', '00:04', '00:05', '00:06', '00:07', '00:08', '00:09', '00:10']

# Decoy function - looks important but unused
def analyze_voltage_stability(readings):
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    return variance < 0.01

# Another red herring - dead code path
def deprecated_diagnostic(seq):
    if all(x > 50 for x in seq):
        return sum(x ** 0.5 for x in seq if x % 10 == 0)
    return -1

# Misleading intermediate calculation (unused)
baseline_avg = sum(timing_data) / len(timing_data)
adjusted_timings = [x * 0.9 for x in timing_data if x > 100]

# Data transformation with distractors
event_counter = defaultdict(int)
for i, duration in enumerate(timing_data):
    category = 'long' if duration > 140 else 'short'
    event_counter[category] += 1
    # Extra logic that doesn't affect final result
    if failure_flags[i]:
        event_counter['failures_recorded'] += 1

# Use of list comprehension - relevant
failed_durations = [timing_data[i] for i in range(len(failure_flags)) if failure_flags[i]]

# Complex conditional computation chain
smoothness_score = 0
if len(failed_durations) > 0:
    mean_failed = sum(failed_durations) / len(failed_durations)
    if mean_failed > 130:
        smoothness_score += 10
    elif mean_failed > 100:
        smoothness_score += 5
else:
    smoothness_score += 15

# Bit manipulation decoy (irrelevant)
status_word = 0b10101010
masked_word = status_word & 0b11110000
shifted_word = masked_word >> 4

# Another distraction: character counting in fake logs
total_chars = sum(len(ts + 'ms') for ts in log_timestamps)
char_freq = Counter(''.join(log_timestamps))

# Core logic embedded within noise
def aggregate_metrics(times, faults):
    # Step 1: Calculate base reliability index
    total_ops = len(times)
    failed_ops = sum(1 for f in faults if f)
    reliability = (total_ops - failed_ops) / total_ops
    
    # Step 2: Compute performance penalty
    penalty = 0
    for t in times:
        if t > 170:
            penalty += t * 0.05
    
    # Step 3: Apply combinatoric adjustment based on failure clustering
    cluster_score = 0
    for i in range(1, len(faults)):
        if faults[i] and faults[i-1]:
            cluster_score += 1
    
    # Step 4: Final diagnostic formula (combination of arithmetic, logic, sequences)
    raw_diagnostic = reliability * 1000 - penalty
    if cluster_score >= 2:
        raw_diagnostic -= 100
    
    # Step 5: Round to nearest integer
    return int(round(raw_diagnostic))

# Additional misleading post-processing (never used)
optimized_diagnostic = math.floor(smoothness_score * 1.5) + event_counter['long']
legacy_diagnostic = sum(failure_flags) * 50

# Key execution point
final_diagnostic = aggregate_metrics(timing_data, failure_flags)

# Print target result
print(f"Target result: {final_diagnostic}")