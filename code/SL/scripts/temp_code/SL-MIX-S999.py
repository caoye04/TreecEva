from collections import defaultdict, deque
import itertools

def tokenize_packet(packet_str):
    return list(packet_str)

def transform_token(token):
    if token.isalpha():
        return chr((ord(token.lower()) - ord('a') + 5) % 26 + ord('a'))
    elif token.isdigit():
        return str((int(token) * 3) % 10)
    else:
        return token

def process_layer(tokens):
    stack = []
    queue = deque()
    for t in tokens:
        transformed = transform_token(t)
        if transformed in 'aeiou':
            stack.append(transformed)
        else:
            queue.append(transformed)
    return stack, queue

def calculate_anomaly_freq(stack, queue):
    freq_map = defaultdict(int)
    while stack:
        freq_map[stack.pop()] += 1
    while queue:
        freq_map[queue.popleft()] += 2
    return freq_map

def compute_security_score(freq_map):
    score = 0
    for char, count in freq_map.items():
        if char in 'aeiou':
            score += count * 3
        else:
            score += count * 2
    return score

# Main execution
packet_data = "SecNet-v2.3!Encrypted"
token_stream = tokenize_packet(packet_data)
processed_stack, processed_queue = process_layer(token_stream)
anomaly_frequencies = calculate_anomaly_freq(processed_stack, processed_queue)
final_security_score = compute_security_score(anomaly_frequencies)
print(f"Result: {final_security_score}")