import hashlib

def custom_hash(token):
    return sum(ord(c) << (i % 4) for i, c in enumerate(token)) & 0xFF

def process_headers(headers):
    base_hash = 0x5C
    field_contributions = {k: custom_hash(v) for k, v in headers.items()}
    merged_data = {**headers, **{'meta': 'verification'}}
    
    for key in sorted(field_contributions.keys()):
        contribution = field_contributions[key]
        if key.startswith('opt'):
            base_hash ^= contribution >> 2
        elif len(key) > 4:
            base_hash = (base_hash + (contribution << 1)) & 0xFF
        else:
            base_hash |= contribution
    
    meta_hash = custom_hash(merged_data['meta'])
    final_checksum = (base_hash ^ meta_hash) % 128
    return final_checksum

packet_headers = {
    'src': '192.168.1.1',
    'dst': '10.0.0.1',
    'proto': 'TCP',
    'opt_flags': 'SYN,ACK',
    'opt_win': '8192'
}

final_checksum = process_headers(packet_headers)
print(f"Result: {final_checksum}")