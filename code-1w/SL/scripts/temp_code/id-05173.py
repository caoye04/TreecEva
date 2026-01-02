from collections import defaultdict, Counter
import math

# Simulated system health monitoring with performance metrics
def generate_metrics():
    raw_data = [120, 85, 90, 77, 110, 64, 95, 100]
    processed = []
    for val in raw_data:
        if val > 100:
            processed.append((val - 100) * 1.5)
        elif val > 80:
            processed.append((val - 80) * 1.2)
        else:
            processed.append(max(0, val - 50) * 0.8)
    return processed

def analyze_trends(data):
    trend_scores = defaultdict(float)
    changes = [data[i] - data[i-1] for i in range(1, len(data))]
    pos_changes = [c for c in changes if c > 0]
    neg_changes = [c for c in changes if c <= 0]
    
    # Irrelevant aggregation (distractor)
    avg_positive = sum(pos_changes) / len(pos_changes) if pos_changes else 0
    avg_negative = sum(neg_changes) / len(neg_changes) if neg_changes else 0
    
    trend_scores['volatility'] = sum(abs(c) for c in changes) / len(changes)
    trend_scores['momentum'] = sum(c for c in changes if c > 0) * 0.7
    
    # Dead code path (never used)
    if len(pos_changes) > 10:
        trend_scores['growth_streak'] = max([i for i in range(len(changes)) if changes[i] > 0])
    
    return trend_scores

def calculate_efficiency(raw):
    efficiency_map = {}
    total_ops = 0
    idle_cycles = 0
    for i, r in enumerate(raw):
        if i % 3 == 0:
            total_ops += int(r // 3)
        elif i % 4 == 0:
            idle_cycles += int(r // 5)
        efficiency_map[f'node_{i}'] = r * 0.95  # Distractor mapping
    
    # Unused calculation
    theoretical_max = sum(raw) * 0.9
    actual_output = total_ops * 1.1
    
    return actual_output / (theoretical_max + 1e-8)

def filter_outliers(scores):
    mean = sum(scores) / len(scores)
    std = math.sqrt(sum((x - mean) ** 2 for x in scores) / len(scores))
    return [s for s in scores if abs(s - mean) <= 2 * std]

def build_metric_set():
    base_metrics = generate_metrics()
    filtered = filter_outliers(base_metrics)
    
    # Bit manipulation red herring
    magic_flag = 0b1010
    shift_key = (magic_flag << 2) ^ 0b1100
    encoded_length = len(filtered) ^ shift_key
    
    # Real usage
    metric_set = {
        'values': filtered,
        'size_hint': encoded_length,  # Not actually used correctly
        'source': 'system_monitor_v2'
    }
    
    # Unused nested structure (misleading)
    metric_set['diagnostics'] = {
        'checksum': sum(filtered) % 17,
        'flags': [True, False, True],
        'history': [{'epoch': 1, 'valid': False}]  # Dead data
    }
    
    return metric_set

def evaluate_performance(ms, benchmark_data):
    values = ms['values']
    trends = analyze_trends(values)
    efficiency = calculate_efficiency(benchmark_data)
    
    # Core logic (interleaved with distractors)
    base_score = sum(values)
    volatility_penalty = trends['volatility'] * 1.8
    momentum_boost = trends['momentum'] * 0.4
    efficiency_factor = efficiency * 50
    
    # Multiple interfering calculations
    phantom_score = 0
    for v in values:
        if v > 30:
            phantom_score += math.log(v) * 0.1
    # This is unused!

    # Actual score computation
    raw_final = base_score - volatility_penalty + momentum_boost + efficiency_factor
    
    # Normalize but ensure it's not too clean
    adjustment = (len(values) * 0.5) - 2.5
    final_score = int(raw_final - adjustment)
    
    # Critical print for result visibility
    print(f"Result: {final_score}")
    return final_score

# Main execution flow
if __name__ == "__main__":
    # Benchmark data (simulates system load inputs)
    benchmark_data = [200, 150, 180, 170, 160, 140, 190, 210]
    
    # Misleading pre-computations
    preliminary = sum(benchmark_data) / len(benchmark_data)
    peak_ratio = max(benchmark_data) / min(benchmark_data)
    
    # Data transformation chain
    metric_set = build_metric_set()
    
    # Decoy function call with no effect
    _ = analyze_trends(benchmark_data[:4])
    
    # Key statement
    final_score = evaluate_performance(metric_set, benchmark_data)
