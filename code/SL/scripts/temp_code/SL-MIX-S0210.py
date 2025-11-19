import math

def compute_rms(values):
    if not values:
        return 0
    return math.sqrt(sum(x**2 for x in values) / len(values))

def process_waveform(waveform_data, threshold=5.0):
    # Extract amplitude values from nested structure
    amplitudes = [amp for component in waveform_data.values() 
                  for amp in component['amplitude_values']]
    
    # Filter high-amplitude components using list comprehension
    significant_amps = [a for a in amplitudes if a > threshold]
    
    # Short-circuit evaluation for early exit
    if not significant_amps or len(significant_amps) < 2:
        return 0
    
    # Compute weighted RMS
    rms = compute_rms(significant_amps)
    weight = 1.5 if len(significant_amps) > 5 else 1.2
    return rms * weight

# Audio waveform data representation
waveforms = {
    'bass': {
        'f100': {'amplitude_values': [2.1, 4.3, 6.7, 8.9]},
        'f200': {'amplitude_values': [1.2, 3.4, 5.6, 7.8, 9.1]}
    },
    'treble': {
        'f1000': {'amplitude_values': [0.5, 2.3, 4.5, 6.7, 8.9, 10.1]},
        'f2000': {'amplitude_values': [1.1, 2.2, 3.3]}
    }
}

# Process each waveform category
processed_scores = {}
for category, data in waveforms.items():
    score = process_waveform(data)
    processed_scores[category] = score

# Calculate overall quality with conditional branching
if processed_scores.get('bass', 0) > processed_scores.get('treble', 0):
    quality_score = processed_scores['bass'] * 1.1
else:
    # Dictionary comprehension for bonus calculation
    bonuses = {k: v * 0.05 for k, v in processed_scores.items() if v > 0}
    quality_score = sum(processed_scores.values()) + sum(bonuses.values())

print(f"Result: {round(quality_score, 2)}")