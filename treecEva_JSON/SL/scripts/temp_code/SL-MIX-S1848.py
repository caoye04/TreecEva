import heapq
import math

def process_signal_peaks():
    samples = [42, 18, 73, 29, 55, 37, 64, 12, 88, 5]
    peak_queue = []
    
    # Process each sample to determine peak priorities
    for idx, sample in enumerate(samples):
        # Priority calculation using bitwise operations and logarithm
        bit_mask = (sample & 0xF) << 2
        log_factor = int(math.log2(sample + 1)) if sample > 0 else 0
        priority = (bit_mask ^ (log_factor << 3)) & 0xFF
        
        # Push to heap (min-heap, so negate for max-heap behavior)
        heapq.heappush(peak_queue, (-priority, idx, sample))
    
    # Extract top 3 peaks and calculate final score
    top_priorities = []
    for _ in range(min(3, len(peak_queue))):
        neg_priority, pos, val = heapq.heappop(peak_queue)
        top_priorities.append(-neg_priority)
    
    # Apply exponential adjustment and XOR combination
    adjusted_scores = [p ^ int(math.exp(i)) for i, p in enumerate(top_priorities)]
    final_priority_score = adjusted_scores[0]
    for score in adjusted_scores[1:]:
        final_priority_score ^= score
    
    return final_priority_score

final_priority_score = process_signal_peaks()
print(f"Result: {final_priority_score}")