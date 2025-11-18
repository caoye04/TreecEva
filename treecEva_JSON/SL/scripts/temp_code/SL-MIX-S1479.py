from collections import defaultdict
from functools import reduce
import math

def decode_custom_base64(encoded_str):
    char_to_bin = {chr(i): i - ord('A') for i in range(ord('A'), ord('Z') + 1)}
    char_to_bin.update({chr(i).lower(): i - ord('a') + 26 for i in range(ord('a'), ord('z') + 1)})
    char_to_bin.update({str(i): i + 52 for i in range(10)})
    char_to_bin['+'] = 62
    char_to_bin['/'] = 63
    
    bits = ''
    for c in encoded_str:
        if c in char_to_bin:
            bin_val = bin(char_to_bin[c])[2:].zfill(6)
            bits += bin_val
    return bits

def parse_packets(bits):
    packets = []
    i = 0
    while i < len(bits):
        if len(bits) - i < 6:
            break
        packet_type = int(bits[i:i+3], 2)
        payload_len = int(bits[i+3:i+6], 2)
        i += 6
        if i + payload_len * 4 > len(bits):
            break
        payload = bits[i:i+payload_len*4]
        packets.append((packet_type, payload))
        i += payload_len * 4
    return packets

encoded_log = "Tk9UMDQxNzI5Mzg="
decoded_bits = decode_custom_base64(encoded_log)
packets = parse_packets(decoded_bits)

freq_counter = defaultdict(int)
for ptype, payload in packets:
    value = int(payload, 2) if payload else 0
    freq_counter[ptype] += 1
    freq_counter[value % 10] += 1

checksum_valid = sum(k*v for k,v in freq_counter.items() if isinstance(k, int)) % 97 == 42

risk_values = list(map(lambda x: x**2 if x < 5 else math.log(x+1), freq_counter.values()))
aggregated_risk = reduce(lambda a,b: a+b, risk_values, 0)

threat_score = aggregated_risk if checksum_valid else -1

print(f"Result: {int(threat_score)}")