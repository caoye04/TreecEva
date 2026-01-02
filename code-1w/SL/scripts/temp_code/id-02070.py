from collections import defaultdict, Counter
import math

# Simulated system performance metrics
def collect_metrics():
    raw_data = [78, 85, 92, 67, 88, 95, 82]
    stats = defaultdict(float)
    stats['sum'] = sum(raw_data)
    stats['count'] = len(raw_data)
    stats['mean'] = stats['sum'] / stats['count']
    
    # Irrelevant computations (distractors)
    temp_offsets = [x - 70 for x in raw_data if x > 70]
    adjustment_factor = math.prod(temp_offsets) % 13
    
    noise_data = [(i * 1.5) + 2 for i in range(len(raw_data))]
    smoothed = [round((raw_data[i] + noise_data[i]) / 2) for i in range(len(raw_data))]
    
    stats['peak'] = max(smoothed)
    stats['adjusted_mean'] = sum(smoothed) / len(smoothed) + adjustment_factor
    
    return stats

def analyze_trends(history):
    trend_scores = []
    for i in range(1, len(history)):
        if history[i] > history[i-1]:
            trend_scores.append(1)
        elif history[i] < history[i-1]:
            trend_scores.append(-1)
        else:
            trend_scores.append(0)
    
    # Dead code path - never used
    def unused_debug_func():
        return sum(trend_scores) * 0.5
    
    direction = sum(trend_scores)
    volatility = Counter(trend_scores).get(1, 0) + Counter(trend_scores).get(-1, 0)
    
    # Misleading intermediate result
    phantom_index = volatility * direction % 7
    
    return {'trend': direction, 'volatility': volatility, 'index': phantom_index}

def validate_integrity(data_points):
    # Bit manipulation red herring
    checksum = 0
    for val in data_points:
        checksum ^= int(val) << 1
        checksum &= 0xFFFF
    
    # Unused logical branch
    if checksum < 1000:
        alt_check = sum([v**2 for v in data_points]) // len(data_points)
    else:
        alt_check = sum([v//2 for v in data_points])
    
    # This function appears important but only returns boolean flag
    return (checksum % 17) == 0

def filter_outliers(values, threshold=2):
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    std_dev = math.sqrt(variance)
    
    # List comprehension with filtering (relevant)
    filtered = [v for v in values if abs(v - mean_val) <= threshold * std_dev]
    
    # Slicing distraction
    window_slice = values[1:-1:2]
    secondary_score = sum(window_slice) // len(window_slice) if window_slice else 0
    
    return filtered

def evaluate_performance(metrics, benchmark):
    base = metrics['mean']
    trend_data = analyze_trends(benchmark)
    trend_influence = trend_data['trend'] * 0.8
    
    # Simulated calibration curve (partially irrelevant)
    calibration_map = {i: (i * 1.05) for i in range(1, 12)}
    calibrated_base = calibration_map.get(int(base), base)
    
    # Key logic step: filtering affects final input size
    cleaned = filter_outliers(benchmark)
    size_factor = len(cleaned) / len(benchmark)
    
    # Critical computation chain
    intermediate = (calibrated_base + trend_influence) * size_factor
    
    # Bitwise operation red herring
    magic_shift = (len(benchmark) << 2) ^ 5
    decoy_adjustment = (magic_shift & 0xFF) / 100
    
    # Final score calculation - only this matters
    final_score = int(intermediate - decoy_adjustment + 0.5)
    
    # Multiple early returns that are never hit (dead paths)
    if final_score > 150:
        return 100
    if final_score < 0:
        return 0
    
    return final_score

# Main execution flow
if __name__ == "__main__":
    # Collect primary metrics
    system_metrics = collect_metrics()
    
    # Benchmark historical data (used in trend analysis)
    benchmark_data = [70, 72, 75, 76, 79, 81, 84, 85]
    
    # Validate data integrity (result not used - distraction)
    is_valid = validate_integrity(benchmark_data)
    
    # Compute final performance score
    final_score = evaluate_performance(system_metrics, benchmark_data)
    
    # Print result as required
    print(f"Result: {final_score}")