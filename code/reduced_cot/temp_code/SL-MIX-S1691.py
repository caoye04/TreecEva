from collections import deque

def simulate_circuit():
    # Gate behavior lookup using lambda functions
    gate_behaviors = {
        'AND': lambda x, y: x & y,
        'OR': lambda x, y: x | y,
        'XOR': lambda x, y: x ^ y,
        'NOT': lambda x: ~x & 0xFF  # 8-bit NOT
    }
    
    # Signal queue (FIFO)
    signals = deque([17, 42, 13, 89])
    
    # Processing stack (LIFO)
    stack = []
    
    # Process signals through gates
    while signals:
        current_signal = signals.popleft()
        # Apply a transformation based on signal value
        transformed = (current_signal * 3 + 7) % 256
        stack.append(transformed)
        
        # When stack has two elements, apply a gate operation
        if len(stack) >= 2:
            b = stack.pop()
            a = stack.pop()
            # Select gate based on a's parity and b's magnitude
            gate = 'AND' if a % 2 == 0 else ('OR' if b > 100 else 'XOR')
            result = gate_behaviors[gate](a, b)
            stack.append(result)
    
    # Finalize with a NOT operation if the stack isn't empty
    final_value = stack.pop() if stack else 0
    circuit_output = gate_behaviors['NOT'](final_value) if final_value != 0 else 0
    
    # Adjust for negative values using modular arithmetic
    circuit_output = circuit_output % 256 if circuit_output < 0 else circuit_output
    
    return circuit_output

# Execute simulation
result = simulate_circuit()
print(f"Result: {result}")