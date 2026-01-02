import math

# Simulated sensor data processing system for environmental monitoring
def collect_readings():
    raw_signals = [127, 255, 192, 64, 80, 240, 168]
    timestamps = [1634567890 + i*30 for i in range(len(raw_signals))]
    return list(zip(timestamps, raw_signals))

# Irrelevant helper - dead path
def deprecated_filter(x):
    return x > 100 and x % 2 == 0

# Decoy transformation
irrelevant_shift = lambda a: [i ^ 255 for i in a if i < 200]

# Core transformation pipeline
def transform_signal(signal_pair):
    timestamp, reading = signal_pair
    
    # Bit manipulation for noise filtering
    cleaned = reading & 0x7F  # Mask high bit
    adjusted = (cleaned << 1) ^ 0x55  # Shift and XOR scramble
    
    # Conditional amplification
    if adjusted < 100:
        adjusted *= 2
    elif adjusted > 200:
        adjusted = int(math.sqrt(adjusted) * 8)
    else:
        adjusted = adjusted // 3 * 2
        
    # Embedded diagnostic checksum (misleading intermediate)
    temp_checksum = sum([adjusted & 0xF, (adjusted >> 4) & 0xF]) * 17
    
    # Actual payload extraction
    payload = (adjusted ^ 0xAA) & 0xFF
    
    # Return structured tuple with red herring fields
    return {
        'time': timestamp,
        'value': payload,
        'flags': (payload >> 6) & 0x3,
        'debug_meta': temp_checksum,  # Distractor
        'spare_field': None
    }

# Data aggregation with enumerate distraction
def aggregate_diagnostics(data_list):
    results = []
    cumulative = 0
    
    # Use of enumerate with irrelevant index tracking
    for idx, record in enumerate(data_list):
        val = record['value']
        flag = record['flags']
        
        # Real logic
        if flag == 2 or val % 7 == 0:
            cumulative += val * 3
        elif val > 150:
            cumulative += val // 4
        else:
            cumulative -= val // 10
        
        # Fake pattern detection (dead code)
        if idx > 0 and record['debug_meta'] > data_list[idx-1]['debug_meta']:
            pass  # No-op distractor
            
        results.append(cumulative)
        
    return results

# Higher-order function with lambda red herring
def process_metrics(dataset, cfg):
    # Irrelevant statistical lambdas
    outlier_fn = lambda x, limit: x > limit * 1.5
    trend_lambda = lambda seq: sum(seq[i] < seq[i+1] for i in range(len(seq)-1))
    
    # Real processing steps
    aggregated = aggregate_diagnostics(dataset)
    base_score = sum(aggregated) % 10000
    
    # Complex conditional using bitwise and arithmetic
    modifier = 0
    if len(aggregated) > 5:
        last_val = aggregated[-1]
        penultimate = aggregated[-2]
        diff = abs(last_val - penultimate)
        
        # Multi-step logic chain
        if diff & 1:
            modifier += 127
        if diff > 200:
            modifier ^= 85
        if len(aggregated) & 1:
            modifier -= 43
        
        # Final adjustment
        modifier = (modifier ^ (diff & 0xFF)) + 10
    else:
        modifier = 50
        
    # Critical answer computation
    final_diagnostic = base_score + modifier
    
    # Unused complex structure to distract
    detailed_report = {
        'raw_series': aggregated,
        'anomalies': list(filter(lambda x: x > 1000, aggregated)),
        'growth_trend': trend_lambda(aggregated),
        'meta_flag': outlier_fn(base_score, 500)
    }
    
    return final_diagnostic

# Configuration with misleading parameters
class Config:
    def __init__(self):
        self.threshold = 95
        self.window_size = 7
        self.enable_legacy = False
        self.debug_mode = True  # Looks important but unused

cfg = Config()

# Main execution flow
if __name__ == "__main__":
    # Step 1: Collect data
    raw_data = collect_readings()
    
    # Step 2: Transform each signal
    transformed_data = [transform_signal(pair) for pair in raw_data]
    
    # Step 3: Process metrics to get final diagnostic
    final_diagnostic = process_metrics(transformed_data, cfg)
    
    # Output result
    print(f"Result: {final_diagnostic}")