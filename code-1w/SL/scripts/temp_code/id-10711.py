from collections import defaultdict, Counter

# Simulated bio-signal processing pipeline with decoy components
def analyze_waveform(signal_data):
    if not signal_data:
        return 0
    
    # Irrelevant preprocessing (distraction)
    normalized = [x / max(signal_data) for x in signal_data]
    filtered = [x for x in normalized if x > 0.1]
    stats = defaultdict(float)
    for val in filtered:
        if val > 0.5:
            stats['high'] += 1
        else:
            stats['low'] += 1

    # Red herring computation
    entropy = 0.0
    for k in stats:
        p = stats[k] / len(filtered) if filtered else 0
        if p > 0:
            entropy -= p * __import__('math').log2(p)

    # Actual relevant logic (obscured)
    peak_count = sum(1 for i in range(1, len(signal_data)-1) 
                     if signal_data[i] > signal_data[i-1] and signal_data[i] > signal_data[i+1])
    return peak_count

# Decoy function – looks important but unused in final path
def compute_coherence(signal_a, signal_b):
    coherence_score = 0
    for i in range(min(len(signal_a), len(signal_b))):
        if signal_a[i] > 0 and signal_b[i] > 0:
            coherence_score += 1
    adjustment = __import__('random').random()  # Unused
    return coherence_score % 7

# Core diagnostic engine
def generate_baseline(length):
    # Distractor: generates data but only one value used
    base = [0] * length
    for i in range(length):
        if i % 3 == 0:
            base[i] = (i * 1.5) // 1
        elif i % 5 == 0:
            base[i] = (i ** 0.5) // 1
        else:
            base[i] = i // 2
    return int(base[7])  # Only index 7 matters

def evaluate_risk_level(biomarkers):
    # Complex-looking but partially dead logic
    risk = 0
    marker_count = Counter(biomarkers)
    
    for marker, count in marker_count.items():
        if marker > 100:
            risk += 2 * count
        elif marker > 50:
            risk += count
            # Dead branch (never reached due to prior conditions)
            if count > 10:  # Impossible in input
                risk -= 1

    # Only this line matters
    return risk + 13

# Main processing chain
def process_metrics(signature, thresholds):
    # Multi-step reasoning with distractions
    temp_results = []
    decoy_map = defaultdict(list)
    
    for key, value in signature.items():
        limit = thresholds.get(key, 50)
        
        # Meaningful computation buried in noise
        if value > limit:
            temp_results.append(value - limit)
            decoy_map[key].append('exceeded')  # Irrelevant tracking
        elif value < limit // 2:
            temp_results.append(-1 * (limit // 2 - value))
        else:
            temp_results.append(0)
            
        # Decoy side-effect
        decoy_map[key].append('processed')

    # Critical aggregation
    net_deviation = sum(temp_results)
    
    # Real answer derived here
    scaling_factor = len([x for x in temp_results if x != 0])
    if scaling_factor == 0:
        scaling_factor = 1
    
    final_score = net_deviation * scaling_factor
    
    # Final transformation (answer depends on this)
    adjustment = generate_baseline(10)  # returns base[7] = 7//2 = 3
    final_diagnostic = final_score + adjustment + evaluate_risk_level([64, 64, 120])
    
    return final_diagnostic

# Execution block with setup
if __name__ == "__main__":
    # Input data setup
    health_signature = {
        'neural': 88,
        'cardiac': 42,
        'respiratory': 68,
        'metabolic': 30
    }
    
    threshold_map = {
        'neural': 80,
        'cardiac': 50,  
        'respiratory': 60,
        'metabolic': 35
    }
    
    # Dead variables and irrelevant operations
    system_status = {'calibration': True, 'noise_floor': 0.002}
    audit_log = []
    for k in health_signature:
        audit_log.append(f"{k}:OK")  # Not used
    
    # Key execution point
    final_diagnostic = process_metrics(health_signature, threshold_map)
    
    # Output result
    print(f"Target result: {final_diagnostic}")