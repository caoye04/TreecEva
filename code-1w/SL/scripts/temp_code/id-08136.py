from collections import defaultdict, Counter
import math

# Simulated sensor data processing system with diagnostic analysis

def preprocess_waveform(signal_chunk):
    # Irrelevant transformation (dead path)
    return [x * 1.05 for x in signal_chunk if x > 0]

def compute_entropy(values):
    # Misleading statistical measure (not used in final result)
    freqs = Counter(values)
    total = len(values)
    entropy = -sum((count / total) * math.log2(count / total) for count in freqs.values())
    return round(entropy, 3)

def extract_features(raw_data, config):
    feature_set = []
    for i, segment in enumerate(raw_data):
        if i % 3 == 0:
            # Real transformation: sum of squares for energy calculation
            energy = sum(x ** 2 for x in segment[:5])
            feature_set.append(energy)
    # Distractor: unused normalization
    normalized = [f / max(feature_set) for f in feature_set]
    return feature_set  # Only raw features are used

def evaluate_stability(metrics, bounds):
    # Complex but irrelevant stability check
    trends = defaultdict(lambda: 'stable')
    for key, val in metrics.items():
        if val > bounds['upper'] * 1.2:
            trends[key] = 'critical'
        elif val < bounds['lower'] * 0.8:
            trends[key] = 'recovering'
    return dict(trends)

def filter_artifacts(samples, mask):
    # Dead code path — never actually called
    cleaned = []
    for s, m in zip(samples, mask):
        if m and abs(s) < 1e4:
            cleaned.append(s * 0.9)
    return cleaned

def build_threshold_map(levels):
    # Actual relevant function: creates mapping used later
    t_map = defaultdict(float)
    for idx, lvl in enumerate(levels):
        t_map[f'chan_{idx}'] = lvl * 0.7 + (idx % 4) * 15
    return t_map

def analyze_signal(buffer, thresholds):
    # Core logic hidden among distractions
    valid_entries = 0
    cumulative_adjustment = 0.0
    
    for entry in buffer:
        chan_id = entry['channel']
        magnitude = entry['amplitude']
        ref_key = f'chan_{chan_id}'
        
        # Key conditional logic chain (4 levels deep)
        if ref_key in thresholds:
            if magnitude > thresholds[ref_key]:
                phase_flag = entry.get('phase', 0) > 0.5
                if phase_flag:
                    weight = 1.75 if entry['quality'] > 0.8 else 1.2
                    # Critical arithmetic computation
                    adjusted_score = (magnitude - thresholds[ref_key]) * weight
                    cumulative_adjustment += adjusted_score
                    valid_entries += 1
    
    # Final diagnostic depends on both count and accumulated adjustment
    if valid_entries == 0:
        return 0
    
    base_diagnostic = int(cumulative_adjustment / valid_entries)
    # Final answer derived from averaged adjustment
    final_diagnostic = base_diagnostic * 2 + 33
    return final_diagnostic

# --- Main execution with extensive distractors ---

# Simulated input data (real signal buffer)
pattern_buffer = [
    {'channel': 0, 'amplitude': 125, 'phase': 0.6, 'quality': 0.91},
    {'channel': 1, 'amplitude': 95,  'phase': 0.3, 'quality': 0.75},
    {'channel': 2, 'amplitude': 160, 'phase': 0.7, 'quality': 0.88},
    {'channel': 0, 'amplitude': 140, 'phase': 0.8, 'quality': 0.95},
    {'channel': 3, 'amplitude': 80,  'phase': 0.2, 'quality': 0.65},
    {'channel': 2, 'amplitude': 180, 'phase': 0.9, 'quality': 0.92}
]

# Real threshold configuration (used in analysis)
threshold_levels = [80, 70, 100, 60]
threshold_map = build_threshold_map(threshold_levels)

# Irrelevant auxiliary data structures
noise_profile = [[-21, 18], [33, -41], [12, 15]]
spectral_weights = list(map(lambda x: round(math.cos(x), 2), range(5)))
diagnostic_log = set()

# Unused intermediate computations (red herrings)
preprocessed = [preprocess_waveform(chunk) for chunk in [[-10,20,30], [40,-50,60]]]
feature_vector = extract_features([[1,2,3,4,5],[9,8,7,6,5]], {'mode': 'fast'})
stability_report = evaluate_stability({'metric_A': 45, 'metric_B': 120}, {'upper': 100, 'lower': 30})
data_entropy = compute_entropy([1,1,2,3,3,3,4,5])

# Decoy assignment (looks important but unused)
criticality_index = sum(abs(w) for w in spectral_weights) * len(noise_profile)

# Key execution point — this determines the answer
final_diagnostic = analyze_signal(pattern_buffer, threshold_map)

# Output result as required
print(f"Result: {final_diagnostic}")