from collections import defaultdict, Counter

# Simulate agricultural yield analysis across soil clusters
def analyze_soil_composition(data_points):
    ph_levels = defaultdict(int)
    nutrient_score = 0
    trace_elements = [0.1, 0.4, 0.2, 0.6, 0.3]
    dummy_accumulator = 0

    for i, (soil_id, ph) in enumerate(data_points):
        ph_levels[soil_id] += ph
        if i % 2 == 0:
            nutrient_score += int(ph * 10) % 3
        else:
            dummy_accumulator += trace_elements[i % 5] ** 2

    # Irrelevant transformation
    normalized = {k: round(v / 7.0, 2) for k, v in ph_levels.items()}
    return ph_levels, nutrient_score

def compute_microbe_density(area):
    density = 0
    for i in range(1, area // 10 + 1):
        if area % i == 0:
            density += i * 2
    return density if density > 50 else 50

def calculate_harvest_efficiency(scores, limit):
    efficiency = 0
    penalty = 0
    temp_log = []

    for idx, score in enumerate(scores):
        adj_index = idx + 1
        if adj_index > limit:
            penalty += 2
        elif score < 5:
            continue
        else:
            efficiency += score * adj_index
            temp_log.append(efficiency)

    # Red herring computation with zip and conditional expression
    status_flags = ['high' if s > 7 else 'low' for s in scores]
    paired = list(zip(scores, status_flags))
    bonus = sum(s**0.5 for s, f in paired if f == 'high') if len(paired) > 3 else 0

    final = efficiency - penalty + int(bonus)
    return final

# Main execution
if __name__ == '__main__':
    raw_data = [
        ('A', 6.2), ('B', 6.8), ('C', 5.9), 
        ('D', 7.1), ('E', 6.4), ('F', 5.5)
    ]
    
    # Step 1: Analyze soil composition
    soil_map, base_score = analyze_soil_composition(raw_data)
    
    # Step 2: Compute microbe density for control zone
    control_area = 120
    microbe_count = compute_microbe_density(control_area)
    
    # Step 3: Generate cluster scores using multiple factors
    cluster_ids = ['A', 'B', 'C', 'D', 'E', 'F']
    base_values = [6, 7, 5, 8, 6, 5]
    adjustment = [0.2, -0.1, 0.4, 0.3, -0.2, 0.5]
    
    cluster_scores = []
    debug_info = {}
    for i, cid in enumerate(cluster_ids):
        raw_val = base_values[i]
        adj_val = adjustment[i]
        final_val = raw_val + adj_val
        cluster_scores.append(int(final_val))
        debug_info[cid] = final_val
    
    # Introduce distractor: counting pattern that isn't used
    score_counter = Counter(cluster_scores)
    rare_scores = [k for k, v in score_counter.items() if v == 1]
    
    # Key threshold logic
    threshold = base_score + 2  # base_score from soil analysis
    
    # Critical statement
    final_yield = calculate_harvest_efficiency(cluster_scores, threshold)
    
    # Print result as required
    print(f"Result: {final_yield}")