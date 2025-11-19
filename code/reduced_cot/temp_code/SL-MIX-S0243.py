import heapq
import base64

def compute_hash(s):
    return hash(s) % 1000

def process_packets():
    # Encoded packet data with priorities
    encoded_packets = [
        ("SGVsbG8=", 5),
        ("V29ybGQ=", 3),
        ("UGl6emE=", 7)
    ]
    
    # Initialize processing structures
    packet_queue = []
    priority_heap = []
    processed_scores = set()
    
    # Step 1: Decode and enqueue packets
    for enc_data, base_priority in encoded_packets:
        decoded_data = base64.b64decode(enc_data).decode('utf-8')
        hash_val = compute_hash(decoded_data)
        adjusted_priority = base_priority * 10 + (hash_val & 0xF)
        packet_queue.append((adjusted_priority, decoded_data))
    
    # Step 2: Push to min-heap
    for priority, data in packet_queue:
        heapq.heappush(priority_heap, (priority, data))
    
    # Step 3: Process packets from heap
    total_score = 0
    while priority_heap:
        priority, data = heapq.heappop(priority_heap)
        if len(data) > 4 and priority not in processed_scores:
            score = priority ^ len(data)
            if score > 10 and (score % 2 == 0 or score < 50):
                total_score += score
                processed_scores.add(priority)
    
    # Final calculation
    final_priority_score = total_score & 0xFF
    return final_priority_score

result = process_packets()
print(f"Result: {result}")