import itertools

# Simulated quantum phase alignment system
def generate_phase_sequence(seed, length):
    seq = [seed]
    for i in range(1, length):
        seq.append((seq[-1] * 17 + 257) % 65536)
    return [s / 65536.0 for s in seq]

# Irrelevant transformation - decoy function
def transform_coordinates(coords):
    return [(c * 3.14159) % 1.0 for c in coords]

# Unused helper - dead code path
def compute_entropy(data):
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    return -sum(f * log(f) for f in freq.values())

# Core stability analyzer with distractors embedded
def calculate_stability_index(phases):
    n = len(phases)
    if n == 0:
        return 0.0
    
    # Distractor: irrelevant normalization
    normalized = [abs(p - 0.5) * 2 for p in phases]
    
    # Real computation begins: find coherent subsequences
    coherence_windows = []
    for size in range(2, min(6, n//2 + 1)):
        windows = [phases[i:i+size] for i in range(n - size + 1)]
        variances = [sum((x - sum(w)/len(w))**2 for x in w) / len(w) for w in windows]
        coherence_windows.extend([v for v in variances if v < 0.01])
    
    # Distractor: unused accumulation
    cumulative_drift = 0.0
    for i in range(1, len(phases)):
        drift = abs(phases[i] - phases[i-1])
        cumulative_drift += drift * 0.1
    
    # Real logic: count stable oscillations using slicing and conditional logic
    oscillation_count = 0
    for i in range(1, n-1):
        prev, curr, next_val = phases[i-1], phases[i], phases[i+1]
        if (prev < curr > next_val) or (prev > curr < next_val):  # Local extrema
            window = phases[max(0, i-3):i+4]  # 7-point window via slicing
            if len(window) >= 5:
                sorted_window = sorted(window)
                median = sorted_window[len(sorted_window)//2]
                if abs(curr - median) < 0.15:
                    oscillation_count += 1
    
    # Secondary real computation: frequency domain approximation
    signal_energy = sum(p**2 for p in phases)
    
    # Distractor: fake harmonic analysis
    harmonics = []
    for h in range(1, 10):
        harmonic_proj = sum(phases[i] * (i % h == 0) for i in range(len(phases)))
        harmonics.append(harmonic_proj)
    
    # Key calculation using itertools and conditional expression
    pairs = list(itertools.combinations(phases[::2], 2))  # Use slicing and combinations
    strong_pairs = [p for p in pairs if abs(p[0] - p[1]) < 0.1]
    
    # Final index calculation - this is what actually matters
    base_index = signal_energy * n
    adjustment = oscillation_count if oscillation_count > 5 else (5 if oscillation_count else 1)
    pair_factor = len(strong_pairs) or 1
    
    final_score = base_index * adjustment / pair_factor
    
    # Critical assignment point
    energy_threshold = int(final_score * 100) / 100.0  # Rounded to 2 decimal places
    
    # More red herrings: unused transformations
    spectral_peaks = [i for i in range(1, len(phases)-1) 
                     if phases[i] > phases[i-1] and phases[i] > phases[i+1] and phases[i] > 0.7]
    peak_ratio = len(spectral_peaks) / n if n else 0
    
    # Decoy return alternative (never reached due to early return)
    if False:
        return sum(normalized) * peak_ratio
        
    return energy_threshold

# Main execution with red herring data
phase_seed = 1234
raw_quantum_data = generate_phase_sequence(phase_seed, 32)
decoy_coordinates = [x * 0.738 for x in raw_quantum_data]
transformed_coords = transform_coordinates(decoy_coordinates)  # Dead usage

# Actual critical computation
phase_vector = raw_quantum_data[4:28]  # Slicing out a subsegment

# This is the key statement
energy_threshold = calculate_stability_index(phase_vector)

# Print result as required
print(f"Result: {energy_threshold}")