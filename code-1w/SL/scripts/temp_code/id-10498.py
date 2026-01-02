import itertools

# Simulated sensor data processing with noise filtering and scoring
raw_readings = [145, 273, 91, 88, 205, 117, 63, 312, 189, 74]
noise_floor = 75
signal_ceiling = 300

# Irrelevant transformation: frequency mapping (distractor)
frequencies = [r % 13 for r in raw_readings if r > 100]
modulated_signals = [f * 1.7 for f in frequencies]

# Relevant signal extraction
cleaned_signals = [r for r in raw_readings if noise_floor < r < signal_ceiling]

# Decoy statistical calculation (dead path)
mean_signal = sum(raw_readings) / len(raw_readings)
median_proxy = sorted(raw_readings)[len(raw_readings)//2]

# Signal normalization using min-max scaling
min_val, max_val = min(cleaned_signals), max(cleaned_signals)
normalized = [(x - min_val) / (max_val - min_val) for x in cleaned_signals]

# Apply non-linear gain boost (relevant)
gain_adjusted = [x ** 1.5 for x in normalized]

# Window slicing for trend analysis (python slicing feature)
trend_window = gain_adjusted[1:-1]  # Exclude edges
peaks = [i for i in range(1, len(trend_window)-1) if trend_window[i-1] < trend_window[i] > trend_window[i+1]]

# Create synthetic reference thresholds (irrelevant but plausible)
thresh_gen = itertools.accumulate([0.1]*5, lambda a, x: a * 1.2 + 0.05)
thresholds = [round(t, 3) for t in thresh_gen]

# Duplicate data handling (set operation - python feature)
dup_check = [0.213, 0.472, 0.472, 0.631, 0.631, 0.631, 0.889]
unique_patterns = list(set(dup_check))
unique_patterns.sort()

# Scale to integer scores for precision
scaled_values = [int(g * 1000) for g in gain_adjusted]

# Spurious correlation matrix (decoy structure)
corr_matrix = [[i*j for j in range(4)] for i in range(4)]

# Real computation begins here — multi-step aggregation
def compute_aggregate(values, limits):
    base_score = sum(values)
    
    # Conditional modulation based on threshold crossings (boolean logic)
    limit_crosses = sum(1 for v in values for l in limits if v > l * 100)
    
    # Bit manipulation for entropy-like weighting
    entropy_key = len(values) ^ limit_crosses
    adjustment_factor = (entropy_key & 7) - 3  # Range: -3 to 4
    
    # Red herring: unused recursive function inside scope
def bad_recursive(n):
    if n <= 1:
        return 1
    return n + bad_recursive(n-2)  # Never called

# Back to main flow
final_score = compute_aggregate(scaled_values, thresholds)
Result: {final_score}