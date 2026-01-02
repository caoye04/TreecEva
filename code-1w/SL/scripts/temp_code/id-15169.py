from collections import defaultdict, Counter
from itertools import zip_longest, cycle

# Simulated patient health monitoring system with noise and red herrings
def analyze_rhythm(pattern):
    if len(pattern) < 3:
        return False
    return all(a <= b <= c for a, b, c in zip(pattern, pattern[1:], pattern[2:]))

def compute_entropy(seq):
    counts = Counter(seq)
    total = len(seq)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Non-standard 'entropy-like' computation (red herring)
    return round(entropy, 4)

def shift_window(data, size=3):
    """Sliding window generator - used in one dead path"""
    for i in range(len(data) - size + 1):
        yield data[i:i+size]

def deprecated_normalizer(x):
    # Unused function - decoy
    return (x - min(x)) / (max(x) - min(x)) if max(x) != min(x) else [0] * len(x)

def false_alarm_detector(seq):
    # Complex logic that's never invoked
    state = 0
    for val in seq:
        state = (state * 7 + val) % 13
    return state in [3, 7, 11]

# Irrelevant signal processing functions
def bandpass_filter(signal, low, high):
    return [x for x in signal if low < abs(x) < high]

def fourier_approximation(series):
    # Fake frequency analysis
    return sum((i+1)*val for i, val in enumerate(series[:5])) % 100

# Real data pipeline starts here
def extract_features(record):
    features = defaultdict(float)
    readings = record['readings']
    
    # Core relevant metrics
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    trend = sum(readings[-10:]) - sum(readings[:10])  # Net directional shift
    
    features['baseline'] = avg
    features['variance'] = variance
    features['trend_score'] = abs(trend)
    
    # Distractor computations
    features['fake_entropy'] = compute_entropy([int(x) % 10 for x in readings])
    features['rhythm_stable'] = int(analyze_rhythm(sorted(readings)[:8]))
    
    # Red herring using itertools
    paired = list(zip_longest(readings[::2], readings[1::2], fillvalue=0))
    features['paired_sum'] = sum(abs(a - b) for a, b in paired)
    
    return dict(features)

def evaluate_stability(metrics, config):
    # Actual decision logic buried in noise
    score = 0
    score += 1 if metrics['baseline'] > config['normal_range'][0] else -1
    score += 1 if metrics['baseline'] < config['normal_range'][1] else -1
    score += 2 if metrics['variance'] < config['thresholds']['variability'] else -2
    score += 1 if metrics['trend_score'] < 150 else -3  # Critical condition
    
    # Irrelevant conditions (dead logic due to impossible branches)
    if metrics['fake_entropy'] > 100:  # Impossible by construction
        score += 5
    if metrics['rhythm_stable'] not in [0, 1]:  # Always true
        score -= 10
    
    return score > 0

def process_metrics(patient_data, criteria):
    results = []
    summary = defaultdict(int)
    
    for record in patient_data:
        feats = extract_features(record)
        stable = evaluate_stability(feats, criteria)
        
        # Real classification
        if stable and feats['trend_score'] < 120:
            summary['stable_low_trend'] += 1
        elif not stable and feats['variance'] > 400:
            summary['unstable_high_var'] += 1
        else:
            summary['moderate'] += 1
        
        # Dead-end accumulation (decoy)
        dummy_cycle = list(cycle([1, 0]))[:len(record['readings'])]
        summary['sync_index'] += sum(d & int(f > 50) for d, f in zip(dummy_cycle, record['readings']))
    
    # Core answer derivation
    base = summary['stable_low_trend'] * 100
    penalty = summary['unstable_high_var'] * 25
    bonus = summary['moderate'] * 10
    final_diagnostic = base - penalty + bonus
    
    # More distractions
    temp_seq = [summary[k] for k in summary]
    final_diagnostic += (temp_seq[0] ^ temp_seq[-1]) * 2 if len(temp_seq) > 1 else 0
    final_diagnostic -= sum(1 for v in summary.values() if v == 0) * 15
    
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    # Simulated dataset
    health_data = [
        {'id': 'P001', 'readings': [72, 75, 73, 74, 76, 78, 77, 75, 73, 72, 70, 68, 69, 71, 73, 74, 75, 77, 79, 80]},
        {'id': 'P002', 'readings': [88, 92, 95, 98, 102, 105, 108, 104, 100, 96, 93, 90, 88, 85, 82, 80, 78, 76, 75, 74]},
        {'id': 'P003', 'readings': [65, 68, 70, 72, 75, 78, 80, 82, 85, 88, 90, 92, 95, 98, 100, 102, 105, 108, 110, 112]},
        {'id': 'P004', 'readings': [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]},
        {'id': 'P005', 'readings': [60, 58, 55, 52, 50, 48, 45, 42, 40, 38, 35, 32, 30, 28, 25, 22, 20, 18, 15, 12]}
    ]
    
    thresholds = {
        'normal_range': (60, 100),
        'thresholds': {
            'variability': 400,
            'critical_trend': 150
        }
    }
    
    # Dead data structures (distractors)
    legacy_mapping = [[i, chr(65 + (i % 26))] for i in range(30)]
    lookup_cube = [[[i+j+k for k in range(3)] for j in range(3)] for i in range(3)]
    
    # Signal filtering (unused)
    filtered_signals = []
    for entry in health_data:
        clean = bandpass_filter(entry['readings'], 10, 500)
        approx_freq = fourier_approximation(clean)
        filtered_signals.append({'source': entry['id'], 'energy': approx_freq})
    
    # Key execution point
    final_diagnostic = process_metrics(health_data, thresholds)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")