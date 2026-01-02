import math

# Simulated system telemetry data with diagnostic flags
technical_metrics = {
    'voltage': [230, 245, 228, 250, 234, 240, 238],
    'frequency': [49.8, 50.1, 49.9, 50.3, 50.0, 49.7, 50.2],
    'load_cycle': [85, 92, 78, 95, 88, 90, 83]
}

system_flags = [True, False, True, True, False, True, True]

# Irrelevant auxiliary function (decoy)
def compute_efficiency_rating(data):
    total = 0
    for i in range(len(data['voltage'])):
        if data['frequency'][i] > 50:
            total += data['voltage'][i] * 0.95
        else:
            total += data['voltage'][i] * 1.02
    return round(total / len(data['voltage']), 2)

# Unused transformation (dead code path)
def shift_signal(sequence, offset=1):
    return sequence[offset:] + sequence[:offset]

# Misleading intermediate calculation (distractor)
current_stability_index = 0
for i, freq in enumerate(technical_metrics['frequency']):
    deviation = abs(freq - 50.0)
    current_stability_index += deviation * technical_metrics['load_cycle'][i]

# Another red herring: checksum that isn't used later
checksum = 0
for val in technical_metrics['voltage']:
    checksum ^= int(val)  # bitwise XOR chain

# Auxiliary state tracker with partial relevance
event_counter = {
    'critical': 0,
    'warning': 0,
    'normal': 0
}

# Data slicing used in actual logic (key python feature)
recent_loads = technical_metrics['load_cycle'][-5:]

# Primary analysis function with nested logic and distractors
def analyze_pattern(log_entries, flags):
    pattern_score = 0
    history = []
    
    # Nesting Level 1: Main loop over entries
    for idx in range(len(log_entries['voltage'])):
        voltage = log_entries['voltage'][idx]
        freq = log_entries['frequency'][idx]
        load = log_entries['load_cycle'][idx]
        flag_status = flags[idx]
        
        # Distractor block: complex but unused computation
        hypothetical_yield = 0
        if voltage > 240 and freq < 50.0:
            hypothetical_yield = (voltage * load) / (freq + 1)  # Not used
        
        # Real logic begins: conditional scoring
        base_score = 0
        
        # Nesting Level 2: Voltage-load interaction
        if voltage > 235:
            if load > 85:
                base_score += 12
            else:
                base_score += 5
        elif voltage < 230:
            base_score -= 8
        
        # Nesting Level 2: Frequency tolerance check
        if abs(freq - 50.0) < 0.2:
            base_score += 6
        elif abs(freq - 50.0) >= 0.3:
            base_score -= 10

        # Nesting Level 2: Flag multiplier logic
        adjustment_factor = 1.0
        # Nesting Level 3: Flag-based dynamic adjustment
        if flag_status:
            if load > 90:
                adjustment_factor = 1.4
            elif voltage < 230:
                adjustment_factor = 0.7
            else:
                adjustment_factor = 1.1
        else:
            adjustment_factor = 0.5  # Suppression when flag inactive

        # Apply adjustment (this is critical)
        adjusted_score = base_score * adjustment_factor
        
        # Update event counter (side effect with partial relevance)
        if base_score < 0:
            event_counter['warning'] += 1
        elif adjusted_score > 15:
            event_counter['critical'] += 1
        else:
            event_counter['normal'] += 1
        
        # Accumulate to main result
        pattern_score += int(round(adjusted_score))
        
        # Store intermediate (used later in slice)
        history.append({'index': idx, 'score': adjusted_score})
    
    # Nesting Level 1: Post-processing with slicing (key python feature)
    recent_history = [h['score'] for h in history[-4:]]
    surge_count = 0
    
    # Nesting Level 2: Surge detection in recent data
    for score in recent_history:
        if score > 14:
            surge_count += 1
    
    # Final composition using multiple concepts
    final_weight = 1.0
    if surge_count >= 2:
        final_weight = 1.25
    
    # Critical arithmetic combination
    raw_result = pattern_score * final_weight
    
    # Bitwise manipulation layer (actual use)
    # Embed status using bit shifting
    diagnostic_code = int(raw_result)  # Truncate
    diagnostic_code = diagnostic_code << 2  # Multiply by 4
    diagnostic_code = diagnostic_code ^ 0b1101  # XOR mask
    
    # Final adjustment based on dictionary state
    if event_counter['critical'] > event_counter['normal']:
        diagnostic_code += 50
    else:
        diagnostic_code -= 25
    
    return diagnostic_code

# Execution point of interest
final_diagnostic = analyze_pattern(technical_metrics, system_flags)

# Print result as required
print(f"Result: {final_diagnostic}")