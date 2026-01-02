def analyze_growth_patterns(data):
    # Irrelevant transformation (distractor)
    normalized = [round(x * 0.98 + 2.1, 2) for x in data]
    adjusted = [max(0, x - 1) for x in normalized]

    # Real computation begins: identify high-growth segments
    segments = [(i, i+3) for i in range(len(data)-2) if data[i] < data[i+1] > data[i+2]]
    
    # Extract peak values from each segment
    peaks = [data[start+1] for start, end in segments]

    # Compute moving average as red herring
    window_size = 2
    moving_averages = [sum(data[i:i+window_size]) / window_size 
                        for i in range(len(data) - window_size + 1)]

    # Actual relevant logic: count how many peaks exceed global median
    median_val = sorted(data)[len(data)//2]
    significant_peaks = [p for p in peaks if p > median_val]
    
    return len(significant_peaks), moving_averages  # second return is unused

# Simulate soil nutrient levels (real input)
soil_nutrients = [34, 56, 23, 67, 89, 45, 78, 91, 33, 65, 29]

# Distractor: temperature fluctuations (not used in final result)
temp_readings = [22.1, 23.4, 21.8, 24.5, 25.0, 23.9, 24.2, 26.1, 25.3, 27.0, 26.8]
adjusted_temps = list(map(lambda t: (t - 32) * 5/9, [t*9/5+32 for t in temp_readings]))

# Identify cluster quality based on nutrient thresholds
cluster_scores = []
for i, nut in enumerate(soil_nutrients):
    score = 0
    if nut > 40:
        score += 2
    if i > 0 and soil_nutrients[i-1] > 30:
        score += 1
    if i < len(soil_nutrients) - 1 and soil_nutrients[i+1] > 50:
        score += 1
    cluster_scores.append(score)

# Another distractor: string-based status codes (never used)
status_labels = ['L', 'M', 'H']
status_map = {0: 'LOW', 1: 'MED', 2: 'HIGH'}
health_status = [status_map.get(min(2, cs), 'UNKNOWN') for cs in cluster_scores]
status_summary = ''.join([s[0] for s in health_status]).lower()

# Core function that determines final yield
def calculate_harvest_efficiency(scores, limit):
    # Filter clusters above threshold
    valid_clusters = [s for s in scores if s >= limit]
    
    # Compute efficiency using tuple unpacking
    contributions = []
    for idx, val in enumerate(valid_clusters):
        multiplier = 1.5 if idx % 2 == 0 else 0.8
        contributions.append((idx, val * multiplier))
    
    # Use lambda to filter effective contributions
    is_effective = lambda x: x[1] > 3.0
    effective = list(filter(is_effective, contributions))
    
    # Final aggregation
    total_contribution = sum(val for _, val in effective)
    base_count = len(valid_clusters)
    
    # Actual answer depends only on this formula
    efficiency_score = int(total_contribution - base_count * 1.2)
    return efficiency_score

# Misleading intermediate calculation (dead path)
shadow_calc = sum([n**0.5 for n in soil_nutrients if n % 2 == 1]) / len(soil_nutrients)

threshold = 2
final_yield = calculate_harvest_efficiency(cluster_scores, threshold)

# Critical print statement
print(f"Result: {final_yield}")