import itertools

def analyze_signal(samples, threshold=50):
    """Irrelevant signal processing function with dead logic."""
    filtered = [s for s in samples if s > threshold]
    normalized = [f / max(filtered) * 100 for f in filtered] if filtered else []
    avg_norm = sum(normalized) / len(normalized) if normalized else 0
    return avg_norm

def calculate_entropy(data):
    """Misleading entropy calculation - not used in final result."""
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not actual entropy, just decoy
    return round(entropy, 4)

def transform_sequence(seq):
    """Applies multiple transformations, only one path matters."""
    a = [x * 2 + 1 for x in seq]
    b = [x for x in a if x % 3 == 0]
    c = [x ^ 5 for x in b]  # Bit manipulation red herring
    d = sorted(c, reverse=True)
    return d[:len(d)//2] if d else []

def compute_chain_value(start):
    """Real computation hidden among distractions."""
    val = start
    for i in range(3):
        if i % 2 == 0:
            val = (val * 3) + 2
        else:
            val = (val + 5) * 2  # This branch never reached due to range(3)
    return val

def evaluate_performance(metrics):
    base = 0
    temp_result = 0
    
    # Relevant logic starts here — nested conditionals and controlled flow
    if len(metrics) > 2:
        chunk = metrics[1:4]
        shifted = [(x >> 1) + (x << 2) for x in chunk]  # Bit shifts look important

        # Actual key transformation
        processed = []
        for idx, num in enumerate(shifted):
            if idx == 0:
                processed.append(num // 4)
            elif idx == 1:
                processed.append(num // 5)
            else:
                processed.append(num // 6)

        aggregate = sum(processed)

        # Critical dependency on itertools cycle (required feature)
        cycle = itertools.cycle([2, -1])
        adjusted = 0
        for val in processed:
            adjusted += val * next(cycle)

        # Real answer depends on this conditional chain
        if aggregate > 100:
            base = 750
        elif aggregate > 50:
            base = 420
        else:
            base = 180

        temp_result = base + adjusted

    else:
        temp_result = 999  # Dead path

    # Decoy assignments and fake dependencies
    checksum = sum(metrics) % 17
    validation_code = ''.join(chr((m % 26) + 97) for m in metrics[:3])
    debug_trace = f'DIAG:{checksum}:{validation_code}'  # Unused string

    # Only this line matters
    final = temp_result + compute_chain_value(7)

    # More irrelevant data structures
    audit_log = {
        'entries': [],
        'status': 'pending',
        'meta': {'version': '2.1', 'mode': 'diagnostic'}
    }
    
    return final

# Irrelevant sample data
signal_samples = [45, 67, 89, 23, 55]
unused_metrics = [12, 15, 10, 8]
dummy_sequence = [4, 8, 12]

# Key input that feeds into real logic
metric_data = [20, 30, 25]  # Used in evaluate_performance

# Call the critical function
final_score = evaluate_performance(metric_data)

# Print result as required
print(f"Target result: {final_score}")