def process_results(data, limit):
    count_valid = 0
    total_sum = 0
    for entry in data:
        if not entry.strip():
            continue
        value = int(entry.split(':')[1])
        flag = int(entry.split(':')[2])
        if value > limit and (flag & 1) == 1:
            total_sum += value ^ 3
            count_valid += 1
    return total_sum // count_valid if count_valid > 0 else 0

# Simulated sensor readings with format: id:value:flag
raw_data = [
    "s1:45:3",
    "s2:60:2",  
    "s3:52:1",
    "s4:0:1",
    "s5:77:3"
]
threshold = 50
temp_offset = 2.5
buffer_size = 1024
final_score = process_results(raw_data, threshold)
print(f"Result: {final_score}")