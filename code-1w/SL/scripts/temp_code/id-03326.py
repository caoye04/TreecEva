import itertools

# Simulated sensor data and performance metrics
def collect_metrics():
    raw_readings = [0.85, 0.92, 0.78, 0.96, 0.88, 0.73, 0.91, 0.87]
    weights = [0.1, 0.2, 0.1, 0.3, 0.05, 0.05, 0.1, 0.1]
    weighted_sum = sum(r * w for r, w in zip(raw_readings, weights))
    
    # Irrelevant transformation (distractor)
    transformed = [x ** 0.5 for x in raw_readings[::2]]
    avg_transformed = sum(transformed) / len(transformed)

    # Real metric computation path
    high_performers = [r for r in raw_readings if r > 0.85]
    stability = max(raw_readings) - min(raw_readings)
    consistency_bonus = 1.0 if stability < 0.2 else 0.5

    return {
        'base': weighted_sum,
        'count': len(high_performers),
        'bonus': consistency_bonus,
        'outlier': raw_readings[-1] * 2  # misleading intermediate
    }

# Legacy system compatibility layer (mostly dead code)
def legacy_adjust(data):
    if len(data) > 10:
        return [x * 0.95 for x in data]
    else:
        return data  # never actually used

# Baseline calibration with slicing distraction
def calibrate_baseline(metrics):
    sequence = list(itertools.accumulate([1, -1, 2, -2, 3, -3]))
    pivot = sequence[3]  # irrelevant
    
    # Actual baseline logic
    base_val = metrics['base']
    adjustment = 0.1 * metrics['count']
    
    # Distracting string operation
    status_flag = 'CALIBRATED'
    parts = status_flag.lower().split('a')
    token = ''.join([p[0] if p else 'x' for p in parts])
    
    return base_val + adjustment

# Main evaluation logic
def evaluate_performance(data, ref):
    # Complex unpacking and conditional logic
    keys = ['base', 'count', 'bonus', 'outlier']
    b, c, bonus_multiplier, _ = [data[k] for k in keys]
    
    # Multi-step calculation with nested conditions
    if c >= 3:
        initial_score = b * 100 + c * 5
        if bonus_multiplier > 0.7:
            initial_score *= 1.2
            # Additional distraction: enumerate usage
            indices = []
            for i, val in enumerate([b, c]):
                if val > 0.5:
                    indices.append(i * 2)
        else:
            initial_score *= 1.05
    else:
        initial_score = b * 80
    
    # Decoy branch (never reached due to data)
    if b < 0.5:
        initial_score = 0
    
    # Final integration with slicing distraction
    history_log = [b * 100, c, bonus_multiplier * 10]
    recent = history_log[-2:]  # unused
    
    # Critical statement
    final_score = int(initial_score + (ref * 2))
    
    # Unused complex structure
    summary = {
        'metrics': {k: data[k] for k in keys},
        'trace': [(i, x*2) for i, x in enumerate(history_log)]
    }
    
    return final_score

# Execution flow
if __name__ == '__main__':
    metric_data = collect_metrics()
    baseline = calibrate_baseline(metric_data)
    final_score = evaluate_performance(metric_data, baseline)
    print(f"Result: {final_score}")