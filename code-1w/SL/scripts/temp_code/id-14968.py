from collections import Counter

def process_sequence(seq):
    filtered = [x for x in seq if x % 3 == 0]
    shifted = [x >> 1 for x in filtered]
    count_map = Counter(shifted)
    most_common_val, _ = count_map.most_common(1)[0]
    return most_common_val * 2

data = [12, 9, 15, 7, 18, 21, 13, 6]
extra_data = [x for x in data if x > 10]  # Irrelevant distractor
flag = len(extra_data) > 3  # Irrelevant boolean
result = process_sequence(data)
print(f"Result: {result}")