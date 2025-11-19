from collections import deque

class SignalProcessor:
    def __init__(self):
        self.signal_stack = []
        self.propagation_queue = deque()
        self.gate_operations = {
            'AND': lambda x, y: x & y,
            'OR': lambda x, y: x | y,
            'XOR': lambda x, y: x ^ y,
            'NOT': lambda x: ~x & 0xFF
        }
    
    def process_circuit(self):
        # Initialize with base signals
        signals = [0b11001010, 0b10110101, 0b01101100]
        
        # Load signals onto stack
        for signal in signals:
            self.signal_stack.append(signal)
        
        # Process gate operations
        operations = ['AND', 'OR', 'XOR']
        for op in operations:
            if len(self.signal_stack) >= 2 and op in self.gate_operations:
                b = self.signal_stack.pop()
                a = self.signal_stack.pop()
                result = self.gate_operations[op](a, b)
                self.signal_stack.append(result)
                self.propagation_queue.append(result)
        
        # Apply NOT to remaining signal if exists
        if self.signal_stack and len(self.signal_stack) > 0:
            signal = self.signal_stack.pop()
            if signal:
                inverted = self.gate_operations['NOT'](signal)
                self.signal_stack.append(inverted)
                self.propagation_queue.appendleft(inverted)
        
        # Calculate final signal strength
        final_signal_strength = 0
        while self.propagation_queue:
            signal = self.propagation_queue.popleft()
            final_signal_strength = (final_signal_strength + signal) % 256
        
        return final_signal_strength

circuit = SignalProcessor()
final_signal_strength = circuit.process_circuit()
print(f"Result: {final_signal_strength}")