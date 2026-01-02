from collections import defaultdict, Counter

# Simulated system performance metrics over time
timing_data = [0.45, 0.32, 0.78, 0.12, 0.54, 0.89, 0.23, 0.67]
error_flags = [False, True, False, False, True, False, False, True]
resource_usage = [45, 67, 52, 33, 71, 88, 40, 56]

def analyze_trend(data):
    trend_scores = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_scores.append(1)
        elif data[i] < data[i-1]:
            trend_scores.append(-1)
        else:
            trend_scores.append(0)
    return trend_scores

def count_transitions(flags):
    transitions = 0
    for i in range(1, len(flags)):
        if flags[i] != flags[i-1]:
            transitions += 1
    return transitions

# Irrelevant helper - dead code path (distractor)
def deprecated_normalization(x):
    return x / max(x) if max(x) != 0 else x

# Unused function - misleading intermediate result
def calculate_variance(lst):
    mean = sum(lst) / len(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

class PerformanceAnalyzer:
    def __init__(self):
        self.cache = defaultdict(int)
        self.iteration_log = []

    def process_batch(self, raw_values):
        normalized = []
        for idx, val in enumerate(raw_values):
            temp_val = val
            if idx % 2 == 0:
                temp_val = temp_val * 1.1
            else:
                temp_val = temp_val * 0.95
            normalized.append(round(temp_val, 3))
        return normalized

    def aggregate_metrics(self, timed, errors, resources):
        analysis = {}
        trend_timing = analyze_trend(timed)
        trend_resources = analyze_trend(resources)
        
        # Distractor computation with zip and enumerate (partially relevant)
        weighted_components = []
        for i, (t, e, r) in enumerate(zip(timed, errors, resources)):
            base_weight = 0.5 if not e else 0.2
            timing_factor = 1 + (len(trend_timing[:i]) * 0.01) if i > 0 else 1
            resource_factor = (100 - r) / 100
            score = t * base_weight * timing_factor * resource_factor
            weighted_components.append(score)
            self.cache[f'entry_{i}'] = score  # Logging, not used later

        # Decoy logic - looks important but unused
        error_counter = Counter(errors)
        self.iteration_log.append(f'Errors: {error_counter[True]}')
        
        return weighted_components

# Misleading standalone function
def estimate_efficiency(data):
    total = 0
    for d in data:
        if d > 0.5:
            total += d * 2
        else:
            total += d * 0.5
    return round(total, 4)

# Main evaluation logic
def evaluate_performance(metrics_dict, weight_map):
    composite = 0
    for key, values in metrics_dict.items():
        if key == 'response_time':
            avg_time = sum(values) / len(values)
            inverse_time = 1 - avg_time  # Better if lower
            composite += inverse_time * weight_map[key]
        elif key == 'resource_load':
            avg_load = sum(values) / len(values)
            load_penalty = (avg_load / 100) * 0.8
            composite += (1 - load_penalty) * weight_map[key]
        elif key == 'stability':
            stability_score = 0.9 if values.count(True) < 3 else 0.6
            composite += stability_score * weight_map[key]
    return int(composite * 100)  # Discretized final score

# Initialize analyzer
analyzer = PerformanceAnalyzer()

# Process raw inputs (distractor usage)
timing_adj = analyzer.process_batch(timing_data)

# Build metric dictionary using zip and enumerate (core relevance)
metrics = {}
for i, (t, e, r) in enumerate(zip(timing_data, error_flags, resource_usage)):
    if i not in [2, 5]:  # Skip some entries arbitrarily
        continue
    if 'response_time' not in metrics:
        metrics['response_time'] = []
    metrics['response_time'].append(t)
    
    if 'resource_load' not in metrics:
        metrics['resource_load'] = []
    metrics['resource_load'].append(r)

# Add stability from error flag transitions (key step)
transitions = count_transitions(error_flags)
metrics['stability'] = [flag for flag in error_flags if flag]  # Only True values

# Weights map - actual impact on final calculation
weights = {
    'response_time': 0.4,
    'resource_load': 0.35,
    'stability': 0.25
}

# Final evaluation point
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Target result: {final_score}")