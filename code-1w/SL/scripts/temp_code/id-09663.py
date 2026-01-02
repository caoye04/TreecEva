import itertools

# Simulate water quality analysis with red herrings and complex logic

def analyze_purity(elements):
    # Irrelevant function - dead code path
    return sum([e ** 0.5 for e in elements if e > 10])

def compute_buffer_capacity(ph_levels):
    # Distractor function - looks important but unused in final result
    capacity = 0
    for p in ph_levels:
        if p < 7:
            capacity += (7 - p) * 10
        elif p > 7:
            capacity += (p - 7) * 8
    return capacity

def detect_heavy_metals(trace_levels):
    # Decoy logic with misleading intermediate values
    thresholds = {'lead': 0.015, 'mercury': 0.002, 'arsenic': 0.01}
    violations = []
    for metal, level in trace_levels.items():
        if level > thresholds.get(metal, 0.1):
            violations.append(level * 1000)
    return sum(violations) if violations else 0.0

def process_contaminants(samples, target_ph):
    # Core logic embedded within distractions
    base_score = 100
    ph_penalty = 0
    contaminant_burden = 0
    
    # Real processing begins
    for sample in samples:
        temperature = sample.get('temp_c', 25)
        ph = sample.get('ph', 7.0)
        turbidity = sample.get('turbidity_ntu', 5)
        metals = sample.get('metals', {})
        
        # Meaningful calculation: deviation from optimal pH
        ph_deviation = abs(ph - target_ph)
        if ph_deviation > 1:
            ph_penalty += int(ph_deviation * 10)
        
        # Real contaminant impact
        if turbidity > 10:
            contaminant_burden += turbidity // 2
        
        # Red herring: heavy metal check that doesn't affect final score
        _ = detect_heavy_metals(metals)
    
    # Distractor: unused transformation using itertools
    all_ph_values = [s.get('ph', 7.0) for s in samples]
    grouped_ph = [list(group) for key, group in itertools.groupby(sorted(all_ph_values), key=lambda x: int(x))]
    complexity_factor = len(grouped_ph) * 3 if len(grouped_ph) > 1 else 0  # Not used

    # Real scoring logic
    adjustment = 0
    if len(samples) >= 3:
        sorted_turbidity = sorted([s.get('turbidity_ntu', 0) for s in samples])
        median_turbidity = sorted_turbidity[len(sorted_turbidity)//2]
        if median_turbidity > 8:
            adjustment -= 15
    
    # Final computation
    filtration_score = base_score - ph_penalty - contaminant_burden + adjustment
    
    # Irrelevant string processing distraction
    status_msg = "Water quality: {}".format("acceptable" if filtration_score >= 70 else "poor")
    char_sum = sum(ord(c) for c in status_msg if c.isalpha()) % 100  # Dead end
    
    return filtration_score

# Main execution block
if __name__ == "__main__":
    # Input data with meaningful and irrelevant fields
    water_samples = [
        {
            'site': 'A',
            'temp_c': 22,
            'ph': 6.8,
            'turbidity_ntu': 12,
            'metals': {'lead': 0.008, 'mercury': 0.001},
            'oxygen_pct': 88
        },
        {
            'site': 'B',
            'temp_c': 24,
            'ph': 8.2,
            'turbidity_ntu': 15,
            'metals': {'lead': 0.012, 'arsenic': 0.005},
            'oxygen_pct': 85
        },
        {
            'site': 'C',
            'temp_c': 26,
            'ph': 6.5,
            'turbidity_ntu': 6,
            'metals': {'lead': 0.006, 'mercury': 0.0005},
            'oxygen_pct': 90
        }
    ]
    
    treatment_ph = 7.0
    
    # Call the main processing function
    filtration_score = process_contaminants(water_samples, treatment_ph)
    
    # Print final result as required
    print(f"Result: {filtration_score}")