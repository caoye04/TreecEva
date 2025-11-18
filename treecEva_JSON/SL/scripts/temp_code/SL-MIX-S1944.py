import heapq
import numpy as np

def encode_shift(message):
    return ''.join(chr((ord(c) + 5) % 256) for c in message)

class SignalDecoder:
    def __init__(self, key_matrix):
        self.key_matrix = np.array(key_matrix)
        self.signal_heap = []
    
    def process(self, encoded_msg):
        # Step 1: Decode with key matrix
        msg_vector = [ord(c) for c in encoded_msg]
        decoded_vector = np.dot(self.key_matrix, msg_vector).tolist()
        
        # Step 2: Apply heap-based priority correction
        for i, val in enumerate(decoded_vector):
            heapq.heappush(self.signal_heap, (val % 100, i, val))
        
        # Step 3: Reconstruct signal
        reconstructed = []
        while self.signal_heap:
            _, _, value = heapq.heappop(self.signal_heap)
            reconstructed.append(chr(int(value) % 256))
        
        return ''.join(reconstructed)

# Protocol setup
transformation_key = [[1, 2], [3, 4]]
decoder = SignalDecoder(transformation_key)

# Encoded transmission
transmission = encode_shift('AI')

# Decoding process
intermediate_result = decoder.process(transmission)

# Final transformation
final_map = {c: str(ord(c)*2) for c in intermediate_result}
aggregated_value = sum(int(v) for v in final_map.values())

decoded_signal = aggregated_value // 4
print(f'Result: {decoded_signal}')