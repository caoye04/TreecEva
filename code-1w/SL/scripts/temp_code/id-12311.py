def transform_input(raw_string):
    cleaned = raw_string.strip().lower()
    parts = cleaned.split(',')
    numeric_parts = []
    for part in parts:
        stripped = part.strip()
        if stripped.isdigit():
            numeric_parts.append(int(stripped))
        elif stripped.replace('.', '').isdigit():
            numeric_parts.append(float(stripped))
    return numeric_parts

raw_data = "  10, 3.5, 7, abc, 2.0, xyz, 8  "
temp_result = transform_input(raw_data)

# Misleading intermediate processing with dead-end branches
interim_values = []
sum_check = 0
for val in temp_result:
    if isinstance(val, int) and val % 2 == 0:
        sum_check += val * 1.5
    elif isinstance(val, float):
        sum_check -= val // 1
    interim_values.append(val ** 2)  # Computation not directly used later

# Actual relevant data extraction
relevant_numbers = [x for x in temp_result if isinstance(x, int)]

# Simulated signal mask using bitwise operations (some distraction)
def apply_mask(seq, key=3):
    masked = []
    for i, num in enumerate(seq):
        noise = (i ^ key) & 7  # XOR and AND to generate red herring values
        masked.append(num & (~noise))  # Actual effect is minimal due to masking pattern
    return masked

masked_ints = apply_mask(relevant_numbers)

# Secondary transformation with string-based control
status_flag = "ACTIVE"
flag_code = status_flag.lower().replace("active", "1").replace("inactive", "0")

if flag_code == "1":
    processed_data = []
    for i, val in enumerate(masked_ints):
        shift_factor = len(interim_values) % 3  # Distracting use of earlier list
        adjusted = val >> shift_factor
        # Injecting case conversion as per language-specific requirement
        control_str = f"Mode{shift_factor}".upper()
        control_val = len(control_str) if 'A' in control_str else 0
        processed_data.append(adjusted + control_val)
else:
    processed_data = [0]

# Final scoring logic
def calculate_final_score(data):
    base = sum(data)
    # Extra distraction: unused helper
    def unused_helper(x):
        return x * x + 2*x + 1
    
    bonus = 0
    if len(data) > 3:
        bonus += 5
    if all(d > 0 for d in data):
        bonus += 10
    
    penalty = 0
    dummy_tracker = []
    for item in data:
        if item < 5:
            penalty += 1
        dummy_tracker.append(item % 3)  # Dead-end tracking
    
    return base + bonus - penalty

final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")