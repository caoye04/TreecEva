import math
from functools import reduce

def process_acoustic_bins(frequency_bins):
    processed_values = []
    for idx, bin_val in enumerate(frequency_bins):
        if bin_val <= 0:
            continue
        log_val = math.log(bin_val, 2)
        mod_log = log_val % 3
        exponent = int(mod_log * 2) if mod_log > 1 else int(mod_log + 1)
        transformed = bin_val ** exponent
        processed_values.append(transformed)
    
    if not processed_values:
        return 0
    
    mean_val = sum(processed_values) / len(processed_values)
    squared_diffs = [(x - mean_val) ** 2 for x in processed_values]
    variance = sum(squared_diffs) / len(squared_diffs)
    
    harmonic_sum = sum(1/x for x in processed_values if x != 0)
    harmonic_mean = len(processed_values) / harmonic_sum if harmonic_sum != 0 else 0
    
    final_metric = (variance * harmonic_mean) % 100
    return final_metric

frequency_bins = [2, 8, 16, 32, 64, 128]
final_metric = process_acoustic_bins(frequency_bins)
print(f'Result: {final_metric}')