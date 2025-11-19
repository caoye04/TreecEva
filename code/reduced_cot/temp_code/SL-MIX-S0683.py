import math
from collections import defaultdict

# Signal frequency data from deep space observations (in MHz)
space_signals = [1420.405, 2840.810, 4261.215, 5681.620, 7102.025]

# Initialize harmonic tracking
harmonic_map = defaultdict(int)

# Process each signal to determine harmonic relationships
for freq in space_signals:
    # Round to nearest integer for harmonic analysis
    base_freq = round(freq)
    
    # Count occurrences of each base frequency
    harmonic_map[base_freq] += 1
    
    # Check for prime factor relationships
    factors = []
    temp = base_freq
    d = 2
    while d * d <= temp:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
    if temp > 1:
        factors.append(temp)
    
    # For each prime factor, increment its harmonic count
    for p in set(factors):
        harmonic_map[p] += 1

# Calculate signal clarity index
clarity_components = []

for freq_key, count in harmonic_map.items():
    if count > 1:  # Only consider frequencies with harmonic relationships
        # Compute log-weighted harmonic strength
        log_strength = math.log(freq_key) * count
        
        # Apply exponential decay based on frequency magnitude
        decay_factor = math.exp(-freq_key / 10000)
        
        # Calculate component contribution
        component = log_strength * decay_factor
        clarity_components.append(component)

# Compute statistical metrics
if len(clarity_components) > 1:
    mean_clarity = sum(clarity_components) / len(clarity_components)
    variance = sum((x - mean_clarity) ** 2 for x in clarity_components) / len(clarity_components)
else:
    mean_clarity = sum(clarity_components) if clarity_components else 0
    variance = 0

# Final clarity index combines mean and variance with number theory adjustment
# Find GCD of all harmonic counts greater than 1
gcd_value = 0
harmonic_counts = [count for count in harmonic_map.values() if count > 1]
if len(harmonic_counts) > 1:
    gcd_value = harmonic_counts[0]
    for i in range(1, len(harmonic_counts)):
        while harmonic_counts[i]:
            gcd_value, harmonic_counts[i] = harmonic_counts[i], gcd_value % harmonic_counts[i]

# Calculate final clarity index
clarity_index = round((mean_clarity + math.sqrt(variance)) * math.log(gcd_value + math.e))

print(f"Result: {clarity_index}")