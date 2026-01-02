import itertools

# Simulated sensor data with noise and redundant fields
data_stream = [
    {'id': 1, 'val': 3.2, 'meta': 'A', 'err': 0.1, 'flag': True},
    {'id': 2, 'val': 5.8, 'meta': 'B', 'err': 0.4, 'flag': False},
    {'id': 3, 'val': 2.1, 'meta': 'A', 'err': 0.05, 'flag': True},
    {'id': 4, 'val': 7.5, 'meta': 'C', 'err': 0.3, 'flag': True},
    {'id': 5, 'val': 4.4, 'meta': 'B', 'err': 0.2, 'flag': False}
]

# Irrelevant transformation: converts metadata to dummy codes (not used in final logic)
meta_mapping = {'A': 100, 'B': 200, 'C': 300}
def translate_meta(record):
    return meta_mapping.get(record['meta'], -1) * record['err']

# Decoy function that appears useful but is never called
def analyze_trend(data):
    return sum(d['val'] * 0.5 for d in data if d['flag']) // len(data)

# Unused recursive summation (red herring)
def recursive_sum(lst, idx=0):
    if idx >= len(lst):
        return 0
    return lst[idx]['val'] + recursive_sum(lst, idx + 1)

# Distractor: precomputed values with no impact
total_raw = sum(item['val'] for item in data_stream)
avg_err = sum(item['err'] for item in data_stream) / len(data_stream)
flagged_count = len([x for x in data_stream if x['flag']])

# Real processing begins: filter valid entries based on flag and error threshold
valid_entries = [item for item in data_stream if item['flag'] and item['err'] < 0.25]

# Apply nonlinear correction using logarithmic scaling (relevant)
corrected_vals = [d['val'] * (1 + 0.1 * d['id']) for d in valid_entries]

# Use itertools to generate sliding window pairs (only first pair used later)
pairwise_deltas = [abs(a - b) for a, b in itertools.pairwise(corrected_vals)]

# Secondary filtering: only high-confidence corrected values
threshold = 4.0
high_confidence = [cv for cv in corrected_vals if cv > threshold]

# Simulate validation against baseline reference
baseline_ref = [4.5, 5.0, 6.0, 7.0]
matches = [any(abs(hc - br) < 0.5 for br in baseline_ref) for hc in high_confidence]
match_count = sum(matches)

# Compute match quality score using exponential weighting
quality_weights = [1.5 ** i for i in range(len(matches))]
weighted_match_score = sum(m * w for m, w in zip(matches, quality_weights))

# Dummy aggregation (unused)
flat_vals = list(itertools.chain.from_iterable([[v] * 1 for v in corrected_vals]))
compressed = [round(f, 1) for f in flat_vals if f > 4.0]

# Core logic: compute precision-adjusted result
precision_factor = len(high_confidence) * 10
adjustment = 0.95 if match_count >= 2 else 0.85
raw_performance = sum(high_confidence) / len(high_confidence) if high_confidence else 0

# Final computation path
interim_result = raw_performance * adjustment * precision_factor

# Additional distraction: string-based encoding of results (irrelevant)
status_code = ''.join([chr(97 + int(d['val'])) for d in valid_entries if d['val'] < 6.0])
version_stamp = f"V2.{len(valid_entries)}{len(high_confidence)}"

# Critical execution point
final_score = int(interim_result) + 5  # offset added for calibration

Result: {final_score}