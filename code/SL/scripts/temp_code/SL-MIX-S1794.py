from collections import deque
from dataclasses import dataclass
from typing import Dict, List

def xor_gate(a: int, b: int) -> int:
    return a ^ b

def and_gate(a: int, b: int) -> int:
    return a & b

def or_gate(a: int, b: int) -> int:
    return a | b

def float_adjust(value: int, factor: float) -> int:
    return int(value * factor) & 0xFF

gate_functions = {
    'XOR': xor_gate,
    'AND': and_gate,
    'OR': or_gate
}

@dataclass
class LogicGate:
    name: str
    gate_type: str
    inputs: List[str]
    output: str
    processed: bool = False

# Initialize signal values
signals: Dict[str, int] = {
    'A': 0b11001010,
    'B': 0b10110101,
    'C': 0b01101100
}

# Define logic gates
gates = [
    LogicGate('G1', 'XOR', ['A', 'B'], 'D'),
    LogicGate('G2', 'AND', ['B', 'C'], 'E'),
    LogicGate('G3', 'OR', ['D', 'E'], 'F'),
    LogicGate('G4', 'XOR', ['A', 'F'], 'G')
]

# Process gates in topological order
processing_queue = deque(gates)

while processing_queue:
    gate = processing_queue.popleft()
    
    # Check if all inputs are available
    if all(inp in signals for inp in gate.inputs):
        # Calculate output
        input_values = [signals[inp] for inp in gate.inputs]
        if len(input_values) == 2:
            result = gate_functions[gate.gate_type](input_values[0], input_values[1])
        else:
            raise ValueError("Invalid number of inputs")
            
        # Apply floating point adjustment
        adjusted_result = float_adjust(result, 1.5)
        signals[gate.output] = adjusted_result
        gate.processed = True
    else:
        # If inputs not ready, put back in queue
        processing_queue.append(gate)
        
    # Early termination if all gates processed
    if all(g.processed for g in gates):
        break

final_output = signals['G']
print(f"Result: {final_output}")