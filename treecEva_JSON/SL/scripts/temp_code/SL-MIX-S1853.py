import math
import re
from collections import defaultdict
from statistics import variance

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd_list(lst):
    result = lst[0]
    for i in range(1, len(lst)):
        result = math.gcd(result, lst[i])
        if result == 1:
            break
    return result

# Sensor readings from 10 different sources
raw_sensor_data = [
    "sensor_a:12.4",
    "sensor_b:7.8",
    "sensor_c:23.1",
    "sensor_d:19.5",
    "sensor_e:11.2",
    "sensor_f:31.7",
    "sensor_g:13.9",
    "sensor_h:17.3",
    "sensor_i:29.8",
    "sensor_j:5.6"
]

# Parse sensor data into a dictionary mapping sensor name to reading
parsed_readings = {}
for entry in raw_sensor_data:
    match = re.match(r"(\w+):(\d+\.\d+)", entry)
    if match:
        sensor_name, reading = match.groups()
        parsed_readings[sensor_name] = float(reading)

# Extract just the numeric readings in order
readings_list = [parsed_readings[key] for key in sorted(parsed_readings.keys())]

# Identify prime indices (0-based) where we'll focus our analysis
prime_indices = [i for i in range(len(readings_list)) if is_prime(i)]

# Extract readings at prime indices
prime_readings = [readings_list[i] for i in prime_indices]

# Calculate variance of prime-indexed readings, or 1 if only one value
variance_of_primes = variance(prime_readings) if len(prime_readings) > 1 else 1.0

# Create weights based on string hash of sensor names at prime indices
sensor_names_at_primes = [list(sorted(parsed_readings.keys()))[i] for i in prime_indices]
weights = [hash(name) % 100 + 1 for name in sensor_names_at_primes]

# Compute weighted sum of prime readings
weighted_sum = sum(r * w for r, w in zip(prime_readings, weights))

# Calculate GCD of the weights
common_weight_factor = gcd_list(weights)

# Final coherence score calculation using ternary operator for thresholding
# and short-circuit evaluation for safety check
valid_variance = variance_of_primes > 0.1 and common_weight_factor > 0
final_coherence_score = (
    round((weighted_sum / common_weight_factor) / variance_of_primes, 2)
    if valid_variance
    else -1.0
)

print(f"Result: {final_coherence_score}")