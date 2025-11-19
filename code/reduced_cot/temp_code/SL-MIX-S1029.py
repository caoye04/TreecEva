import itertools

def evaluate_gate(inputs, gate_type, delay_map):
    if gate_type == 'AND':
        return all(inputs), delay_map['AND']
    elif gate_type == 'OR':
        return any(inputs), delay_map['OR']
    elif gate_type == 'XOR':
        result = inputs[0]
        for i in range(1, len(inputs)):
            result ^= inputs[i]
        return result, delay_map['XOR']
    else:  # NOT gate
        return not inputs[0], delay_map['NOT']

def analyze_circuit(signals, config):
    total_delay = 0
    processed_signals = []
    
    for sig in signals:
        if isinstance(sig, tuple):
            sub_result, sub_delay = analyze_circuit(sig[0], config)
            processed_signals.append(sub_result)
            total_delay += sub_delay
        else:
            processed_signals.append(sig)
    
    if isinstance(config, dict) and 'gate' in config:
        result, gate_delay = evaluate_gate(processed_signals, config['gate'], config['delays'])
        total_delay += gate_delay
        return result, total_delay
    else:
        return processed_signals[0], total_delay

signal_network = (
    [
        ([(True, False), {'gate': 'XOR', 'delays': {'AND': 3, 'OR': 2, 'XOR': 4, 'NOT': 1}}], 
         {'gate': 'NOT', 'delays': {'AND': 3, 'OR': 2, 'XOR': 4, 'NOT': 1}}),
        [False, True]
    ], 
    {'gate': 'OR', 'delays': {'AND': 3, 'OR': 2, 'XOR': 4, 'NOT': 1}}
)

combinations = list(itertools.product([True, False], repeat=2))
max_delay = 0

for combo in combinations:
    test_signal = ([combo[0], combo[1]], {'gate': 'AND', 'delays': {'AND': 3, 'OR': 2, 'XOR': 4, 'NOT': 1}})
    _, delay = analyze_circuit(test_signal, test_signal[1])
    if delay > max_delay:
        max_delay = delay

propagation_delay = max_delay + (lambda x: x * 2 if x % 2 == 0 else x + 1)(len(combinations))
print(f"Result: {propagation_delay}")