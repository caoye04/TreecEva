import math

def signal_processing_pipeline():
    # Frequency bins with initial amplitude values
    freq_bins = {f'bin_{i}': i*2.5 for i in range(1, 9)}
    
    # Apply logarithmic scaling to each bin
    log_scaled = {k: math.log(v) if v > 0 else 0 for k, v in freq_bins.items()}
    
    # Exponentially adjust high-frequency components
    exp_adjusted = {k: v * math.exp(0.1) if 'bin_' in k and int(k.split('_')[1]) > 4 else v 
                   for k, v in log_scaled.items()}
    
    # Bitwise masking operation using lambda for odd-positioned bins
    mask_operation = lambda x, mask: int(x) & mask
    masked_values = {k: mask_operation(v, 0xF) for k, v in exp_adjusted.items()}
    
    # Calculate weighted sum with floating point precision
    weights = [math.sqrt(i) for i in range(1, len(masked_values)+1)]
    weighted_products = [v * w for v, w in zip(masked_values.values(), weights)]
    
    # Final accumulation with precision rounding
    final_amplitude_sum = round(sum(weighted_products), 4)
    
    return final_amplitude_sum

# Execute the pipeline
final_amplitude_sum = signal_processing_pipeline()
print(f'Result: {final_amplitude_sum}')