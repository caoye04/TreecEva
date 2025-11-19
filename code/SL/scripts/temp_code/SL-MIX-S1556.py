class SignalNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def build_signal_chain(values):
    if not values:
        return None
    head = SignalNode(values[0])
    current = head
    for val in values[1:]:
        current.next = SignalNode(val)
        current = current.next
    return head

def process_signals(head):
    accumulator = 0
    position = 0
    current = head
    
    while current:
        signal_val = current.value
        
        # Logical operations with conditional branching
        if signal_val == 1 and position % 2 == 0:
            accumulator |= (1 << position)
        elif signal_val == 0 or position % 3 == 0:
            accumulator &= ~(1 << (position // 2))
        else:
            accumulator ^= signal_val
        
        # Switch-case like logic for position-based operations
        op_code = position % 4
        if op_code == 0:  # AND with mask
            mask = 0b1010
            accumulator &= mask
        elif op_code == 1:  # OR with increment
            accumulator |= (position + 1)
        elif op_code == 2:  # XOR with bit-reversed position
            reversed_pos = int(format(position, 'b')[::-1], 2) if position > 0 else 0
            accumulator ^= reversed_pos
        else:  # op_code == 3, NAND simulation
            accumulator = ~(accumulator & (position + 1)) & 0xFFFF
        
        position += 1
        current = current.next
    
    # Final processing with set operations
    active_bits = {i for i in range(16) if (accumulator & (1 << i))}
    even_bits = {i for i in range(0, 16, 2)}
    odd_bits = {i for i in range(1, 16, 2)}
    
    # Complex set operation combining multiple sets
    processed_set = (active_bits.intersection(even_bits)).union(odd_bits.difference(active_bits))
    
    # Convert set to final value using generator expression
    circuit_output = sum(1 << i for i in processed_set)
    
    return circuit_output

# Main execution
signal_values = [1, 0, 1, 1, 0, 1, 0, 1]
signal_chain = build_signal_chain(signal_values)
circuit_output = process_signals(signal_chain)
print(f"Result: {circuit_output}")