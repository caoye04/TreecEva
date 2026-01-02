import itertools

# Neural signal processing simulation
def simulate_neural_response(stimulus, weights):
    weighted_sum = sum(s * w for s, w in zip(stimulus, weights))
    activation = weighted_sum / len(weights)
    
    # Bitwise consistency check on stimulus pattern
    pattern_key = stimulus[0] ^ stimulus[1] | stimulus[2]
    safety_toggle = (pattern_key & 1) == 1
    
    # Conditional expression for output decision
    bool_output = 'high' in ('low', 'mid', 'high') if activation > 0.3 else False
    
    # Key statement
    threshold_flag = not (activation < 0.5) and bool_output
    
    # Irrelevant tracking variable (minimal distraction)
    log_entry = f'Stimulus processed: {len(stimulus)} components'
    
    return threshold_flag

# Input data
stimulus_input = [0.8, 0.4, 0.6]
weight_config = [0.5, 0.7, 0.9]

# Execute
result = simulate_neural_response(stimulus_input, weight_config)
print(f'Result: {result}')