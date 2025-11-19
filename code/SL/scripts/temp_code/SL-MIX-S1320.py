import heapq
from collections import defaultdict

def find_harmonic_sequences(frequencies, threshold=2):
    # State definitions
    STATE_IDLE = 0
    STATE_FIRST = 1
    STATE_SECOND = 2
    
    state = STATE_IDLE
    diff = 0
    harmonic_sequences_count = 0
    i = 0
    
    while i < len(frequencies):
        if state == STATE_IDLE:
            if i + 1 < len(frequencies):
                state = STATE_FIRST
                i += 1
            else:
                break
        elif state == STATE_FIRST:
            if i + 1 < len(frequencies):
                diff = frequencies[i] - frequencies[i-1]
                if diff > threshold:
                    state = STATE_SECOND
                    i += 1
                else:
                    state = STATE_IDLE
                    i += 1
            else:
                break
        elif state == STATE_SECOND:
            if i + 1 < len(frequencies):
                current_diff = frequencies[i] - frequencies[i-1]
                if current_diff == diff:
                    harmonic_sequences_count += 1
                    # Skip ahead to avoid counting overlapping sequences
                    i += 2
                    state = STATE_IDLE
                else:
                    state = STATE_IDLE
                    i -= 1
            else:
                break
    return harmonic_sequences_count

# Audio sample frequencies
audio_frequencies = [10, 15, 20, 22, 27, 32, 40, 45, 50, 60, 68, 76, 80, 90, 100]

# Process the frequencies
harmonic_sequences_count = find_harmonic_sequences(audio_frequencies)

# Additional processing using combinatorics
freq_set = set(audio_frequencies)
combinations_count = sum(1 for f in audio_frequencies if f+10 in freq_set and f+20 in freq_set)

# Final adjustment using heap
heap = list(freq_set)
heapq.heapify(heap)
top_elements = [heapq.heappop(heap) for _ in range(min(5, len(heap)))]

# Update count based on top elements
if len(top_elements) >= 3:
    mean_top = sum(top_elements[:3]) / 3
    if mean_top > 50:
        harmonic_sequences_count += 1

print(f"Result: {harmonic_sequences_count}")