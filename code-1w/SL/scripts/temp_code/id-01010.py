def analyze_frequency(text):
    freq = {}
    for char in text.lower():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    return freq

# Irrelevant helper function (dead code path)
def normalize_vector(v):
    magnitude = sum(x ** 2 for x in v) ** 0.5
    return [x / magnitude for x in v] if magnitude else v

# Simulate system health metrics (some relevant, some not)
def compute_health_factor(loads, thresholds):
    overload_count = 0
    for i in range(len(loads)):
        if loads[i] > thresholds.get(f'server_{i}', 90):
            overload_count += 1
    return 10 - overload_count

# Main logic for scoring
stats = {'hits': 85, 'misses': 15, 'latency_avg': 42, 'retries': 3}
modifiers = {'boost': 1.2, 'penalty': 0.9, 'decay': 0.99}

# Distractor: unused variables
baseline = 70
thresholds = {'server_0': 85, 'server_1': 95, 'server_2': 90}
signal_data = [0.1, 0.3, 0.4, 0.2]
normalized_signal = normalize_vector(signal_data)  # Computed but unused

# Simulate frequency analysis on access pattern
access_pattern = "ABCDABEAC"
frequency_map = analyze_frequency(access_pattern)  # Used to derive 'consistency'
consistency = len([v for v in frequency_map.values() if v > 1])

# Compute auxiliary score components
base_score = stats['hits'] * 2 - stats['misses'] * 3
latency_bonus = 10 if stats['latency_avg'] < 50 else 0
retry_penalty = stats['retries'] * 5

# Intermediate distractor computation
estimated_load = (stats['hits'] + stats['misses']) * stats['latency_avg'] / 100
projected_load = estimated_load * 1.1  # Not used later

health_metrics = [88, 82, 91]
health_factor = compute_health_factor(health_metrics, thresholds)

# Core calculation chain
adjusted_base = base_score + latency_bonus - retry_penalty
if consistency >= 2:
    adjusted_base = int(adjusted_base * modifiers['boost'])
else:
    adjusted_base = int(adjusted_base * modifiers['penalty'])

# Apply decay based on retries (only if retries > 0)
if stats['retries'] > 0:
    for _ in range(stats['retries']):
        adjusted_base *= modifiers['decay']

# Final composition
final_score = int(adjusted_base + health_factor)

# Output result
print(f"Result: {final_score}")