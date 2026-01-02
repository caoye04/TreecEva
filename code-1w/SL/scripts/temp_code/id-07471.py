from collections import defaultdict, Counter
import math

# Simulated sensor data processing with embedded logic chain
def generate_signals(base_freq, duration):
    return [int(math.sin(base_freq * t) * 100) for t in range(1, duration + 1)]

def filter_outliers(data, limit=90):
    # Irrelevant filtering function (not used in final path)
    return [x for x in data if abs(x) <= limit]

def shift_window(sequence, offset=1):
    # Unused transformation — red herring
    return sequence[offset:] + sequence[:offset]

def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def evaluate_stability(readings):
    variance = sum((x - sum(readings)/len(readings))**2 for x in readings) / len(readings)
    return variance < 1500

def extract_signatures(data_stream):
    # Complex but partially irrelevant feature extraction
    signatures = []
    for i in range(0, len(data_stream) - 3, 3):
        block = data_stream[i:i+3]
        sig = (block[0] ^ block[1]) & block[2]  # Bit manipulation red herring
        signatures.append(abs(sig) % 7)
    return signatures

def build_transition_map(seq):
    # Distractor: builds a Markov-like map not used in answer
    trans_map = defaultdict(int)
    for a, b in zip(seq, seq[1:]):
        trans_map[(a % 5, b % 5)] += 1
    return trans_map

def detect_cycles(pattern):
    # Dead-end analysis
    for size in range(2, len(pattern)//2 + 1):
        if len(pattern) % size == 0:
            if all(pattern[i] == pattern[i % size] for i in range(len(pattern))):
                return True
    return False

def analyze_pattern(seq, threshold):
    # Core logic begins here
    segment_a = seq[::2]  # Every other element
    segment_b = seq[1::2]
    
    # Compute statistical profile (some values are distractions)
    avg_a = sum(segment_a) / len(segment_a)
    avg_b = sum(segment_b) / len(segment_b)
    diff_metric = abs(avg_a - avg_b)
    
    # Logical branching chain
    flag_x = diff_metric > 10
    flag_y = (sum(1 for x in seq if x > 0) / len(seq)) > threshold
    flag_z = compute_entropy(seq) > 2.0
    
    # Nested conditional with bit manipulation decoy
    temp_key = 0
    if flag_x:
        temp_key += 100
        if flag_y:
            temp_key += 25
            intermediate = (len(seq) ^ 15) & 255  # Misleading bitwise op
            if flag_z:
                temp_key += 17
                # Real contribution
                cycle_check = any(seq[i] == seq[i-1] for i in range(1, len(seq)))
                if not cycle_check:
                    temp_key += 42
            else:
                temp_key -= 5
        else:
            temp_key *= 2
    else:
        temp_key = 1
    
    # Critical path: simple counting disguised in complexity
    balance = 0
    for val in seq:
        if val > 0:
            balance += 1
        elif val < 0:
            balance -= 1
    
    # Final computation — only this matters
    adjustment = 3 if evaluate_stability(seq) else 0
    final_score = temp_key + balance + adjustment
    
    # Decoy assignment
    diagnostic_flag = "STABLE" if final_score > 100 else "FLUCTUATING"
    
    # ACTUAL TARGET VARIABLE
    final_diagnostic = final_score * 3  # Key transformation
    
    return final_diagnostic

# Orchestration with red herrings
if __name__ == "__main__":
    raw_input = generate_signals(base_freq=0.3, duration=24)
    
    # Unused derived variables — distraction
    cleaned_data = filter_outliers(raw_input, limit=85)
    shifted_buffer = shift_window(raw_input, offset=3)
    signature_features = extract_signatures(raw_input)
    transition_graph = build_transition_map(raw_input)
    cyclic = detect_cycles(signature_features)
    
    # Key data structure — actual input
    logic_sequence = [x // 10 for x in raw_input]  # Scale down
    
    # Irrelevant slicing and lambdas (meets language feature requirement)
    process_fn = lambda arr: [abs(y) for y in arr if y != 0]
    processed = process_fn(logic_sequence[5:18:2])
    
    # Execute main analysis
    final_diagnostic = analyze_pattern(logic_sequence, threshold=0.65)
    
    # OUTPUT REQUIRED FORMAT
    print(f"Result: {final_diagnostic}")