from itertools import accumulate

# Simulate time-series sensor readings with noise filtering
def process_sensor_data(raw_readings):
    baseline = sum(raw_readings) / len(raw_readings)
    filtered = [x for x in raw_readings if abs(x - baseline) < 10]
    
    # Irrelevant transformation: frequency analysis (not used in final result)
    freq_domain = list(map(lambda x: (x - baseline) ** 2, raw_readings))
    avg_power = sum(freq_domain) / len(freq_domain)

    # Relevant processing path
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered) + 1e-8) for x in filtered]
    integrated = list(accumulate(normalized, lambda a, b: a + b * 0.9))
    
    # Dummy recursive smoothing (dead-end)
    def smooth(data, depth=2):
        if depth == 0 or len(data) < 2:
            return data
        smoothed = [data[0]] + [(a + b) / 2 for a, b in zip(data[:-1], data[1:])] + [data[-1]]
        return smooth(smoothed, depth - 1)
    
    smoothed_result = smooth(integrated)  # Computed but unused
    
    # Key state tracking variables
    trend_score = sum(1 for i in range(1, len(integrated)) if integrated[i] > integrated[i-1])
    volatility = max(integrated) - min(integrated)
    
    # Distractor: complex dictionary aggregation (partially irrelevant)
    stats_summary = {
        'count': len(filtered),
        'trend_ratio': trend_score / (len(integrated) - 1) if len(integrated) > 1 else 0,
        'volatility_index': volatility,
        'baseline_shift': avg_power  # Unused in final logic
    }
    
    # Final computation chain
    aggregate = sum(integrated) * stats_summary['trend_ratio']
    scaling_factor = 1 + (stats_summary['volatility_index'] / 5)
    final_flux = aggregate * scaling_factor
    
    return final_flux

# Input data
readings = [12, 15, 14, 10, 18, 22, 19, 25, 21, 17, 16, 13]
result = process_sensor_data(readings)
print(f"Result: {result}")