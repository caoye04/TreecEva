def analyze_pattern(sequence, threshold):
    count_map = {}
    temp_result = 0
    for idx, char in enumerate(sequence):
        if char not in count_map:
            count_map[char] = 0
        count_map[char] += 1
        
    # Irrelevant character frequency tracking (distractor)
    freq_list = [count_map[k] for k in sorted(count_map)]
    median_freq = freq_list[len(freq_list)//2] if freq_list else 0

    running_sum = 0
    for i, ch in enumerate(sequence):
        running_sum += ord(ch) * (i + 1)
    
    base_value = running_sum % threshold
    return base_value

# Misleading preprocessing
raw_data = "abracadabra"
data_parts = raw_data.split('a')
filtered_parts = [p for p in data_parts if len(p) > 0]

# Core logic disguised among distractions
checksum = 0
for part in filtered_parts:
    for c in part:
        checksum ^= ord(c)  # Bitwise XOR as red herring

pivot_key = len(filtered_parts) * 2
base_tally = analyze_pattern(raw_data, pivot_key)

# Secondary analysis with partial relevance
length_flag = 1 if len(raw_data) % 2 == 0 else -1
aux_counter = 0
for a, b in zip(raw_data, raw_data[1:]):
    if a < b:
        aux_counter += 1

# Real adjustment logic
penalty_offset = (aux_counter * length_flag) % 7

# Critical function
def calculate_adjustment(total, offset):
    intermediate = total + offset ** 2
    if intermediate > 50:
        intermediate -= 23
    return (intermediate * 3) // 4

final_score = calculate_adjustment(base_tally, penalty_offset)

# Print required result
print(f"Target result: {final_score}")