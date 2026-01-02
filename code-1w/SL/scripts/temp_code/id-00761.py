import itertools

# Simulated biomedical signal processing system with decoy computations

def analyze_waveform(signal):
    # Irrelevant transformation (dead-end function)
    return [x * 0.9 for x in signal if x > 50]

def compute_entropy(data):
    # Unused complexity - distractor
    total = sum(data)
    return sum(-(x/total) * (x/total) for x in data if x > 0)

def generate_phase_shift(elements, shift):
    # Decoy utility - never used in critical path
    rotated = elements[-shift:] + elements[:-shift]
    return rotated

def extract_features(dataset):
    # Real but obscured logic: computes alternating sum and filters peaks
    filtered = [x for x in dataset if x % 2 == 1]  # keep only odd values
    return filtered[::2]  # every other odd number

def derive_key(signal_chunk):
    # Core calculation buried in noise
    a = sum(x**2 for x in signal_chunk) // 100
    b = len([x for x in signal_chunk if x > 30])
    c = signal_chunk[len(signal_chunk)//2]  # middle element
    return (a + b) // c

def process_metrics(signature, reference):
    # Critical function - contains key logic steps
    
    # Step 1: slice relevant window
    segment = signature[4:11]
    
    # Step 2: set difference to filter anomalies
    ref_set = set(reference)
    seg_set = set(segment)
    anomalies = seg_set - ref_set
    
    # Step 3: use itertools to generate pairs
    pairs = list(itertools.combinations(anomalies, 2))
    
    # Step 4: compute pairwise XOR products
    xor_products = [abs(a ^ b) for a, b in pairs]
    
    # Step 5: extract features from products
    features = extract_features(xor_products)
    
    # Step 6: derive intermediate metric
    metric = derive_key(features)
    
    # Step 7: apply conditional adjustment
    adjustment = 7 if len(features) > 3 else 11
    
    # Step 8: final computation
    result = metric * adjustment
    
    # Distractor variables below (irrelevant)
    temp_scale = [x * 1.05 for x in signature]
    norm = sum(x**2 for x in temp_scale)**0.5
    phase_data = generate_phase_shift(temp_scale, 3)
    entropy = compute_entropy(phase_data)
    waveform_analysis = analyze_waveform(phase_data)
    
    return result

# Input data - fixed and deterministic
baseline_readings = [12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
health_signature = [10, 14, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]

# Execution point of interest
final_diagnostic = process_metrics(health_signature, baseline_readings)

print(f"Result: {final_diagnostic}")