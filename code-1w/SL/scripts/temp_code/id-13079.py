from collections import defaultdict, Counter

# Simulated sensor data with noise and redundant fields
data_stream = [
    {'id': 'A7', 'temp': 23.5, 'humidity': 45, 'status': 'OK', 'meta': [1, 1, 0]},
    {'id': 'B2', 'temp': -19.2, 'humidity': 60, 'status': 'ERR', 'meta': [0, 1, 1]},
    {'id': 'A7', 'temp': 24.1, 'humidity': 47, 'status': 'OK', 'meta': [1, 0, 0]},
    {'id': 'C5', 'temp': 30.0, 'humidity': 30, 'status': 'OK', 'meta': [1, 1, 1]},
    {'id': 'B2', 'temp': -18.9, 'humidity': 62, 'status': 'OK', 'meta': [0, 1, 0]},
    {'id': 'D1', 'temp': 15.3, 'humidity': 80, 'status': 'OK', 'meta': [1, 0, 1]},
]

# Irrelevant statistical counters (distractor)
stats_counter = defaultdict(int)
for entry in data_stream:
    stats_counter[entry['status']] += 1
    stats_counter['total'] += 1

# Noise filter based on meta pattern (partially relevant but misleading)
valid_meta = [1, 1, 1]
def is_clean(entry):
    return entry['meta'] == valid_meta

cleaned_data = [e for e in data_stream if is_clean(e)]

# Primary filtering: group by id and compute average temp only for OK status
working_units = [e for e in data_stream if e['status'] == 'OK']
grouped = defaultdict(list)
for unit in working_units:
    grouped[unit['id']].append(unit['temp'])

averages = {uid: sum(temps) / len(temps) for uid, temps in grouped.items()}

# Decoy function: calculates humidity variance (unused)
def calculate_humidity_risk(records):
    hums = [r['humidity'] for r in records if r['status'] == 'OK']
    mean_hum = sum(hums) / len(hums)
    var = sum((h - mean_hum) ** 2 for h in hums) / len(hums)
    return var * 1.5

# Another red herring: bit analysis of ids (irrelevant)
bit_flags = {}
for entry in data_stream:
    bid = entry['id']
    # Convert last char to ASCII and extract bits
    ascii_val = ord(bid[-1])
    parity = bin(ascii_val).count('1') % 2
    bit_flags[bid] = (ascii_val & 7, parity)

# Threshold logic based on dynamic condition
base_ref = 20.0
tolerance = 5.0
temperature_class = lambda t: 'HIGH' if t > base_ref + tolerance else 'LOW' if t < base_ref - tolerance else 'NORMAL'

# Filter readings: only include sensors whose average temp is NOT in HIGH range
filtered_ids = {uid for uid, avg in averages.items() if temperature_class(avg) != 'HIGH'}
filtered_data = [u for u in working_units if u['id'] in filtered_ids]

# Critical distraction: complex unused transformation chain
transform_chain = [
    lambda x: x * 1.05,
    lambda x: x + 2.1,
    lambda x: abs(x) ** 0.5
]

processed_values = []
for record in filtered_data:
    val = record['temp']
    for func in transform_chain:  # This loop runs but result unused
        val = func(val)
    processed_values.append(val)  # Collected but not used

# Real processing begins here: count occurrences per ID in filtered set
id_frequency = Counter([item['id'] for item in filtered_data])

# Apply threshold function that depends on frequency and base temp
threshold_func = lambda freq, base_temp: (freq * base_temp) / 2.0 if freq > 1 else base_temp * 0.9

# Core diagnostic calculation
final_diagnostic = 0.0
for record in filtered_data:
    fid = record['id']
    freq_score = id_frequency[fid]
    temp_score = record['temp']
    contribution = threshold_func(freq_score, temp_score)
    final_diagnostic += contribution

# Additional decoy: recursive checksum on IDs (never called)
def recursive_checksum(ids, depth=0):
    if depth >= 3 or not ids:
        return 0
    current = sum(ord(c) for c in ''.join(ids)) % 7
    return current + recursive_checksum(ids[:-1], depth + 1)

# Actual output
print(f"Result: {final_diagnostic}")