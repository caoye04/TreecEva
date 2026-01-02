def analyze_pattern(sequence):
    # Irrelevant function: analyzes string patterns (distractor)
    if not sequence:
        return 0
    count = 0
    for char in sequence:
        if char.isupper():
            count += 1
    return count

# Misleading data transformation (red herring)
def transform_input(raw):
    parts = raw.split(',')
    cleaned = [p.strip().lower() for p in parts]
    joined = '|'.join(cleaned)
    return joined.replace('|', ':')

# Unused recursive decoy function
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Another distraction: bit manipulation with no impact
def check_flags(value):
    flag_a = value & 1
    flag_b = (value >> 3) & 1
    flag_c = (value ^ 7) & 1
    return flag_a ^ flag_b | flag_c

# Core logic buried among noise
def process_entries(entries):
    total = 0
    multiplier = 1
    temp_result = 0  # Decoy accumulator

    for entry in entries:
        # Real logic starts here
        length = len(entry)
        if length % 2 == 0:
            total += length * 2
        else:
            total -= length // 2

        # Fake complex processing
        reversed_str = entry[::-1]
        if 'x' in reversed_str:
            temp_result += 5  # Dead path

    # Only this matters
    if total > 10:
        multiplier = 3
    elif total < 0:
        multiplier = -1
    else:
        multiplier = 2

    return total * multiplier

# Main calculation chain
def calculate_final_score(data):
    # Step 1: Extract relevant tokens
    tokens = data['input'].split(';')
    filtered = []
    for token in tokens:
        stripped = token.strip()
        if stripped.startswith('a') or stripped.endswith('z'):
            filtered.append(stripped)
    
    # Step 2: Process filtered list
    intermediate = process_entries(filtered)
    
    # Step 3: Apply adjustment based on metadata
    meta_adjust = len(data['meta'])
    adjusted = intermediate + meta_adjust * 2
n    # Step 4: Check dummy condition (never triggers due to data)
    if any('xyz' in t for t in tokens):
        adjusted = abs(adjusted) * -1  # Dead code path

    # Step 5: Final non-linear adjustment
    if adjusted % 4 == 0:
        final = adjusted * 1.5
    elif adjusted % 3 == 0:
        final = adjusted * 1.2
    else:
        final = adjusted * 1.75  # This will be triggered

    return int(final)  # Ensure integer result

# Simulated user input (real data source)
user_data = {
    'input': 'alpha;betaz;gamma;delta;omegaz',  # Note: betaz, omegaz match filter
    'meta': ['config', 'setting'],              # len=2 → contributes 4
    'debug': True,
    'version': '2.1.0'
}

# Call the main function
final_score = calculate_final_score(user_data)
print(f"Result: {final_score}")