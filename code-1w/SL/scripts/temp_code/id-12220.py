import itertools

def analyze_pattern(sequence):
    trend = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend.append(1)
        elif sequence[i] < sequence[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    return trend

def calculate_equilibrium(data, limit):
    # Irrelevant transformation (distractor)
    scaled_data = [x * 1.5 for x in data if x > 0]
    temp_accum = 0
    for val in scaled_data:
        temp_accum += val ** 0.5
    
    # Core logic hidden among distractions
    positive_peaks = [x for x in data if x > limit]
    negative_troughs = [x for x in data if x < -limit]
    peak_sum = sum(positive_peaks) if positive_peaks else 0
    trough_sum = sum(negative_troughs) if negative_troughs else 0
    
    # Misleading intermediate calculation
    dummy_metric = len(scaled_data) * temp_accum / (len(data) or 1)
    adjustment = 0
    for combo in itertools.combinations([abs(x) for x in data if x != 0], 2):
        adjustment += abs(combo[0] - combo[1])
        if adjustment > 1000:  # Early break (semi-relevant but not critical)
            break
    
    # Actual key computation
    net_bias = peak_sum + trough_sum
    symmetry_factor = len(positive_peaks) - len(negative_troughs)
    equilibrium_score = int(net_bias - symmetry_factor * 2.7)  # Final deterministic result
    
    # Dead code branch (distractor)
    if len(data) > 1000:
        fallback = sum(data) / len(data)
        return fallback
        
    return equilibrium_score

# Simulated sensor flow data (realistic context)
data_stream = [3, -5, 8, -2, 12, -11, 7, 4, -6, 9, -8, 10, -12]
threshold = 6

# Preliminary analysis (irrelevant to final answer)
trend_analysis = analyze_pattern(data_stream)
baseline_shift = sum(data_stream) / len(data_stream)

# Key statement containing target variable
equilibrium_score = calculate_equilibrium(data_stream, threshold)

print(f"Result: {equilibrium_score}")