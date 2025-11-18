import collections
import math

def process_acoustic_data(raw_readings):
    # State definitions
    STATE_LOW, STATE_MEDIUM, STATE_HIGH = 0, 1, 2
    current_state = STATE_LOW
    
    # Amplification factors per state
    amplification_factors = {STATE_LOW: 1.2, STATE_MEDIUM: 1.8, STATE_HIGH: 2.5}
    
    # Weighted averaging parameters
    alpha = 0.15  # Smoothing factor
    processed_signal = 0.0
    
    # Counters for state transitions
    transition_counter = collections.defaultdict(int)
    
    for idx, reading in enumerate(raw_readings):
        # State transition logic based on reading magnitude
        if reading < 50.0:
            new_state = STATE_LOW
        elif reading < 150.0:
            new_state = STATE_MEDIUM
        else:
            new_state = STATE_HIGH
            
        # Record transition (except initial state)
        if idx > 0 and new_state != current_state:
            transition_key = f"{current_state}->{new_state}"
            transition_counter[transition_key] += 1
        
        current_state = new_state
        
        # Apply amplification based on current state
        amplified_reading = reading * amplification_factors[current_state]
        
        # Apply exponential moving average
        processed_signal = alpha * amplified_reading + (1 - alpha) * processed_signal
    
    # Calculate final score using transition entropy
    total_transitions = sum(transition_counter.values())
    if total_transitions == 0:
        entropy_bonus = 1.0
    else:
        # Compute Shannon entropy of transitions
        entropy = 0.0
        for count in transition_counter.values():
            probability = count / total_transitions
            entropy -= probability * math.log(probability, 2)
        entropy_bonus = 1.0 + entropy / 10.0  # Normalize entropy impact
    
    # Final weighted score
    processed_frequency_score = processed_signal * entropy_bonus
    return processed_frequency_score

# Simulated acoustic readings over 72 hours (hourly samples)
acoustic_readings = [
    45.2, 47.8, 120.5, 135.1, 142.3, 165.7, 178.9, 182.4,
    190.1, 205.6, 210.3, 225.8, 150.2, 145.7, 138.9, 125.4,
    110.6, 95.3, 82.7, 75.1, 68.9, 62.4, 55.8, 48.2,
    42.6, 38.9, 45.3, 52.7, 60.1, 68.4, 76.8, 85.2,
    92.6, 105.3, 118.7, 132.1, 145.8, 158.4, 172.9, 185.6,
    198.3, 210.7, 225.4, 238.1, 245.9, 252.6, 260.3, 268.7,
    275.2, 282.8, 290.1, 298.4, 305.7, 312.9, 320.1, 328.6,
    335.2, 342.8, 350.1, 358.4, 365.7, 372.9, 380.1, 388.6,
    395.2, 402.8, 410.1, 418.4, 425.7, 432.9, 440.1, 448.6
]

processed_frequency_score = process_acoustic_data(acoustic_readings)
print(f"Result: {processed_frequency_score:.6f}")