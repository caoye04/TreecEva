from math import log2, exp
from functools import reduce
from collections import namedtuple

def transform_key_stage(key_segment):
    return (key_segment << 2) ^ 0xF0

def validate_checksum(fragment, target):
    if fragment == 0:
        return target == 0
    if target < 0:
        return False
    return validate_checksum(fragment >> 1, target - (fragment & 1))

def process_encryption_key(base_key):
    segments = [base_key >> i & 0xFF for i in range(0, 24, 8)]
    transformed = list(map(transform_key_stage, segments))
    aggregated = reduce(lambda x, y: x | y, transformed)
    
    operation_code = aggregated % 4
    checksum_component = 0
    
    match operation_code:
        case 0:
            checksum_component = int(exp(log2(aggregated)))
        case 1:
            checksum_component = aggregated & 0xAA
        case 2:
            checksum_component = aggregated ^ 0xCC
        case 3:
            checksum_component = aggregated | 0xF0
    
    sorted_bits = sorted([int(b) for b in bin(checksum_component)[2:]])
    bit_sum = sum(sorted_bits)
    
    if validate_checksum(checksum_component, bit_sum):
        return checksum_component
    else:
        return checksum_component ^ 0xFF

EncryptionSession = namedtuple('EncryptionSession', ['session_id', 'base_key'])
session = EncryptionSession(session_id=12345, base_key=0x123456)
final_checksum = process_encryption_key(session.base_key)
print(f"Result: {final_checksum}")