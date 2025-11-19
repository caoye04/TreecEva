from collections import deque
import base64

def hex_to_int(hex_str):
    return int(hex_str, 16)

def decode_log(encoded_chunk):
    decoded_bytes = base64.b64decode(encoded_chunk)
    return decoded_bytes.decode('utf-8')

# Encoded log entries
log_entries = ["Njg2Zjc0NmY=", "NzI2ZTY1NjY=", "NmU2ZTY1NzI="]

# Initialize data structures
frequency_map = {}
anomaly_queue = deque()
modulus_base = 13

for idx, entry in enumerate(log_entries):
    try:
        # Stage 1: Base64 decode
        decoded_str = decode_log(entry)
        
        # Stage 2: Hex to integer conversion
        numeric_val = hex_to_int(decoded_str)
        
        # Stage 3: Modular reduction
        reduced_val = numeric_val % modulus_base
        
        # Stage 4: Frequency tracking
        if reduced_val in frequency_map:
            frequency_map[reduced_val] += 1
        else:
            frequency_map[reduced_val] = 1
            
        # Stage 5: Anomaly detection (values appearing once are anomalies)
        if frequency_map[reduced_val] == 1:
            anomaly_queue.append(reduced_val)
    except Exception as e:
        pass  # Skip malformed entries

# Calculate anomaly score
anomaly_score = 0
while anomaly_queue:
    val = anomaly_queue.popleft()
    if frequency_map[val] == 1:
        anomaly_score += val * 2

print(f"Result: {anomaly_score}")