def compress_sequence(data):
    if not data:
        return []
    compressed = [data[0]]
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i-1]:
            count += 1
        else:
            if count > 1:
                compressed.append(str(count))
            compressed.append(data[i])
            count = 1
    if count > 1:
        compressed.append(str(count))
    return compressed

original_data = 'aaabbcdddddff'
compressed_data = compress_sequence(original_data)
redundancy_check = sum(1 for c in original_data if c == 'd')
temp_buffer = [x for x in compressed_data if x.isdigit()]
compression_ratio = len(original_data) / len(compressed_data)
print(f"Result: {compression_ratio}")