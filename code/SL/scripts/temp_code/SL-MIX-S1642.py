def generate_mask_table():
    return {i: (i << 2) ^ 0xF for i in range(16)}

def process_headers(headers, mask_table):
    processed = []
    for h in headers:
        masked = h & 0xFF
        transformed = masked ^ mask_table[masked & 0xF]
        processed.append(transformed)
    return processed

def binary_search_verification(data, target):
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) >> 1
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

@staticmethod
def compute_checksum(components):
    checksum = 0
    for component in components:
        checksum ^= component
        checksum = (checksum << 1) | (checksum >> 7)
    return checksum & 0xFF

packet_headers = [0x12, 0x34, 0x56, 0x78, 0x9A, 0xBC, 0xDE, 0xF0]
mask_lookup = generate_mask_table()
processed_headers = process_headers(packet_headers, mask_lookup)
sorted_processed = sorted(processed_headers)
target_value = sorted_processed[3]
verification_index = binary_search_verification(sorted_processed, target_value)
final_verification_code = compute_checksum([target_value, verification_index, len(sorted_processed)])
print(f'Result: {final_verification_code}')