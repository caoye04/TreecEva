from collections import defaultdict

class LogicGate:
    def __init__(self, gate_type, inputs):
        self.type = gate_type
        self.inputs = inputs
        self.output = 0
    
    def evaluate(self, signals):
        if self.type == 'AND':
            self.output = signals[self.inputs[0]] & signals[self.inputs[1]]
        elif self.type == 'OR':
            self.output = signals[self.inputs[0]] | signals[self.inputs[1]]
        elif self.type == 'XOR':
            self.output = signals[self.inputs[0]] ^ signals[self.inputs[1]]
        return self.output

gate_network = [
    LogicGate('AND', ['A', 'B']),
    LogicGate('OR', ['C', 'D']),
    LogicGate('XOR', [0, 1])
]

initial_states = {'A': 0b1101, 'B': 0b1011, 'C': 0b0110, 'D': 0b1001}
signal_strength = 0
simulation_cycles = 3

for cycle in range(simulation_cycles):
    current_signals = initial_states.copy()
    intermediate_outputs = {}
    
    # First level gates
    for i, gate in enumerate(gate_network[:2]):
        intermediate_outputs[i] = gate.evaluate(current_signals)
    
    # Second level gate processing outputs
    temp_signals = current_signals.copy()
    for idx, val in intermediate_outputs.items():
        temp_signals[idx] = val
    
    # Final output calculation
    signal_strength = gate_network[2].evaluate(temp_signals)
    
    # State transition for next cycle
    initial_states['A'] = (initial_states['A'] + cycle) & 0b1111
    initial_states['B'] = (initial_states['B'] ^ cycle) & 0b1111
    initial_states['C'] = (initial_states['C'] >> 1) | (cycle << 3)
    initial_states['D'] = (initial_states['D'] << 1) & 0b1111

print(f'Result: {signal_strength}')