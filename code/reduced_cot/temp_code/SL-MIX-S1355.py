from functools import reduce

def signal_hash(s):
    return reduce(lambda acc, c: (acc * 31 + ord(c)) & 0xFFFFFFFF, s, 0)

class TransmissionOptimizer:
    def __init__(self):
        self.visited_states = set()
    
    def encode_segment(self, segment, depth=0):
        if depth > 4 or signal_hash(segment) in self.visited_states:
            return segment[::-1]  # Backtrack with reversed segment
        
        self.visited_states.add(signal_hash(segment))
        
        # Greedy optimization: find best split point
        best_split = 0
        best_score = float('inf')
        
        for i in range(1, len(segment)):
            left_part = segment[:i]
            right_part = segment[i:]
            score = abs(signal_hash(left_part) - signal_hash(right_part))
            if score < best_score:
                best_score = score
                best_split = i
        
        if best_split == 0:
            return segment
        
        left_encoded = self.encode_segment(segment[:best_split], depth+1)
        right_encoded = self.encode_segment(segment[best_split:], depth+1)
        
        # Combine with special encoding
        combined = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(left_encoded.ljust(len(right_encoded), '\x00'), right_encoded.ljust(len(left_encoded), '\x00')))
        return combined

# Main processing
optimizer = TransmissionOptimizer()
test_signal = "COMMUNICATION"
processed_segments = []

for i in range(1, len(test_signal)-1):
    segment = test_signal[max(0, i-3):min(len(test_signal), i+4)]
    encoded = optimizer.encode_segment(segment)
    processed_segments.append(encoded)

# Final aggregation step
aggregated = ''.join(processed_segments)
transform_map = {c: chr((ord(c) * 17 + 23) % 97 + 32) for c in set(aggregated)}
final_encoded = ''.join(transform_map[c] for c in aggregated)
final_encoded_length = len(final_encoded)

print(f"Result: {final_encoded_length}")