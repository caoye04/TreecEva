import functools

def signal_band_optimizer(frequency_bands):
    # Dynamic programming table for optimal bit allocation
    dp_table = [0] * (len(frequency_bands) + 1)
    
    for i in range(1, len(frequency_bands) + 1):
        current_band_energy = frequency_bands[i-1]
        # Bit allocation strategy using arithmetic and bitwise operations
        optimal_bits = (current_band_energy << 2) - (current_band_energy >> 1)
        dp_table[i] = max(dp_table[i-1], dp_table[i-1] + optimal_bits)
    
    return dp_table[len(frequency_bands)]

# Audio signal characteristics for analysis
audio_spectrum = [15, 23, 9, 31, 17, 28, 12, 35]

# Apply functional transformation to spectrum data
transformed_spectrum = list(map(lambda x: x * 3 if x % 2 == 0 else x * 2, audio_spectrum))

# Calculate base efficiency using dynamic programming
base_efficiency = signal_band_optimizer(transformed_spectrum)

# Apply decorator-based enhancement factor
def enhancement_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        # Enhancement calculation using arithmetic operations
        enhancement_factor = (original_result & 0xFF) ^ 0x55
        return original_result + enhancement_factor
    return wrapper

@enhancement_decorator
def calculate_refined_efficiency(base_value):
    # Refinement using bit manipulation and arithmetic
    refined = (base_value | 0xF0) - (base_value & 0x0F)
    return refined

# Compute final efficiency score
refined_efficiency = calculate_refined_efficiency(base_efficiency)
final_efficiency_score = refined_efficiency - sum(filter(lambda x: x > 50, transformed_spectrum))

print(f"Result: {final_efficiency_score}")