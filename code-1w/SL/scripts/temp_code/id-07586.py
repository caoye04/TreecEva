from collections import defaultdict, Counter
import math

# Simulated sensor data: timestamp -> metric readings
data_stream = [
    (1001, 'cpu', 78), (1002, 'mem', 85), (1003, 'disk', 45),
    (1004, 'cpu', 88), (1005, 'mem', 90), (1006, 'disk', 50),
    (1007, 'cpu', 92), (1008, 'mem', 94), (1009, 'disk', 55),
    (1010, 'cpu', 95), (1011, 'mem', 97), (1012, 'disk', 60)
]

# Irrelevant historical log entries (distractor)
log_archive = [
    "ERR_CRITICAL: Timeout at node 7", "WARN: High latency observed",
    "INFO: System rebooted at 03:14", "DEBUG: Cache flushed successfully"
]

# Parse logs for error count (red herring - not used later)
error_count = sum(1 for log in log_archive if log.startswith("ERR"))
debug_count = sum(1 for log in log_archive if log.startswith("DEBUG"))

# Extract time-series by type
metrics_ts = defaultdict(list)
for ts, typ, val in data_stream:
    metrics_ts[typ].append((ts, val))

# Define threshold levels (real input to logic)
thresholds = {
    'cpu': (80, 90),      # (warning, critical)
    'mem': (85, 95),
    'disk': (50, 58)
}

# Compute rolling exponential moving average (complex distractor)
def ema(values, alpha=0.3):
    if not values:
        return 0.0
    avg = values[0]
    for v in values[1:]:
        avg = alpha * v + (1 - alpha) * avg
    return round(avg, 3)

# Misleading health score using EMA (dead path)
ems_cpu = ema([v for _, v in metrics_ts['cpu']])
ems_mem = ema([v for _, v in metrics_ts['mem']])
ems_disk = ema([v for _, v in metrics_ts['disk']])

raw_health_score = (100 - ems_cpu) * 0.4 + (100 - ems_mem) * 0.5 + (100 - ems_disk) * 0.1

# Real processing begins here -------------------------

# Count how many times each metric exceeded critical threshold
breach_count = defaultdict(int)
for typ, readings in metrics_ts.items():
    warn_level, crit_level = thresholds[typ]
    for _, val in readings:
        if val > crit_level:
            breach_count[typ] += 1

# Bitwise aggregation of breach patterns (key transformation)
# cpu: 3 breaches -> binary 11, mem: 2 -> 10, disk: 1 -> 01
aggregated_flag = 0
for i, key in enumerate(['cpu', 'mem', 'disk']):
    shifts = breach_count[key]
    temp_mask = (shifts & 3) << (2 * i)  # Use only 2 bits per metric
    aggregated_flag ^= temp_mask  # XOR into flag (bit manipulation)

# String-based anomaly signature (set and string operations)
anomaly_tags = set()
for log in log_archive:
    words = log.lower().split(':')
    if len(words) > 1:
        action = words[1].strip().split()[0]  # First word after category
        anomaly_tags.add(action)

# Dummy transformation of tags (irrelevant)
signature = ''.join(sorted({tag[0] for tag in anomaly_tags}))  # First letters

# Core diagnostic logic: uses breach counts and thresholds
# Only this part matters for final answer

def evaluate_stress_level(counts, tholds):
    level = 0
    for metric in ['cpu', 'mem', 'disk']:
        crit = tholds[metric][1]
        c = counts[metric]
        if c >= 3 and crit < 90:
            level += 100
        elif c == 2:
            level += 50
        elif c == 1:
            level += 25
    return level

stress_base = evaluate_stress_level(breach_count, thresholds)

# Secondary adjustment based on pattern
pattern_key = tuple(sorted(breach_count[m] for m in ['cpu', 'mem', 'disk']))

# Apply multiplier based on pattern (e.g., escalating trend)
multipliers = {
    (1, 2, 3): 1.8,
    (2, 2, 2): 1.5,
    (3, 2, 1): 1.2,
    (1, 1, 1): 1.0
}
if pattern_key in multipliers:
    stress_factor = multipliers[pattern_key]
else:
    # Default: geometric mean influence
    prod = 1
    for x in pattern_key:
        prod *= max(x, 1)
    stress_factor = round(math.sqrt(prod) / 2.0, 2)

interim_score = stress_base * stress_factor

# Final transformation with modular arithmetic and bit mixing
def finalize(diag, flag, seed=17):
    # Mix in flag via bitwise AND and rotation
    rotated = ((flag << 3) | (flag >> 5)) & 0xFF
    combined = (diag ^ rotated) + seed
    checksum = (combined * 31) % 997
    return abs(checksum - 500)  # Normalize around center

# Key execution point
final_diagnostic = process_metrics(health_data, thresholds)

# But we haven't defined process_metrics yet — that's the trap!
# Let's define it now — it's just a wrapper

def process_metrics(data, tholds):
    bc = defaultdict(int)
    for t, ty, v in data:
        if ty in tholds and v > tholds[ty][1]:
            bc[ty] += 1
    base = 0
    for k in ['cpu', 'mem', 'disk']:
        if bc[k] >= 3:
            base += 100
        elif bc[k] == 2:
            base += 50
        elif bc[k] == 1:
            base += 25
    p = tuple(sorted(bc[m] for m in ['cpu', 'mem', 'disk']))
    f = multipliers[p] if p in multipliers else math.sqrt(max(p[0]*p[1]*p[2], 1)) / 2
    s = base * f
    flag_val = 0
    for idx, met in enumerate(['cpu', 'mem', 'disk']):
        sh = (bc[met] & 3) << (2 * idx)
        flag_val ^= sh
    r_flag = ((flag_val << 3) | (flag_val >> 5)) & 0xFF
    c_val = (int(s) ^ r_flag) + 17
    chk = (c_val * 31) % 997
    return int(abs(chk - 500))

# Now reassign with correct function call
final_diagnostic = process_metrics(data_stream, thresholds)

print(f"Target result: {final_diagnostic}")