from collections import deque
import statistics

def process_packets():
    packet_queue = deque([120, 85, 200, 95, 160, 75, 180])
    mask = 0xF0  # 240 in decimal
    
    # Apply bitwise masking to each packet size
    masked_packets = [pkt & mask for pkt in packet_queue]
    
    # Rotate queue left by 2 positions
    packet_queue.rotate(-2)
    
    # Calculate mean of masked packets
    avg_masked = statistics.mean(masked_packets)
    
    # XOR the first and last elements of rotated queue
    xor_result = packet_queue[0] ^ packet_queue[-1]
    
    # Apply right shift to xor_result by 2 bits
    shifted_xor = xor_result >> 2
    
    # Compute anomaly score as the product of average and shifted XOR, minus the variance of original queue
    variance_original = statistics.variance(packet_queue)
    anomaly_score = int(avg_masked * shifted_xor - variance_original)
    
    return anomaly_score

anomaly_score = process_packets()
print(f"Result: {anomaly_score}")