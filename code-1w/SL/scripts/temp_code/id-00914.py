def analyze_metrics(data):
    # Irrelevant transformation (dead path)
    temp_buffer = [x * 1.5 for x in data if x > 10]
    temp_buffer = [x for x in temp_buffer if x < 50]

    # Core metric calculation (obscured by noise)
    base_values = [x for x in data if x % 2 == 0]
    adjusted = [x + (x // 4) for x in base_values]

    # Distractor: complex but unused list operation
    shadow_copy = data.copy()
    shadow_copy.reverse()
    shadow_copy = [x ** 0.5 for x in shadow_copy if x > 5]

    # Actual relevant logic buried here
    threshold_mask = [x for x in adjusted if x > 15]
    return sum(threshold_mask)


def filter_anomalies(records):
    # Red herring function – looks important but not used
    clean = []
    for r in records:
        if r < 0:
            continue
        elif r in {7, 13, 19}:
            clean.append(r * 2)
        else:
            clean.append(r)
    return set(clean)


def compute_entropy(seq):
    from math import log2
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    total = len(seq)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 6)  # Unused result

# Decoy data structures
system_cache = [0] * 100
debug_trace = {'status': 'active', 'mode': 'diagnostic'}

# Key input data
raw_input = [8, 12, 6, 22, 14, 3, 16, 9, 20, 11]

# Irrelevant pre-processing
shifted_data = [x + 5 for x in raw_input]
shifted_data = [x for x in shifted_data if x % 3 != 0]

# Hidden dependency
primary_stream = [x for x in raw_input if x >= 10]

# Set operations (required feature)
metric_set = set(raw_input)
metric_set.add(25)
metric_set.discard(3)
metric_set.update([14, 18])

# Multiple distractions: fake control flows
flag = True
if flag:
    dummy_var = sum(x * x for x in raw_input if x < 5)
    temp_result = None
    for i in range(2):
        temp_result = [i ** j for j in range(3)]

# Simulated intermediate results that mislead
baseline = sum(x for x in raw_input if x in {8, 12, 22}) // 3
offset = len(metric_set) * 2 - 5

# Real computation path begins here — hard to isolate
processed = analyze_metrics(raw_input)

# Fake entropy use
e_val = compute_entropy(raw_input)

# Critical statement where answer is determined
final_score = processed + len(metric_set) * 3

# Another decoy assignment
final_score = final_score if final_score > 100 else final_score + 20

# Output must be printed exactly like this
print(f"Result: {final_score}")