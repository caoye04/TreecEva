from collections import defaultdict, Counter
import itertools

# Simulated system telemetry data
telemetry_stream = [
    {'sensor': 'temp', 'value': 72.5, 'status': 'OK'},
    {'sensor': 'pressure', 'value': 1013.25, 'status': 'OK'},
    {'sensor': 'temp', 'value': 73.1, 'status': 'OK'},
    {'sensor': 'humidity', 'value': 45.0, 'status': 'WARNING'},
    {'sensor': 'temp', 'value': 74.3, 'status': 'OK'},
    {'sensor': 'pressure', 'value': 1012.8, 'status': 'OK'},
    {'sensor': 'humidity', 'value': 47.2, 'status': 'OK'},
    {'sensor': 'temp', 'value': 75.0, 'status': 'CRITICAL'},
    {'sensor': 'pressure', 'value': 1011.9, 'status': 'WARNING'}
]

# Irrelevant transformation: converts sensor names to frequency of letters
letter_freq = defaultdict(int)
for entry in telemetry_stream:
    for char in entry['sensor']:
        letter_freq[char] += 1

# Dead code path: unused function
def analyze_frequency_pattern(freq_dict):
    total = sum(freq_dict.values())
    entropy = 0
    for v in freq_dict.values():
        p = v / total
        entropy -= p * __import__('math').log2(p)
    return entropy

# Unused but plausible-looking metric
frequency_entropy = analyze_frequency_pattern(letter_freq)

# Misleading intermediate: computes average per sensor but not used in final result
duplicate_sensor_avg = defaultdict(list)
for entry in telemetry_stream:
    duplicate_sensor_avg[entry['sensor']].append(entry['value'])
sensor_averages = {k: sum(v)/len(v) for k, v in duplicate_sensor_avg.items()}

# Another red herring: generates all pairwise combinations of readings (not used)
pairwise_combinations = list(itertools.combinations([e['value'] for e in telemetry_stream if e['sensor']=='temp'], 2))
redundant_diffs = [abs(a-b) for a,b in pairwise_combinations if a > 70 and b < 75]

# Core logic disguised among distractions
log_data = []
critical_count = 0
event_sequence = []

for entry in telemetry_stream:
    log_data.append({
        'type': entry['sensor'],
        'val': int(entry['value']),  # truncates decimal part
        'flag': entry['status']
    })
    if entry['status'] == 'CRITICAL':
        critical_count += 1
    event_sequence.append(entry['status'])

# Simulated system state with decoy fields
system_state = {
    'uptime': 86400,
    'load_avg': [1.2, 1.5, 1.7],
    'version': '2.1.9',
    'mode': 'diagnostic',
    'cache_hits': 4217,
    'consecutive_ok': 0
}

# Distractor loop: counts consecutive OK states but uses wrong condition
streak = 0
max_streak = 0
for status in event_sequence:
    if status == 'OK':
        streak += 1
    else:
        max_streak = max(max_streak, streak)
        streak = 0
system_state['consecutive_ok'] = max_streak  # Actually not used in final calculation

# Decoy statistical summary
status_counter = Counter(event_sequence)
warning_level = len(event_sequence) / (status_counter.get('CRITICAL', 1))

# Actual key computation chain
aggregated = defaultdict(int)
for item in log_data:
    aggregated[item['type']] += item['val']  # uses truncated integer value

# Secondary transformation
transformed = []
for k, v in aggregated.items():
    if k == 'temp':
        transformed.append(v * 2)
    elif k == 'pressure':
        transformed.append(v // 3)  # integer division
    else:
        transformed.append(v + 5)

# Final diagnostic depends only on transformed temp value and critical count
base_score = transformed[0]  # temp contributes first
penalty = critical_count * 100
final_diagnostic = base_score - penalty

# Additional distraction: string manipulation unrelated to result
diag_code = ''.join([s[0] for s in sorted(aggregated.keys())])  # 'hpt'
version_tag = f"{system_state['version']}_{diag_code}"

# Output the required variable
print(f"Result: {final_diagnostic}")