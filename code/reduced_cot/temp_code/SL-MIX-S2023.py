import heapq
import re

def decode_packet(encoded_str, key_seq):
    decoded_chars = []
    for i, char in enumerate(encoded_str):
        key = key_seq[i % len(key_seq)]
        decoded_char = chr(ord(char) ^ key)
        decoded_chars.append(decoded_char)
    return ''.join(decoded_chars)

def calculate_severity(command):
    score = 0
    if re.search(r'(exec|spawn|fork)', command):
        score += 50
    if re.search(r'/bin/sh', command):
        score += 30
    if ';' in command or '|' in command:
        score += 20
    return score

encoded_packets = ['xqlks', '{sp', '~uyqj']
key_sequence = [3, 7, 11]
decoded_commands = [decode_packet(p, key_sequence) for p in encoded_packets]
severity_heap = []
for cmd in decoded_commands:
    severity = calculate_severity(cmd)
    heapq.heappush(severity_heap, (-severity, cmd))

top_threat_level = -severity_heap[0][0] if severity_heap else 0
print(f"Result: {top_threat_level}")