import itertools

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    return [0.12, 0.34, 0.55, 0.61, 0.63, 0.71, 0.82, 0.59, 0.44, 0.21]

def filter_outliers(data, limit=0.8):
    # Irrelevant filtering (distractor)
    return [x for x in data if x <= limit]

def rolling_average(values, window=3):
    averages = []
    for i in range(len(values) - window + 1):
        averages.append(sum(values[i:i+window]) / window)
    return averages

def count_transitions(signal):
    # Counts how many times signal crosses midline (0.5)
    transitions = 0
    for i in range(1, len(signal)):
        if (signal[i-1] < 0.5) != (signal[i] < 0.5):
            transitions += 1
    return transitions

def compute_entropy(data):
    # Dead function - not used in final computation (red herring)
    from math import log
    freq = {}
    for x in data:
        key = int(x * 10)
        freq[key] = freq.get(key, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return entropy

def extract_peaks(signal):
    # Returns indices where value > 0.6 and increasing then decreasing
    peaks = []
    for i in range(1, len(signal)-1):
        if signal[i-1] < signal[i] > signal[i+1] and signal[i] > 0.6:
            peaks.append(i)
    return peaks

def smooth_signal(signal):
    # Moving average smoothing (unused path)
    smoothed = [signal[0]]
    for i in range(1, len(signal)-1):
        smoothed.append(sum(signal[i-1:i+2]) / 3)
    smoothed.append(signal[-1])
    return smoothed

def generate_combinations(length):
    # Distractor: generates bit patterns not used in main logic
    return list(itertools.product([0, 1], repeat=length))[:10]

def validate_coherence(signal):
    # Measures consistency of upward/downward runs
    if len(signal) < 2:
        return True
    directions = [(signal[i] < signal[i+1]) for i in range(len(signal)-1)]
    changes = sum(1 for i in range(len(directions)-1) if directions[i] != directions[i+1])
    return changes < 5

def analyze_pattern(sequence, threshold):
    # Core logic embedded within distractions
    
    # Step 1: Count transitions across 0.5
    cross_count = count_transitions(sequence)
    
    # Step 2: Find peak positions above threshold
    peaks = extract_peaks(sequence)
    
    # Step 3: Compute rolling average over 3-element window
    roll_avg = rolling_average(sequence)
    
    # Step 4: Count how many rolling averages exceed threshold
    high_avg_count = len([x for x in roll_avg if x > threshold])
    
    # Step 5: Use itertools to group consecutive rising values in roll_avg
    rising_runs = []
    current_run = 0
    for a, b in itertools.pairwise(roll_avg):  # pairwise from itertools
        if b > a:
            current_run += 1
        else:
            if current_run > 0:
                rising_runs.append(current_run)
                current_run = 0
    if current_run > 0:
        rising_runs.append(current_run)
    
    # Step 6: Sum of squares of rising run lengths (distraction but computed)
    run_energy = sum(r**2 for r in rising_runs)
    
    # Step 7: Validate sequence coherence (used in decision)
    coherent = validate_coherence(sequence)
    
    # Step 8: Final diagnostic calculation
    base_score = cross_count * 100
    peak_bonus = len(peaks) * 25
    avg_bonus = high_avg_count * 15
    
    final_score = base_score + peak_bonus + avg_bonus
    
    # Apply penalty if not coherent
    if not coherent:
        final_score -= 50
    
    # This is the actual answer variable
    final_diagnostic = final_score
    
    # Irrelevant print for distraction
    # print(f'Debug - Run energy: {run_energy}')
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    raw_data = collect_readings()
    
    # Irrelevant operations (distractors)
    filtered_data = filter_outliers(raw_data)
    smoothed_data = smooth_signal(raw_data)
    combo_list = generate_combinations(4)
    entropy_value = compute_entropy(raw_data)  # Computed but unused
    
    # Key data transformation
    signal_sequence = [x * 1.5 for x in raw_data]  # Amplify signal
    
    # Critical execution point
    final_diagnostic = analyze_pattern(signal_sequence, threshold=0.65)
    
    Target result: {final_diagnostic}