import math
from itertools import combinations

def process_sonar_data(raw_readings):
    # Tokenize and parse raw readings
    tokens = [float(x) for x in raw_readings.split(',')]
    
    # Apply floating point transformations
    transformed = [math.sqrt(abs(x)) * math.sin(x) for x in tokens]
    
    # Dynamic programming optimization
    n = len(transformed)
    dp = [0.0] * (n + 1)
    
    for i in range(1, n + 1):
        dp[i] = max(dp[i-1], dp[i-1] + transformed[i-1])
    
    return dp[n]

def calculate_signal_strength(readings_batch):
    # Generator expression for memory efficiency
    strengths = (process_sonar_data(reading) for reading in readings_batch)
    
    # Combine using combinatorial logic
    combined_strength = 0.0
    for combo in combinations(strengths, 2):
        combined_strength += combo[0] * combo[1]
    
    return combined_strength

# Main execution
sonar_batches = [
    "1.2,-2.5,3.1,-4.8,5.5",
    "-1.1,2.2,-3.3,4.4,-5.5",
    "0.5,-1.5,2.5,-3.5,4.5"
]

optimized_signal_strength = calculate_signal_strength(sonar_batches)
print(f"Result: {optimized_signal_strength}")