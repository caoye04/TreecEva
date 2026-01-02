from collections import Counter, defaultdict
import math

# Simulated system telemetry data
telemetry_stream = [
    'event|cpu:78|mem:45|disk:22',
    'event|cpu:85|mem:60|disk:33',
    'alert|cpu:91|mem:77|disk:40',
    'event|cpu:70|mem:50|disk:25'
]

# Parse logs with distraction parsing paths
def parse_telemetry(stream):
    parsed = []
    temp_buffer = []
    for entry in stream:
        parts = entry.split('|')
        data_map = {}
        for p in parts[1:]:
            k, v = p.split(':')
            data_map[k] = int(v)
        data_map['raw_len'] = len(entry)  # irrelevant metric
        data_map['type'] = parts[0]
        parsed.append(data_map)
    
    # DEAD CODE PATH - never used
    if temp_buffer and sum(len(x) for x in temp_buffer) > 100:
        return sorted(temp_buffer, key=lambda x: x[-1])
    
    return parsed

def compute_entropy(values):
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    entropy = -sum(p * math.log2(p) for p in probs)
    return round(entropy, 6)

def analyze_correlation(x, y):
    n = len(x)
    mean_x, mean_y = sum(x)/n, sum(y)/n
    numerator = sum((x[i]-mean_x)*(y[i]-mean_y) for i in range(n))
    denom_x = sum((xi-mean_x)**2 for xi in x)
    denom_y = sum((yi-mean_y)**2 for yi in y)
    if denom_x == 0 or denom_y == 0:
        return 0.0
    return round(numerator / (math.sqrt(denom_x) * math.sqrt(denom_y)), 6)

def generate_synthetic_data(seed=42):
    # Unused synthetic data generator - red herring
    import random
    random.seed(seed)
    return [random.randint(30, 90) for _ in range(100)]

def filter_critical_events(logs):
    critical = [log for log in logs if log['type'] == 'alert']
    severity = sum(log['cpu'] + log['mem'] for log in critical)
    return severity

def extract_patterns(logs):
    patterns = defaultdict(int)
    cpu_values = [log['cpu'] for log in logs]
    mem_values = [log['mem'] for log in logs]
    
    # Distractor analysis
    patterns['cpu_high'] = sum(1 for v in cpu_values if v > 80)
    patterns['mem_fluctuation'] = max(mem_values) - min(mem_values)
    patterns['stability_score'] = 100 - (sum(abs(cpu_values[i] - cpu_values[i-1]) 
                                    for i in range(1, len(cpu_values))) // len(cpu_values))
    
    # Real computation buried here
    patterns['correlation'] = analyze_correlation(cpu_values, mem_values)
    patterns['entropy_cpu'] = compute_entropy(cpu_values)
    
    return dict(patterns)

def calculate_efficiency_index(logs):
    durations = [log.get('duration', 1) for log in logs]  # default to 1
    efficiencies = []
    for log in logs:
        e = (log['cpu'] * 0.6) + (log['mem'] * 0.3) + (log['disk'] * 0.1)
        efficiencies.append(round(100 - e, 2))  # lower resource = higher efficiency
    return sum(efficiencies) / len(efficiencies)

def evaluate_baseline_drift(metrics, base):
    drift = 0.0
    for key in ['cpu', 'mem', 'disk']:
        if key in base:
            current_avg = sum(m[key] for m in metrics) / len(metrics)
            drift += abs(current_avg - base[key])
    return drift * 1.5  # amplified drift score

def evaluate_performance(data_log, baseline_metrics):
    # Step 1: Extract patterns including correlation
    patterns = extract_patterns(data_log)
    
    # Step 2: Calculate efficiency index
    efficiency = calculate_efficiency_index(data_log)
    
    # Step 3: Evaluate baseline drift
    drift = evaluate_baseline_drift(data_log, baseline_metrics)
    
    # Step 4: Get critical event penalty
    critical_penalty = filter_critical_events(data_log)
    
    # Step 5: Compute composite anomaly score (distraction)
    anomaly_score = (
        patterns['cpu_high'] * 10 + 
        patterns['mem_fluctuation'] * 2 + 
        (100 - patterns['stability_score'])
    )
    
    # Step 6: Main calculation path — uses correlation and entropy
    relevance_factor = patterns['correlation']
    entropy_weight = patterns['entropy_cpu']
    
    # Core reasoning: performance degrades with high entropy and low correlation
    base_score = 1000
    adjustment = (relevance_factor * 150) - (entropy_weight * 50)
    volatility_penalty = drift * 4
    
    # Final score computation
    final_score = base_score + adjustment - volatility_penalty - critical_penalty
    
    # Irrelevant transformations below
    final_score = max(final_score, 10)  # floor at 10
    final_score = round(final_score, 2)
    
    # NEVER USED — decoy transformation chain
    temp_result = final_score * 1.05
    if temp_result > 500:
        temp_result = math.sqrt(temp_result) * 10
    temp_result = temp_result / 0.95
    
    return int(final_score)

# Main execution flow
if __name__ == "__main__":
    # Parse real telemetry
    parsed_logs = parse_telemetry(telemetry_stream)
    
    # Baseline configuration (normal conditions)
    baseline_metrics = {'cpu': 75, 'mem': 50, 'disk': 30}
    
    # Generate unused synthetic dataset
    synthetic_load = generate_synthetic_data(42)
    
    # Build auxiliary counter (partially used)
    event_counter = Counter(log['type'] for log in parsed_logs)
    
    # Data transformation pipeline
    processed_data = []
    for log in parsed_logs:
        transformed = {k: v for k, v in log.items() if k not in ['raw_len']}
        processed_data.append(transformed)
    
    # Call target function
    final_score = evaluate_performance(processed_data, baseline_metrics)
    
    # Print result as required
    print(f"Result: {final_score}")