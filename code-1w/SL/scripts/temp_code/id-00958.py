from collections import defaultdict
from itertools import combinations

# Simulate a multi-stage processing pipeline with diagnostic overhead
def analyze_pipeline_performance(base_units, cycle_time, processor_count):
    stage_log = defaultdict(int)
    diagnostics = []
    
    # Initialize primary variables
    total_input = base_units * processor_count
    total_output = 0
    
    # Simulate staged processing with conditional throughput
    for stage in range(1, 4):
        stage_multiplier = 0.9 if stage == 2 else 0.95
        loss_rate = 0.05 if stage == 1 else 0.03
        
        processed_this_stage = int(total_input * stage_multiplier)
        lost_units = int(total_input * loss_rate)
        remaining = total_input - lost_units
        
        # Log stage metrics (some used later)
        stage_log[f'stage_{stage}_processed'] = processed_this_stage
        stage_log[f'stage_{stage}_remaining'] = remaining
        
        total_input = remaining  # Carry forward remaining units
        total_output += processed_this_stage
    
    # Spurious combinatorial analysis (distractor: not used in final result)
    critical_paths = []
    for r in range(2, min(4, processor_count + 1)):
        for combo in combinations(range(processor_count), r):
            path_metric = sum([c**2 + cycle_time for c in combo])
            critical_paths.append(path_metric)
    
    # Diagnostic summary (dead code path - only conditionally executed in real systems)
    if len(critical_paths) > 100:
        avg_path = sum(critical_paths) / len(critical_paths)
        diagnostics.append(avg_path)
    
    # Secondary distraction: simulate thermal throttling check
    thermal_load = processor_count * 7.8
    throttle_adjustment = 0.0
    if thermal_load > 50:
        for _ in range(5):
            throttle_adjustment += 0.01 * thermal_load
    
    # Core calculation: efficiency score
    efficiency_score = total_output / (cycle_time * processor_count)
    
    # Additional irrelevant post-processing
    normalized_score = round(efficiency_score, 2)
    if normalized_score > 100:
        efficiency_score *= 0.9
    
    # Final output
    print(f"Result: {efficiency_score}")
    return efficiency_score

# Execute simulation
result = analyze_pipeline_performance(base_units=850, cycle_time=6, processor_count=8)