from functools import wraps, reduce
from math import sqrt

def call_tracker(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

def process_signal_block(block_data):
    # Apply normalization and calculate energy
    normalized = [x/max(block_data) if max(block_data) != 0 else 0 for x in block_data]
    energy = sum(x**2 for x in normalized)
    return energy

@call_tracker
def adaptive_filter_coeff(coeff_set):
    # Calculate adaptive coefficient using complex formula
    if not coeff_set:
        return 0
    product = reduce(lambda x, y: x * y, coeff_set, 1)
    return sqrt(abs(product)) if product < 0 else product**(1/3)

def evaluate_filter_performance(signal_blocks):
    metrics = {}
    for i, block in enumerate(signal_blocks):
        if not block or len(block) == 0:
            continue
        energy = process_signal_block(block)
        coeff_adaptation = adaptive_filter_coeff([energy, i+1, len(block)])
        
        # Short-circuit evaluation for performance check
        if energy > 0 and coeff_adaptation >= 0:
            metrics[f'block_{i}'] = {
                'energy': energy,
                'adaptation': coeff_adaptation,
                'performance': energy * coeff_adaptation
            }
        else:
            metrics[f'block_{i}'] = {'energy': 0, 'adaptation': 0, 'performance': 0}
    return metrics

# Main processing
audio_segments = [
    [1, 2, 3, 4, 5],
    [],
    [10, -5, 3],
    [0, 0, 0],
    [2.5, -1.5, 3.5, -2.0]
]

filter_coefficients = [1.2, -0.5, 0.8, 1.0]
adapted_coeff = adaptive_filter_coeff(filter_coefficients)

if adapted_coeff > 0 or len(audio_segments) > 3:
    performance_metrics = evaluate_filter_performance(audio_segments)
    
    # Dictionary comprehension with merging
    enhanced_metrics = {k: {**v, 'enhanced': v['performance'] * adapted_coeff} 
                       for k, v in performance_metrics.items() 
                       if v['energy'] > 0}
    
    # Early return pattern
    if not enhanced_metrics:
        final_metric = 0
    else:
        final_metric = sum(m['enhanced'] for m in enhanced_metrics.values())
else:
    final_metric = -1

print(f"Result: {final_metric}")