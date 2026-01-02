def analyze_flow_patterns(data_sequence):
    # Preprocess: extract directional trends
    trends = [(data_sequence[i+1] - data_sequence[i]) for i in range(len(data_sequence)-1)]
    positive_flow = sum(1 for t in trends if t > 0)
    negative_flow = sum(1 for t in trends if t < 0)
    net_bias = abs(positive_flow - negative_flow)

    # Irrelevant statistical distraction
    mean_trend = sum(trends) / len(trends) if trends else 0
    variance_proxy = sum((t - mean_trend)**2 for t in trends) / len(trends) if trends else 0

    return positive_flow, negative_flow, net_bias


def generate_threshold_profile(base_value, depth=3):
    # Generates nested threshold levels (only top level used later)
    profile = []
    current = base_value
    for i in range(depth):
        current = (current * 1.5 + i) % 17
        profile.append(current)
    
    # Dead code path - never accessed
    if False:
        fallback = [x * 2 for x in profile if x % 2 == 0]
        return fallback

    return profile

# Core simulation parameters
time_series_data = [12, 15, 14, 18, 22, 20, 25, 30, 28, 33]
base_threshold = 7

# Derive auxiliary metrics
pos, neg, bias = analyze_flow_patterns(time_series_data)

# Generate unused alternate configurations
alt_config_a = generate_threshold_profile(base_threshold, 2)
alt_config_b = generate_threshold_profile(base_threshold + 3, 4)

# Construct flow matrix using tuple-based encoding
flow_matrix = []
for i in range(len(time_series_data) - 1):
    delta = time_series_data[i+1] - time_series_data[i]
    category = 'up' if delta > 0 else 'down'
    magnitude = abs(delta)
    flow_matrix.append((i, magnitude, category))

# Define actual thresholds used in calculation
thresholds = generate_threshold_profile(base_threshold, 3)

# Misleading intermediate computation (not used in final result)
dummy_score = sum(abs(x - y) for x, y in zip(alt_config_a, alt_config_b[:len(alt_config_a)]))
dummy_flag = dummy_score > 10

# State tracker with red herring variables
state_log = []
counter_a = 0
counter_b = 0
overflow_flag = False

# Primary equilibrium calculation function
def calculate_equilibrium(matrix, limits):
    score = 0
    adjustment_factor = limits[0] / (limits[1] or 1)
    
    for step, mag, cat in matrix:
        # Apply threshold modulation
        if mag >= limits[1]:
            counter_a += 1  # Tracked but not used
            if cat == 'up':
                score += mag * adjustment_factor
            else:
                score -= mag * 0.8
        elif mag <= limits[2]:
            counter_b += 1  # Also tracked but irrelevant
            score += mag * 0.3
        
        # Log state unnecessarily
        state_log.append((step, round(score, 3), cat))
        
        # Unused overflow detection
        if abs(score) > 100:
            overflow_flag = True  # Never actually affects logic
    
    # Final nonlinear transformation
    final_score = abs(score) ** 0.9 * (1 + (-1) ** int(adjustment_factor))
    return int(round(final_score))

# Execute main computation
equilibrium_score = calculate_equilibrium(flow_matrix, thresholds)

print(f"Result: {equilibrium_score}")