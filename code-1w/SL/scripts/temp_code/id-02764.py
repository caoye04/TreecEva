def analyze_growth_patterns(data_log):
    total_entries = len(data_log)
    temp_accumulator = 0
    growth_stages = []

    for entry in data_log:
        if 'phase' in entry and entry['phase'] == 'mature':
            temp_accumulator += entry.get('biomass', 0)
            growth_stages.append(entry['height'])

    avg_height = sum(growth_stages) / len(growth_stages) if growth_stages else 0
    return temp_accumulator, avg_height


def filter_noisy_readings(raw_readings):
    # Irrelevant filtering (distractor)
    cleaned = [r for r in raw_readings if r > 0.1]
    outlier_count = len(raw_readings) - len(cleaned)
    return cleaned  # Not used later


def extract_sensor_ids(logs):
    # Dead code path — never called
    ids = set()
    for log in logs:
        ids.add(log['sensor_id'])
    return sorted(ids)


def calculate_harvest_efficiency(scores, thresh):
    weighted_sum = 0
    adjustment_factor = 1.25
    decay_rate = 0.95
    peak_value = max(scores) if scores else 0

    for i, score in enumerate(scores):
        if score < thresh:
            continue
        # Apply decay based on position (simulates diminishing returns)
        decayed_score = score * (decay_rate ** i)
        weighted_sum += decayed_score * adjustment_factor

    # Additional logic with slicing and string-based tagging
    tag_base = "YLD"
    extension = "_T{thresh}".format(thresh=thresh)
    full_tag = tag_base + extension
    tag_length = len(full_tag)

    # Use of slicing: take middle part of sorted scores
    sorted_scores = sorted(scores)
    mid_section = sorted_scores[1:-1]  # Exclude min and max
    mid_avg = sum(mid_section) / len(mid_section) if mid_section else 0

    # Final computation combines multiple concepts
    efficiency = weighted_sum + mid_avg * 0.75
    efficiency -= tag_length * 0.1  # Minor penalty

    return int(efficiency)  # Deterministic integer result


# Simulated agricultural sensor data (real input)
data_log = [
    {'phase': 'germination', 'biomass': 2, 'height': 5},
    {'phase': 'growth', 'biomass': 8, 'height': 15},
    {'phase': 'mature', 'biomass': 15, 'height': 30},
    {'phase': 'mature', 'biomass': 18, 'height': 35},
    {'phase': 'mature', 'biomass': 14, 'height': 28},
    {'phase': 'senescence', 'biomass': 10, 'height': 20}
]

raw_readings = [0.05, 0.12, 0.3, 0.08, 0.5]
sensor_clusters = ['C1', 'C2', 'C3', 'C2', 'C1']

# Extract meaningful biomass and height metrics
total_biomass, average_height = analyze_growth_patterns(data_log)

# Derive cluster-specific scores using height-derived weights
cluster_scores = []
for record in data_log:
    if record['phase'] == 'mature':
        score = record['height'] * 1.5 + record['biomass'] * 0.8
        cluster_scores.append(int(score))

# Misleading intermediate calculations (distractors)
baseline_projection = average_height * 0.6
projected_yield = baseline_projection * total_biomass / 2
scaling_constant = 2.718  # Unused

threshold = 40
final_yield = calculate_harvest_efficiency(cluster_scores, threshold)

# Print final result
print(f"Result: {final_yield}")