from collections import deque

def simulate_circuit():
    # Initial signal states: id -> voltage_level
    signals = {'A': 1, 'B': 0, 'C': 1, 'D': 0, 'E': 1}
    # Gate operations: (gate_type, input_signals, output_signal)
    gates = [
        ('AND', ['A', 'B'], 'X'),
        ('OR', ['C', 'D'], 'Y'),
        ('XOR', ['X', 'Y'], 'Z'),
        ('AND', ['Z', 'E'], 'W'),
        ('OR', ['W', 'A'], 'V')
    ]
    
    processing_queue = deque(gates)
    
    while processing_queue:
        gate_type, inputs, output = processing_queue.popleft()
        
        # Short-circuit evaluation for efficiency
        if gate_type == 'AND':
            signals[output] = signals[inputs[0]] and signals[inputs[1]]
        elif gate_type == 'OR':
            signals[output] = signals[inputs[0]] or signals[inputs[1]]
        else:  # XOR
            signals[output] = signals[inputs[0]] ^ signals[inputs[1]]
        
        # Early termination if final signal is computed
        if output == 'V':
            final_signal_strength = signals[output] * 100 + sum(signals.values())
            return final_signal_strength
    
    return 0

final_signal_strength = simulate_circuit()
print(f"Result: {final_signal_strength}")