def preprocess_entries(raw_entries):
    cleaned = [e.strip().lower() for e in raw_entries if len(e) > 0]
    filtered = [c for c in cleaned if 'error' not in c]
    return filtered

raw_data = [' DATA1 ', '', 'ERROR: corrupt', ' data2', 'data3 ', 'ERROR', ' data4']

# Irrelevant transformation chain
buffer_cache = [item.upper() for item in raw_data if 'corrupt' not in item]
temp_checksum = sum(len(entry) for entry in buffer_cache) % 17
dummy_matrix = [[i + j for j in range(3)] for i in range(3)]

processed_data = preprocess_entries(raw_data)

# Simulate feature extraction with distractions
feature_flags = {}
for idx, entry in enumerate(processed_data):
    feature_flags[f'f_{idx}'] = len(entry) % 3 == 0

extraction_log = {k: v for k, v in feature_flags.items() if v}

# Secondary irrelevant computation
shadow_accumulator = 0
for i in range(len(dummy_matrix)):
    for j in range(len(dummy_matrix[i])):
        shadow_accumulator += dummy_matrix[i][j] * (i + 1)

# Core logic embedded in distraction
base_values = [len(item) for item in processed_data]
adjusted_values = [v * 2 if k in extraction_log else v for k, v in enumerate(base_values)]

# Misleading normalization step
normalization_factor = max(adjusted_values) if adjusted_values else 1
decoy_normalized = [round(x / normalization_factor, 4) for x in adjusted_values]

# Actual scoring function
def calculate_final_score(data_list):
    score = 0
    for i, entry in enumerate(data_list):
        if 'data' in entry:
            score += len(entry) * (i + 1)
    return score

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")