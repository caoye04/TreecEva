import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples():
    raw = [0.1, 0.4, 0.9, 1.6, 2.5, 3.6, 4.9, 6.4, 8.1, 10.0]
    offset = 0.5
    adjusted = [x + offset for x in raw]
    filtered = [x for x in adjusted if x > 1.0]
    return filtered

# Irrelevant helper: computes statistical moment (not used in final path)
def compute_moment(data, order=2):
    mean_val = sum(data) / len(data)
    return sum((x - mean_val) ** order for x in data) / len(data)

# Distraction function: simulates temperature drift compensation (unused)
def apply_drift_compensation(signal, temp_coeff=0.02):
    return [x * (1 + temp_coeff * 25) for x in signal]

# Signal normalization (used)
def normalize_signal(signal):
    max_val = max(signal)
    return [x / max_val for x in signal] if max_val > 0 else signal

# Data binning logic (partially relevant, but some outputs ignored)
def bin_data(normalized, bins=5):
    width = 1.0 / bins
    counts = [0] * bins
    for val in normalized:
        idx = min(int(val // width), bins - 1)
        counts[idx] += 1
    # Dead code path: unused histogram stats
    total = sum(counts)
    if total == 0:
        uniformity = 0.0
    else:
        uniformity = sum(c * c for c in counts) / (total * total)
    return counts  # Only counts used later

# Core analysis with conditional expression
def evaluate_coherence(bins):
    peak_bin = max(bins)
    secondary = sorted(bins)[-2] if len([b for b in bins if b > 0]) > 1 else 0
    # Conditional expression determining coherence score
    return 1.0 if peak_bin >= 3 and (peak_bin - secondary) >= 2 else 0.65

# Final diagnostic engine
def analyze_signal(data, thresh):
    base_score = sum(data) * 100
    bin_distribution = bin_data(data)
    coherence = evaluate_coherence(bin_distribution)
    adjustment_factor = 1.2 if coherence > 0.9 else 0.88
    refined_score = base_score * adjustment_factor
    # Final threshold comparison using logical operation
    meets_threshold = refined_score >= thresh
    # Key variable computed here
    final_diagnostic = int(refined_score) if meets_threshold else int(thresh)
    return final_diagnostic

# --- Execution Workflow ---
samples = collect_samples()                    # Step 1: collect data
dummy_moment = compute_moment(samples, 3)     # Distractor: unused stat
compensated = apply_drift_compensation(samples)  # Red herring: unconnected path
normalized_samples = normalize_signal(samples)   # Relevant: normalize
dummy_hist = bin_data(normalized_samples, 4)   # Distractor call with diff bins
processed_data = normalize_signal(compensated)  # Actually use compensated path? No!
# Correction: revert to correct source due to calibration failure flag
CALIBRATION_FAILED = True
processed_data = normalize_signal(samples) if CALIBRATION_FAILED else processed_data

threshold = 345.67
final_diagnostic = analyze_signal(processed_data, threshold)
print(f"Target result: {final_diagnostic}")