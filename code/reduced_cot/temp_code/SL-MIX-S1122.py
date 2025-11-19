import hashlib
from collections import namedtuple

def compute_field_hash(field_data):
    return int(hashlib.md5(field_data.encode()).hexdigest()[:8], 16)

def extract_header_components(raw_packet):
    tokens = raw_packet.split('|')
    Header = namedtuple('Header', ['src_port', 'dst_port', 'seq_num', 'flags'])
    return Header(int(tokens[0]), int(tokens[1]), int(tokens[2]), tokens[3])

packet_stream = [
    "8080|443|1001|SYN",
    "443|8080|1002|ACK",
    "8080|443|1003|PSH|ACK",
    "443|8080|1004|PSH|ACK",
    "8080|443|1005|FIN|ACK"
]

header_hashes = {i: compute_field_hash(p) for i, p in enumerate(packet_stream)}
base_mask = 0xF0F0F0F0
suspicious_patterns = {}

for idx, packet in enumerate(packet_stream):
    header = extract_header_components(packet)
    port_xor = header.src_port ^ header.dst_port
    seq_and = header.seq_num & base_mask
    flag_hash = compute_field_hash(header.flags)
    
    if (port_xor > 0x1000) and ('PSH' in header.flags):
        pattern_key = (port_xor << 4) | (seq_and >> 24)
        suspicious_patterns[idx] = pattern_key ^ flag_hash
    else:
        suspicious_patterns[idx] = (port_xor & 0xFF) | ((seq_and >> 16) & 0xFF00)

merged_data = {**header_hashes, **{k+10: v for k, v in suspicious_patterns.items()}}
filtered_entries = {k: v for k, v in merged_data.items() if v % 2 == 0}

forensic_score = 0
for key in sorted(filtered_entries.keys()):
    value = filtered_entries[key]
    if (key & 1) == 0:
        forensic_score += (value >> 8) & 0xFFFF
    else:
        forensic_score -= value & 0xFF

print(f"Result: {forensic_score}")