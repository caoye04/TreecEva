from itertools import combinations

def analyze_sequence(seq):
    # Irrelevant analysis function (dead code path)
    total_pairs = 0
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] + seq[j] == 10:
                total_pairs += 1
    return total_pairs

def validate_timing(timing_log):
    # Distractor function that computes average but isn't used
    avg_time = sum(timing_log) / len(timing_log)
    variance = sum((t - avg_time) ** 2 for t in timing_log) / len(timing_log)
    return avg_time < 50 and variance < 200

def extract_metrics(data_chunk):
    # Slicing and processing
    segment_a = data_chunk[::2]  # Every other element
    segment_b = data_chunk[1::2]
    
    # Intermediate calculations with some irrelevant ones
    raw_sum = sum(segment_a)
    shifted_sum = sum(x * 1.5 for x in segment_b)
    penalty_factor = len([x for x in data_chunk if x > 100]) * 0.5
    
    # Real metric computation
    base_metric = raw_sum + shifted_sum
    adjustment = abs(segment_a[0] - segment_b[-1]) if segment_b else 0
    return base_metric - adjustment - penalty_factor

def calculate_performance(log_entries):
    cumulative = 0
    temp_buffer = []
    
    for entry in log_entries:
        # Simulate string-based data ingestion
        parts = entry.split(',')
        numeric_vals = [int(p.strip()) for p in parts if p.strip().isdigit()]
        
        if len(numeric_vals) < 3:
            continue
            
        # Extract key performance indicators
        peak_load = max(numeric_vals)
        startup_phase = numeric_vals[:3]
        steady_state = numeric_vals[3:]
        
        # Irrelevant min/max tracking
        min_during_startup = min(startup_phase)
        spikes = [v for v in steady_state if v > 90]
        spike_count = len(spikes)
        
        # Core logic: only this contributes to final answer
        score_component = extract_metrics(numeric_vals)
        decay = 0.95 ** spike_count
        cumulative += score_component * decay
        
        # Buffer operation that doesn't affect result
        temp_buffer.append(sum(startup_phase) / len(startup_phase))
    
    # Final transformation
    normalized = cumulative / len(log_entries)
    final_adjustment = sum(1 for tb in temp_buffer if tb > 40)
    final_score = int(normalized - final_adjustment)
    
    # Additional misleading computation
    hypothetical = list(combinations([1, 2, 3, 4], 2))
    dummy_total = sum(a * b for a, b in hypothetical)
    
    return final_score

# Main execution data
benchmark_data = [
    "10,20,30,85,95,105,40",
    "15,25,35,70,92,110,60,45",
    "5,45,55,65,88,102", 
    "20,30,40,50,55"
]

# Execute
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")