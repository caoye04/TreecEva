from heapq import heappush, heappop

def process_packets():
    # Packet processing state machine
    states = {
        'INIT': lambda x: (x * 17) % 256,
        'TRANSFORM': lambda x: x ^ 0xAA,
        'VALIDATE': lambda x: (x & 0xF0) | ((x << 2) & 0x0F)
    }
    
    # Processing queue with initial packets
    packet_queue = [123, 45, 67, 89, 202]
    verification_heap = []
    
    # State transitions
    state_sequence = ['INIT', 'TRANSFORM', 'VALIDATE']
    
    while packet_queue:
        current_packet = packet_queue.pop(0)
        
        # Apply state transformations
        for state in state_sequence:
            if current_packet > 200 and state == 'TRANSFORM':
                # Early return for high-value packets
                current_packet = states[state](current_packet) & 0x7F
                break
            current_packet = states[state](current_packet)
        
        # Push transformed packet to verification heap
        heappush(verification_heap, current_packet)
    
    # Calculate final verification score
    final_verification_score = 0
    while verification_heap:
        value = heappop(verification_heap)
        final_verification_score = (final_verification_score + value) % 1000
    
    return final_verification_score

# Dictionary comprehension for system configuration
system_config = {f'param_{i}': (i**2) % 17 for i in range(1, 6)}

# Merge with default settings
default_settings = {'buffer_size': 1024, 'timeout': 30}
system_config = {**default_settings, **system_config}

# Execute packet processing
final_verification_score = process_packets()
print(f"Result: {final_verification_score}")