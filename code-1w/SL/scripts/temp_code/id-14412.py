from collections import defaultdict, Counter
import math

# Simulated health monitoring system with sensor data processing
def analyze_rhythm(sequence):
    if not sequence:
        return 0
    rhythm_score = 0
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            rhythm_score += 1
        elif sequence[i] < sequence[i-1]:
            rhythm_score -= 1
    return abs(rhythm_score)

def compute_entropy(data):
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

def validate_checksum(record):
    # Irrelevant validation function (decoy)
    return sum(record) % 7 == 0

def legacy_normalization(x):
    # Dead code path - never used
    return (x - min(x)) / (max(x) - min(x)) if max(x) != min(x) else [0]*len(x)

def filter_outliers(stream, limit=50):
    # Misleading: looks important but only used on decoy data
    return [x for x in stream if 10 <= x <= limit]

def generate_synthetic_data(n):
    # Distractor: generates unused synthetic records
    return [int(50 + 25 * math.sin(i)) for i in range(n)]

def extract_features(snapshot):
    # Extracts multiple features, some irrelevant
    stats = defaultdict(float)
    stats['mean'] = sum(snapshot) / len(snapshot)
    stats['peak'] = max(snapshot)
    stats['baseline'] = snapshot[0]
    stats['variance'] = sum((x - stats['mean'])**2 for x in snapshot) / len(snapshot)
    stats['zero_crossings'] = sum(1 for i in range(1, len(snapshot)) 
                                if (snapshot[i-1] < 0 <= snapshot[i]))
    return stats

def evaluate_stability(features, config):
    # Complex weighting with red herring coefficients
    stability = 0
    stability += features['mean'] * config.get('trend_weight', 0.3)
    stability -= features['variance'] * config.get('noise_penalty', 0.1)
    stability += features['peak'] * 0.05  # Unused weight
    stability = max(0, stability)
    return int(stability)

def process_metrics(data, criteria):
    # Core logic embedded within distractions
    results = []
    diagnostics = []
    temporal_patterns = []
    
    for record in data:
        # Real feature extraction
        feat = extract_features(record)
        entropy = compute_entropy(record)
        rhythm = analyze_rhythm(record)
        
        # Critical decision logic
        if feat['mean'] > criteria['threshold_low']:
            if entropy > criteria['entropy_min']:
                if rhythm < criteria['rhythm_cap']:
                    results.append(feat['mean'] * 2)
                else:
                    results.append(feat['mean'] / 2)
            else:
                results.append(feat['mean'])
        else:
            results.append(0)
        
        # Side computation (distractor)
        temp_diag = {
            'raw_length': len(record),
            'checksum_ok': validate_checksum(record),
            'entropy_flag': entropy > 3.0
        }
        diagnostics.append(temp_diag)
        
        # Accumulate pattern history (partially relevant)
        temporal_patterns.append(rhythm)
    
    # Final aggregation - key answer derivation
    aggregate = sum(results)
    trend_consistency = sum(1 for t in temporal_patterns if t <= 3)
    
    # Final diagnostic depends only on specific path
    if trend_consistency >= len(temporal_patterns) // 2:
        final_diagnostic = int(aggregate * 1.2)
    else:
        final_diagnostic = int(aggregate * 0.8)
    
    # Decoy output variables
    summary_report = {
        'total_records': len(data),
        'valid_streams': len([d for d in diagnostics if d['checksum_ok']]),
        'high_entropy_count': len([d for d in diagnostics if d['entropy_flag']])
    }
    
    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    # Simulated patient health data streams (real input)
    health_data = [
        [45, 50, 55, 60, 58, 52],
        [30, 35, 40, 42, 38, 34],
        [65, 68, 70, 69, 66, 64],
        [25, 20, 18, 22, 26, 30]
    ]
    
    # Threshold configuration (critical parameters)
    thresholds = {
        'threshold_low': 35,
        'entropy_min': 2.0,
        'rhythm_cap': 4
    }
    
    # Unused data structures (distraction)
    dummy_logs = generate_synthetic_data(100)
    outlier_filtered = filter_outliers(dummy_logs, 40)
    
    # Configuration map with extra keys (red herring)
    analysis_config = {
        'trend_weight': 0.3,
        'noise_penalty': 0.1,
        'debug_mode': False,
        'version': '2.1a'
    }
    
    # Key execution point
    final_diagnostic = process_metrics(health_data, thresholds)
    
    # Output result
    print(f"Result: {final_diagnostic}")