import math
from collections import defaultdict

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

# Sensor data per zone: {zone_id: [temp_readings]}
sensor_zones = {
    'alpha': [23.5, 25.0, 22.8],
    'beta': [19.2, 21.7, 20.1],
    'gamma': [27.3, 26.9, 28.0],
    'delta': [18.5, 19.0, 18.8]
}

# State machine tracking
state_log = defaultdict(list)
current_state = 'normal'
prime_weights = {}
zone_deviations = []

for zone, temps in sensor_zones.items():
    # Compute geometric mean
    product = 1
    for t in temps:
        product *= t
    geometric_mean = product ** (1 / len(temps))
    
    # Assign prime weight based on zone name length
    name_length = len(zone)
    prime_weights[zone] = 1.0
    if is_prime(name_length):
        prime_weights[zone] = 1.75
    
    # Adjusted metric
    adjusted_metric = geometric_mean * prime_weights[zone]
    
    # Calculate deviation from ideal (25 degrees)
    deviation = abs(adjusted_metric - 25.0)
    zone_deviations.append(round(deviation, 4))
    
    # State transitions
    if deviation > 3.0:
        current_state = 'alert'
    elif deviation > 1.5:
        current_state = 'warning'
    else:
        current_state = 'normal'
    
    state_log[current_state].append(zone)

# Compute stability index using GCD of deviations scaled by log factor
gcd_deviation = gcd_list([int(d * 10000) for d in zone_deviations])
log_factor = math.log10(sum(len(zones) for zones in state_log.values()) + 1)
stability_index = round(gcd_deviation * log_factor, 2)

print(f"Result: {stability_index}")