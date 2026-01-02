def analyze_growth_patterns(data, base_factor):
    growth_rates = []
    temp_offset = 0.0
    for i, (temp, moisture) in enumerate(zip(data['temperatures'], data['moisture_levels'])):
        rate = (temp - 20) * 0.5 + (moisture - 50) * 0.3
        if temp > 30:
            rate *= 0.8  # Heat stress penalty
        if moisture < 40:
            rate *= 0.7  # Drought effect
        growth_rates.append(max(rate, 0))
    
    # Irrelevant smoothing pass (distractor)
    smoothed = [growth_rates[0]]
    for i in range(1, len(growth_rates)):
        smoothed.append((smoothed[i-1] + growth_rates[i]) / 2)
    
    return growth_rates


def calculate_cluster_weight(indices, weights):
    total = 0
    for idx in indices:
        if idx < len(weights):
            total += weights[idx] ** 0.5
    return total if total > 0 else 1e-8


def calculate_harvest_efficiency(clusters, threshold):
    efficiency = 0.0
    penalty_adjustment = 0.95
    boost_counter = 0
    
    for i, cluster in enumerate(clusters):
        size = cluster['size']
        health = cluster['health_index']
        elevation = cluster['elevation']
        
        # Primary yield calculation
        base_yield = size * health * 0.1
        
        # Elevation adjustment (only above threshold)
        if elevation > threshold:
            base_yield *= 1.1
        else:
            base_yield *= 0.9
        
        # Boost logic based on neighboring clusters (simulated via index)
        if i > 0 and clusters[i-1]['health_index'] > health:
            boost_counter += 1
            base_yield *= 1.05
        
        efficiency += base_yield
    
    # Dead code: unused transformation (distractor)
    transformed_efficiency = efficiency * 0.99 + 1.5
    normalized = efficiency / (len(clusters) or 1)
    
    # Final adjustment using irrelevant combinatorics (distractor)
    combo_factor = 1.0
    for i in range(1, min(len(clusters), 4)):
        combo_factor *= (i / (efficiency + 1))
    
    final_efficiency = efficiency - (boost_counter * 0.5 * combo_factor)
    
    return round(final_efficiency, 4)

# Main execution
sensor_data = {
    'temperatures': [25, 32, 28, 35, 22],
    'moisture_levels': [55, 38, 60, 33, 50]
}

base_config = 1.25

# Call analysis (produces intermediate result)
growth_results = analyze_growth_patterns(sensor_data, base_config)

# Construct cluster dataset
cluster_data = [
    {'size': 120, 'health_index': 0.85, 'elevation': 150},
    {'size': 95, 'health_index': 0.92, 'elevation': 180},
    {'size': 130, 'health_index': 0.78, 'elevation': 140},
    {'size': 110, 'health_index': 0.88, 'elevation': 190}
]

threshold = 160

# Key statement
final_yield = calculate_harvest_efficiency(cluster_data, threshold)

print(f"Result: {final_yield}")