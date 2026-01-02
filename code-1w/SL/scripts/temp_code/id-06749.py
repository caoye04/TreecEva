def analyze_text_patterns(text):
    # Distractor: Advanced string analysis with irrelevant metrics
    char_freq = {}
    for char in text:
        if char.isalpha():
            char_freq[char.lower()] = char_freq.get(char.lower(), 0) + 1
    entropy = 0.0
    total = sum(char_freq.values())
    for count in char_freq.values():
        p = count / total
        entropy -= p * __import__('math').log2(p)
    return entropy

def preprocess_signals(signal_list):
    # Distractor: Signal processing red herring
    transformed = []
    for i, val in enumerate(signal_list):
        if i % 2 == 0:
            transformed.append(val * 1.5)
        else:
            transformed.append(val ** 0.5)
    return [x for x in transformed if x > 0]

def compute_checksum(data):
    # Seemingly important but unused function (dead code path)
    checksum = 0
    for item in data:
        if isinstance(item, int):
            checksum ^= item
    return checksum

def evaluate_performance(metrics):
    # Core logic buried in distractions
    base_points = 0
    penalty = 0
    
    # Relevant data transformation using zip and enumerate
    for idx, (name, value) in enumerate(zip(['latency', 'throughput', 'error_rate'], metrics)):
        if idx == 0:  # latency
            base_points += int(100 - value)
        elif idx == 1:  # throughput
            base_points += int(value // 10)
        elif idx == 2:  # error_rate
            penalty += int(value * 100)
    
    # Bit manipulation that actually matters
    adjusted = (base_points << 2) ^ penalty
    
    # Irrelevant conditional block (misleading intermediate result)
    if adjusted > 500:
        normalized = adjusted / 1.75
    else:
        normalized = adjusted  # This path is taken
    
    # Final adjustment based on string property of a label (use of string method)
    label = "PERFORMANCE_LOG_2024"
    modifier = len(label.split('_'))  # Returns 3
    
    final_score = normalized - modifier  # Key computation
    
    # Dead code: never executed due to structure
    redundant_check = [x for x in range(10) if x > 20]
    
    return final_score

# Simulate execution context
raw_text = "Optimizing compiler pipelines for next-gen AI workloads."
entropy_value = analyze_text_patterns(raw_text)
signal_input = [4, 9, 16, 25]
processed_signal = preprocess_signals(signal_input)

# Actual input to the core function
metric_data = [23.0, 145.0, 0.12]  # latency, throughput, error_rate
final_score = evaluate_performance(metric_data)
print(f"Result: {final_score}")