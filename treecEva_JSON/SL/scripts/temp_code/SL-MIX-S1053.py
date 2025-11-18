import statistics

def process_waveforms():
    raw_samples = [12, 28, 35, 42, 56, 63, 77, 84]
    
    # Stage 1: Bit-mask filtering
    mask = 0b11110000
    filtered_samples = [x & mask for x in raw_samples]
    
    # Stage 2: String encoding transformation
    encoded_strings = [bin(x)[2:].zfill(8) for x in filtered_samples]
    
    # Stage 3: Pattern matching with lambda
    pattern_matcher = lambda s: sum(1 for i in range(len(s)-1) if s[i] == s[i+1])
    match_counts = list(map(pattern_matcher, encoded_strings))
    
    # Stage 4: Statistical aggregation
    mean_matches = statistics.mean(match_counts)
    variance_matches = statistics.variance(match_counts)
    
    # Stage 5: Final metric computation
    accumulator = 0
    for i in range(len(match_counts)):
        if match_counts[i] > mean_matches:
            accumulator |= (1 << i)
    
    final_metric = accumulator ^ int(variance_matches)
    return final_metric

final_metric = process_waveforms()
print(f"Result: {final_metric}")