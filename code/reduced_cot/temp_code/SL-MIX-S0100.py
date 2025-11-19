from collections import deque
import re

def packet_analyzer():
    # Initialize sliding window and tracking variables
    packet_window = deque(maxlen=5)
    duplicate_tracker = {}
    congestion_window_size = 10
    
    # Packet data: (sequence_number, payload_size)
    packet_stream = [
        (1001, 512), (1002, 256), (1003, 1024), (1004, 128),
        (1005, 64), (1003, 512), (1006, 2048), (1007, 32),
        (1008, 4096), (1009, 16), (1010, 8192), (1008, 1024)
    ]
    
    # Process each packet
    for seq_num, payload in packet_stream:
        # Check if sequence number already exists in current window
        is_duplicate = seq_num in [p[0] for p in packet_window]
        
        # Update duplicate tracker
        if is_duplicate:
            duplicate_tracker[seq_num] = duplicate_tracker.get(seq_num, 0) + 1
        
        # Add packet to sliding window
        packet_window.append((seq_num, payload))
        
        # Adjust congestion window based on packet characteristics
        if payload > 1000:
            congestion_window_size = congestion_window_size - 1 if congestion_window_size > 1 else 1
        elif is_duplicate:
            congestion_window_size = congestion_window_size + 1 if congestion_window_size < 20 else 20
        else:
            # Apply regex pattern matching to sequence number for special handling
            seq_str = str(seq_num)
            if re.match(r'.*[02468]$', seq_str):  # Even ending digit
                congestion_window_size = congestion_window_size + 1
            else:
                congestion_window_size = congestion_window_size - 1
    
    return congestion_window_size

# Execute the analyzer
final_congestion_window = packet_analyzer()
print(f"Result: {final_congestion_window}")