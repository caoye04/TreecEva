import math

def analyze_signal(pattern, threshold=0.75):
    magnitude = sum(p ** 2 for p in pattern)
    normalized = [p / math.sqrt(magnitude) for p in pattern]
    energy = sum(math.sin(x * math.pi / 4) ** 2 for x in normalized)
    return energy > threshold


def transform_coordinates(coords):
    x, y, z = coords
    rotated_x = x * math.cos(math.pi / 3) - y * math.sin(math.pi / 3)
    rotated_y = x * math.sin(math.pi / 3) + y * math.cos(math.pi / 3)
    transformed = (rotated_x, rotated_y, z ** 2)
    return transformed


def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = -sum((count / total) * math.log2(count / total) for count in counts.values())
    return entropy

# Irrelevant helper function (dead code path)
def deprecated_calc(v):
    return (v << 3) ^ 0xAFFE

# Unused constant (distractor)
MAX_BUFFER_SIZE = 1024 * 1024

# Simulated sensor data (real and decoy)
sensor_readings = {
    'primary': [0.1, 0.4, 0.9, 0.2],
    'secondary': [1.0, 0.5, 0.3, 0.8],
    'tertiary': [0.7, 0.6, 0.2, 0.9]
}

# Misleading intermediate metrics (red herring)
avg_primary = sum(sensor_readings['primary']) / len(sensor_readings['primary'])
temporal_weight = avg_primary * 1.618
offset_correction = math.floor(temporal_weight * 100) % 7

# Real processing begins
metric_data = {
    'amplitude': sum(sensor_readings['secondary']),
    'stability': len([x for x in sensor_readings['primary'] if x > 0.3]),
    'complexity': compute_entropy([int(x * 10) for x in sensor_readings['tertiary']])
}

# Configuration with distractor keys
user_config = {
    'threshold': 0.85,
    'debug_mode': True,
    'log_level': 'VERBOSE',
    'precision_boost': False,
    'legacy_compat': 'disabled'
}

# Decoy data structure (unused)
system_state = {
    'uptime': 1274,
    'load_avg': (0.45, 0.67, 0.89),
    'cache_hit_rate': 0.92
}

# Coordinate transformation (partially relevant)
raw_coords = (2.0, 1.5, 1.1)
processed_coords = transform_coordinates(raw_coords)
spatial_factor = processed_coords[2]  # Only this component used later

# Conditional expression with side-effect-free computation
adjustment = 1.5 if metric_data['stability'] >= 3 else 0.75

# Bit manipulation decoy (no impact on result)
status_flag = 0x1234
debug_mask = 0xFF
masked_status = status_flag & debug_mask  # Dead end

# Core logic hidden among distractions
def evaluate_performance(metrics, config):
    base_score = metrics['amplitude'] * 10
    stability_bonus = metrics['stability'] * 5
    complexity_penalty = int(metrics['complexity'] * 2)
    
    # Key conditional branch affecting final result
    if config['threshold'] > 0.8:
        threshold_factor = 1.2
    else:
        threshold_factor = 0.85
    
    # Combine with spatial factor from coordinate transform
    raw_score = (base_score + stability_bonus - complexity_penalty) * threshold_factor
    final_adjustment = adjustment * spatial_factor
    
    # Final computation
    result = int(raw_score + final_adjustment)
    
    # Early return red herring (never reached)
    if config.get('precision_boost'):
        return result * 2  # This path is not taken
        
    return result

# Critical execution point
final_score = evaluate_performance(metric_data, user_config)

# Print result as required
print(f"Target result: {final_score}")