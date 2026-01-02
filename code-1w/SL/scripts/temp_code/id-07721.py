from collections import defaultdict, Counter

def analyze_events(raw_logs):
    event_count = defaultdict(int)
    priority_flags = [False] * len(raw_logs)
    temp_analysis = []

    for i, log in enumerate(raw_logs):
        parts = log.split('|')
        level = parts[1].strip()
        code = int(parts[2].strip())
        event_count[level] += 1

        if code > 500:
            priority_flags[i] = True

        if 'ERROR' in level:
            temp_analysis.append(code * 0.1)

    # Distractor: unused computation
    sum_temp = sum(temp_analysis) if temp_analysis else 0.0
    normalized = [x / (sum_temp or 1) for x in temp_analysis]

    return event_count, priority_flags

def compute_diagnostic_score(data_stream, config):
    score = 0
    history = []
    for val in data_stream:
        if val < config['min']:
            continue
        elif val > config['max']:
            history.append(val)
            break
        else:
            score += val % 7
    # Dead path: never executed due to logic above
    if len(history) == 0 and False:
        score *= 2
    return score

def filter_anomalies(records):
    anomalies = set()
    seen = set()
    for i, r in enumerate(records):
        if r in seen:
            anomalies.add(i)
        seen.add(r)
    # Decoy function with irrelevant transformation
    transformed = [r ^ 255 for r in records if r < 100]
    return anomalies

def process_metrics(logs, thresholds):
    codes = []n    levels = []
    for log in logs:
        _, level, code_str = map(str.strip, log.split('|'))
        levels.append(level)
        codes.append(int(code_str))

    level_counter = Counter(levels)
    total_critical = level_counter['CRITICAL'] + level_counter['ERROR']

    avg_code = sum(codes) / len(codes) if codes else 0
    adjusted_avg = avg_code * (1.0 + 0.05 * total_critical)

    # Key intermediate result (misleading)
    preliminary_diag = int(adjusted_avg // 3)

    # Red herring: complex but unused bitwise manipulation
    magic_mask = 0b101010
    decoy_state = 0
    for c in codes:
        decoy_state ^= (c & magic_mask) << 1
        if decoy_state > 1000:
            decoy_state = decoy_state % 1000

    # Real signal path: find first code above threshold with even index
    valid_indices = []
    for i, c in enumerate(codes):
        if c > thresholds.get('primary', 400) and i % 2 == 0:
            valid_indices.append(c)

    selected_value = valid_indices[0] if valid_indices else 0

    # Final computation using both statistical and positional logic
    correction_factor = len([c for c in codes if c % 10 == 0])
    final_diagnostic = selected_value - correction_factor + preliminary_diag

    # Irrelevant container transformation
    zip_result = list(zip(levels, [c * 2 for c in codes]))
    enum_check = [i for i, (lvl, _) in enumerate(zip_result) if lvl == 'WARNING']

    return final_diagnostic

# Simulated system log entries (real input)
log_entries = [
    "SYS|INFO    |200",
    "NET|WARNING |302",
    "SEC|ERROR   |404",
    "HWM|CRITICAL|501",
    "MEM|DEBUG   |100",
    "CPU|CRITICAL|603",
    "DISK|INFO   |205"
]

system_thresholds = {
    'primary': 400,
    'backup': 300,
    'timeout': 5
}

# Execute analysis chain
raw_counts, flags = analyze_events(log_entries)
score = compute_diagnostic_score([10, 20, 60, 80], {'min': 15, 'max': 75})
anomalous_positions = filter_anomalies([100, 200, 100, 300])

# Critical execution point
final_diagnostic = process_metrics(log_entries, system_thresholds)

print(f"Result: {final_diagnostic}")