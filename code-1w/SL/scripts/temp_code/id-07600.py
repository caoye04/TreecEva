from collections import defaultdict, Counter
import itertools

# Simulated system metrics over time (timestamp, cpu, memory, requests)
raw_data = [
    (1000, 75, 2048, 150), (1001, 80, 2064, 155), (1002, 85, 2096, 160),
    (1003, 90, 2112, 165), (1004, 95, 2144, 170), (1005, 99, 2176, 175)
]

# Irrelevant historical log (decoy data)
historical_logs = [
    {'event': 'startup', 'level': 'INFO'},
    {'event': 'auth_success', 'level': 'DEBUG'},
    {'event': 'timeout', 'level': 'WARN'}
]

# Distractor: unused function that looks important
def analyze_security_threats(logs):
    threat_count = 0
    for entry in logs:
        if entry['level'] == 'WARN' or entry['level'] == 'ERROR':
            threat_count += 1
    return threat_count

# Distractor: dead computation path
total_warnings = 0
for log in historical_logs:
    if log['level'] == 'WARN':
        total_warnings += 1

# Extract relevant performance windows
performance_windows = []
for i in range(0, len(raw_data) - 2):
    window = raw_data[i:i+3]
    avg_cpu = sum(w[1] for w in window) / 3
    avg_mem = sum(w[2] for w in window) / 3
    total_req = sum(w[3] for w in window)
    performance_windows.append((avg_cpu, avg_mem, total_req))

# Compute trend indicators (some are red herrings)
trend_analysis = []
for j in range(1, len(performance_windows)):
    prev_cpu, _, _ = performance_windows[j-1]
    curr_cpu, _, _ = performance_windows[j]
    cpu_delta = curr_cpu - prev_cpu
    stability_index = 1 if abs(cpu_delta) < 5 else 0
    trend_analysis.append(stability_index)

# Misleading intermediate metric (unused later)
avg_stability = sum(trend_analysis) / len(trend_analysis) if trend_analysis else 0

# Real processing begins: filter high-load segments
high_load_segments = [w for w in performance_windows if w[0] > 85]

# Aggregate memory usage per segment (distraction)
memory_map = defaultdict(list)
for seg in high_load_segments:
    mem_key = int(seg[1] // 100)
    memory_map[mem_key].append(seg[1])

# Decoy statistical summary
stats_summary = {}
for k, v in memory_map.items():
    stats_summary[k] = {
        'count': len(v),
        'total': sum(v)
    }

# Core logic: count consecutive stable request patterns
request_counts = [seg[2] for seg in high_load_segments]
consecutive_up = 0
for r in range(1, len(request_counts)):
    if request_counts[r] > request_counts[r-1]:
        consecutive_up += 1
    else:
        break  # only counts initial ascending run

# Baseline threshold computed from first window
baseline_requests = performance_windows[0][2]  # First 3-window total

# Another decoy: permutation analysis of timestamps (irrelevant)
timestamps = [row[0] for row in raw_data]
perm_count = 0
for perm in itertools.permutations(timestamps[:3]):
    if perm[0] < perm[1] < perm[2]:
        perm_count += 1

# Real signal: deviation from baseline in high-load phase
deviation_score = 0
if high_load_segments:
    latest_request_total = high_load_segments[-1][2]
    deviation_score = abs(latest_request_total - baseline_requests)

# Secondary metric: number of high-load windows
coverage_bonus = len(high_load_segments) * 2

# Tertiary: check if memory increased monotonically in high load
memory_values = [seg[1] for seg in high_load_segments]
monotonic_memory = all(m2 >= m1 for m1, m2 in zip(memory_values, memory_values[1:]))

# Bonus for monotonicity
growth_bonus = 15 if monotonic_memory else 0

# Final composition uses only selected components (many distractors ignored)
metrics = {
    'deviation': deviation_score,
    'streak': consecutive_up,
    'bonus': coverage_bonus + growth_bonus
}

baseline = {'threshold': 450, 'penalty_factor': 0.8}

# Key statement containing the answer
final_score = evaluate_performance(metrics, baseline)

# Actual implementation of evaluation function
def evaluate_performance(met, base):
    base_score = 100
    # Only these matter:
    if met['deviation'] > 20:
        base_score -= met['deviation'] * 2
    else:
        base_score += 10
    
    if met['streak'] >= 2:
        base_score += 25
    
    base_score += met['bonus']
    
    # Final adjustment based on hidden rule: must cap at trending max
    trending_max = 137  # Determined from pattern analysis
    return min(base_score, trending_max)

# Print result as required
print(f"Target result: {final_score}")