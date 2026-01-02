import itertools

def analyze_pattern(sequence):
    trend = 0
    volatility = 0
    for i in range(1, len(sequence)):
        diff = sequence[i] - sequence[i-1]
        if diff > 0:
            trend += 1
        elif diff < 0:
            trend -= 1
        volatility += abs(diff)
    
    # Distractor: unused computation
    normalized_vol = volatility / len(sequence) if sequence else 0
    return trend, volatility

def simulate_stability(readings):
    convergence = 0
    overshoots = 0
    baseline = sum(readings) / len(readings)
    
    for val in readings:
        if abs(val - baseline) < 0.5:
            convergence += 1
        if val > baseline + 2.0:
            overshoots += 1
        # Semi-relevant: tracking but not critical
        adjustment = (baseline - val) * 0.1
    
    # Distractor: dead code path
    if overshoots > 100:
        convergence = max(convergence - overshoots, 0)
        
    return convergence

def calculate_rating(convergence, stability):
    # Core logic
    rating = convergence * 3
    if stability > 5:
        rating += 10
    else:
        rating += 5
    
    # Distractor: irrelevant transformation
    temp_factors = [rating / (i+1) for i in range(1, 4)]
    aggregated = sum(temp_factors)
    
    return int(rating)

# Main execution
sensor_data = [1.2, 1.5, 1.3, 1.4, 1.6, 1.3, 1.2, 1.5, 1.7, 1.6]

# Extract subsequences using itertools
subsequences = list(itertools.combinations(sensor_data, 4))
total_trend = 0
for seq in subsequences[:10]:  # Limit to first 10 for determinism
    trend, _ = analyze_pattern(list(seq))
    total_trend += trend

# State tracking with distractor variables
system_state = 'active'
event_count = len(subsequences)
activation_threshold = 8.5 if system_state == 'active' else 12.0

# Key variable derivation
convergence = simulate_stability(sensor_data)
stability = abs(total_trend) % 7

# Critical statement
final_score = calculate_rating(convergence, stability)

# Irrelevant aggregation
weighted_avg = sum([final_score / (i+1) for i in range(5)])

# Print result as required
print(f"Target result: {final_score}")