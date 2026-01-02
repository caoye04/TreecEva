import math

# Simulated biomedical signal processing system
def analyze_waveform(signal_data, sample_rate):
    fft_magnitude = [abs(val) for val in signal_data]
    peak_frequency = max(fft_magnitude)
    avg_power = sum(x**2 for x in fft_magnitude) / len(fft_magnitude)
    
    # Irrelevant transformation (distractor)
    normalized = [x / (peak_frequency + 1e-9) for x in fft_magnitude]
    entropy = -sum(p * math.log(p + 1e-9) for p in normalized)
    
    # Unused feature extraction (dead code path)
    def compute_fractal_dimension():
        return 1.7 + 0.3 * math.sin(len(signal_data))
    
    # Actual relevant metric
    signal_rms = math.sqrt(avg_power)
    return signal_rms

# Red herring function - looks important but unused
def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def extract_features(readings):
    # Extract time-domain features with distractions
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    skewness = sum((x - mean_val) ** 3 for x in readings) / (len(readings) * (variance ** 1.5)) if variance > 0 else 0
    
    # Distractor: unused frequency analysis
    dominant_freq = max(abs(x) for x in readings) / (mean_val + 1e-6)
    
    # Composite index (only one component used later)
    stability_index = 1 / (1 + variance)
    return {
        'avg': mean_val,
        'variability': variance,
        'asymmetry': skewness,
        'stability': stability_index,
        'dominance': dominant_freq
    }

def evaluate_risk_level(biomarkers, age_factor):
    base_risk = 0.5
    adjustment = 0
    
    # Complex conditional logic with misleading branches
    if biomarkers['asymmetry'] > 0.3:
        adjustment += 0.2 * age_factor
        if biomarkers['variability'] < 10:
            adjustment -= 0.1
        else:
            adjustment += 0.15
    elif biomarkers['stability'] < 0.7:
        adjustment += 0.3
        # Dead branch (never reached due to prior condition)
        if biomarkers['dominance'] > 2.0:
            adjustment *= 1.2
    
    # Final risk calculation (partially influenced by logic above)
    risk_score = base_risk + adjustment
    risk_category = 'High' if risk_score > 0.7 else 'Normal'
    
    # Return multiple values, only one used downstream
    return risk_score, risk_category, adjustment

# Core processing chain
def process_metrics(indicators, threshold_config):
    # Primary data transformation pipeline
    filtered_data = [x for x in indicators if x > threshold_config['noise_floor']]
    
    # Multi-step computation with intermediate distractors
    transformed = []
    cumulative_shift = 0
    
    for i, val in enumerate(filtered_data):
        # Complex transformation
        shifted = val + math.sin(i * 0.5) - cumulative_shift
        adjusted = shifted * (1 + math.exp(-i * 0.1))
        
        # Update shift based on pattern
        if i % 3 == 0 and i > 0:
            cumulative_shift += 0.5 * math.log(adjusted + 1)
        
        transformed.append(adjusted)
    
    # Secondary processing with conditional expression
    summary_stats = {
        'count': len(transformed),
        'total': sum(transformed),
        'peak': max(transformed) if transformed else 0,
        'baseline': threshold_config['reference_level']
    }
    
    # Compute diagnostic score through multi-stage logic
    offset = summary_stats['peak'] - summary_stats['baseline']
    multiplier = 2.0 if offset > 15 else (1.5 if offset > 5 else 1.0)
    
    # Critical calculation step
    temp_diagnostic = (summary_stats['total'] * multiplier) / (summary_stats['count'] + 1e-8)
    
    # Final nonlinear calibration
    final_diagnostic = int(temp_diagnostic * 1.75) + 32
    
    # Dead code - looks like post-processing but unused
    if final_diagnostic > 100:
        final_diagnostic = 100 - (final_diagnostic % 10)
    
    return final_diagnostic

# Main execution block
if __name__ == "__main__":
    # Simulated sensor inputs (biomedical context)
    raw_signals = [-0.2, 1.1, 0.8, 2.3, -1.0, 4.5, 3.2, 2.1, 5.7, 6.3, 4.1, 3.9, 7.2]
    
    # Process primary waveform
    processed_rms = analyze_waveform(raw_signals, sample_rate=100)
    
    # Extract secondary features
    features = extract_features(raw_signals)
    
    # Evaluate risk (partial result used)
    _, category, adj = evaluate_risk_level(features, age_factor=1.2)
    
    # Generate derived indicators (mix of real and fake data)
    health_indicators = [
        processed_rms * 10,
        features['avg'] * 15,
        features['stability'] * 50,
        adj * 200,
        6.3, 4.8, 7.1, 5.5, 8.2, 6.9, 7.7
    ]
    
    # Threshold configuration (some values unused)
    thresholds = {
        'noise_floor': 3.0,
        'reference_level': 4.5,
        'critical_limit': 9.0,
        'hysteresis': 0.5
    }
    
    # Execute core statement
    final_diagnostic = process_metrics(health_indicators, thresholds)
    
    # Print target result
    print(f"Target result: {final_diagnostic}")