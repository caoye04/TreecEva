import math

def process_sequence(materials, steps):
    # Irrelevant transformation chain with decoy outputs
    temp_log = [math.log(x + 1) for x in materials if x > 5]
    shift_key = sum(temp_log[:3]) if len(temp_log) >= 3 else 0
    encrypted = [(x * 7 + int(shift_key)) % 64 for x in materials]
    
    # Core relevant processing (buried among distractions)
    transformed = []
    for i, val in enumerate(materials):
        if i % 2 == 0:
            transformed.append(val ** 0.5)
        else:
            transformed.append(val / (i + 1))
    
    # Dead path: never used result
    outlier_detect = [x for x in transformed if x > 10]
    compression_factor = len(transformed) / (len(outlier_detect) + 1)
    
    # Actual signal path
    result = []
    for _ in range(steps):
        result = [x * 0.9 for x in transformed]
        transformed = result
    
    return result

def validate_purity(seq):
    # Mix of string-based validation and numeric filtering
    status_flags = ['pass', 'check', 'pass', 'fail']
    critical_flag = status_flags[len(seq) % 4]
    
    # String method distraction
    flag_summary = ''.join(sorted(status_flags)).upper().replace('CHECK', 'VERIFY')
    summary_hash = sum(ord(c) for c in flag_summary) % 100
    
    # Real computation buried here
    base_score = sum(x for x in seq if x > 0.5)
    penalty = 0
    for x in seq:
        if x < 0.1:
            penalty += 1
    
    # Decoy logic that looks important but isn't connected to output
    calibration_data = "ref_01,ref_02,ref_03"
    refs = calibration_data.split(',')
    ref_lengths = [len(r) for r in refs]
    avg_ref_len = sum(ref_lengths) / len(ref_lengths)
    
    # Actual score calculation
    purity_score = (base_score * 100) - (penalty * 50)
    return int(purity_score)

def analyze_composition(data):
    # Unused function - red herring
    return sum(x ** 2 for x in data) / len(data)

def main():
    # Input initialization
    raw_materials = [16, 25, 36, 49, 64, 81]
    refinement_steps = 3
    
    # Irrelevant preprocessing
    normalized = [x / max(raw_materials) for x in raw_materials]
    histogram_bins = [0]*10
    for x in normalized:
        idx = min(int(x * 10), 9)
        histogram_bins[idx] += 1
    
    # Key execution point
    filtration_score = validate_purity(process_sequence(raw_materials, refinement_steps))
    
    # More distractions
    report_id = "FRX-" + str(sum(raw_materials) % 1000).zfill(3)
    audit_trail = report_id.replace('FRX', 'LOG').split('-')
    verification_code = hash(tuple(audit_trail)) % 10000
    
    # Final irrelevant conditional
    if verification_code % 2 == 0:
        final_status = "APPROVED"
    else:
        final_status = "PENDING"
    
    print(f"Result: {filtration_score}")

if __name__ == "__main__":
    main()