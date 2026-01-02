from itertools import combinations

# Sensor data simulation and processing for environmental monitoring system
def collect_sensor_data():
    base_values = [23.4, 25.1, 19.5, 24.3, 26.7, 22.0, 20.8, 27.3, 28.1, 18.9]
    adjustments = [0.5, -1.2, 0.8, -0.3, 1.1]
    refined = []
    
    # Apply complex adjustment pattern (only some are used)
    for i in range(len(base_values)):
        temp = base_values[i]
        if i % 3 == 0:
            temp += adjustments[0]
        elif i % 4 == 0:
            temp -= adjustments[2]
        else:
            temp += adjustments[4]  # Only this path matters
        refined.append(round(temp, 2))
    
    # Irrelevant transformation
    reshaped = [[refined[i], refined[i+1]] for i in range(0, len(refined)-1, 2)]
    checksum = sum(int(x*10) for x in refined) % 100  # Distractor
    
    return refined

def filter_anomalies(data):
    # Identify outliers using interquartile range method
    sorted_data = sorted(data)
    q1 = sorted_data[len(sorted_data)//4]
    q3 = sorted_data[3*len(sorted_data)//4]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    filtered = [x for x in data if lower_bound <= x <= upper_bound]
    
    # Red herring: complex set operations with unused result
    pairs = list(combinations(filtered, 2))
    high_variance_pairs = set()
    for a, b in pairs:
        if abs(a - b) > 3.0:
            high_variance_pairs.add((a, b))
    pair_count = len(high_variance_pairs)  # Unused
    
    # Another distraction: bit manipulation on indices
    special_indices = []
    for i, val in enumerate(data):
        if (i ^ 7) & 5 == 3 and val < 25.0:  # Complex but mostly irrelevant
            special_indices.append(i)
    
    return filtered

def rolling_average(series, window=3):
    # Unused function - dead code path
    averages = []
    for i in range(len(series) - window + 1):
        avg = sum(series[i:i+window]) / window
        averages.append(round(avg, 2))
    return averages

def analyze_readings(readings):
    # Core analysis logic
    total = sum(readings)
    count = len(readings)
    
    # Multiple layers of computation
    base_metric = total / count
    
    # Correction factors
    factor_a = 1.0
    if count > 6:
        factor_a = 0.95
    if count < 8:
        factor_a *= 1.02
    
    adjusted_metric = base_metric * factor_a
    
    # Secondary validation check (distractor)
    validation_set = {round(x, 1) for x in readings}
    expected_range = set(round(20 + i*0.5, 1) for i in range(20))
    overlap = len(validation_set.intersection(expected_range))
    
    # Tertiary calculation - looks important but isn't critical
    cumulative = 0
    growth_factors = []
    for i in range(1, len(readings)):
        if readings[i-1] != 0:
            change = (readings[i] - readings[i-1]) / abs(readings[i-1])
            cumulative += change
n            growth_factors.append(change)
    
    final_adjustment = 1.0
    if cumulative > 0.1:
        final_adjustment = 1.05
    elif cumulative < -0.1:
        final_adjustment = 0.95
    
    # The actual answer derivation (non-obvious due to distractions)
    # After filtering, we have 8 elements, mean ~23.76, adjusted by 0.95*1.05
    raw_avg = sum(readings) / len(readings)
    final_diagnostic = int(round(raw_avg * 0.95 * 1.05 * 100))  # Key result
    
    # Final red herring: recursive summation of digit products
    def digit_product_recursive(n, depth=0):
        if depth >= 3 or n < 10:
            return n
        product = 1
        for digit in str(n):
            if digit != '0':
                product *= int(digit)
        return digit_product_recursive(product, depth + 1)
    
    checksum_final = digit_product_recursive(final_diagnostic)  # Unused
    
    return final_diagnostic

# Main execution sequence
collected_data = collect_sensor_data()
temp_diagnostic = sum(collected_data) // len(collected_data)  # Misleading intermediate
filtered_data = filter_anomalies(collected_data)
final_diagnostic = analyze_readings(filtered_data)
print(f"Target result: {final_diagnostic}")