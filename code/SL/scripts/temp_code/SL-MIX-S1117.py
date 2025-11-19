def call_tracker(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

def compute_filter_coefficients(taps):
    dp = [0] * (taps + 1)
    dp[0] = 1
    dp[1] = 2
    for i in range(2, taps + 1):
        dp[i] = dp[i-1] + dp[i-2] + (i & (i-1))  # Bitwise operation
    return dp[taps]

@call_tracker
def process_frequency_band(band_id, coefficients):
    if band_id % 2 == 0:
        return coefficients * 2
    else:
        return coefficients + 5

filter_taps = 8
base_coefficient = compute_filter_coefficients(filter_taps)
frequency_bands = [3, 7, 2, 9, 4]
processed_signals = []

for idx, band in enumerate(frequency_bands):
    adjusted_band = band + (idx & 1)  # Bitwise operation
    if adjusted_band > 5:
        coeff_modifier = process_frequency_band(idx, base_coefficient)
        processed_signals.append(coeff_modifier)
    else:
        processed_signals.append(base_coefficient // 2)

optimized_gain = sum(processed_signals) - (process_frequency_band.call_count << 2)  # Left shift
print(f"Result: {optimized_gain}")