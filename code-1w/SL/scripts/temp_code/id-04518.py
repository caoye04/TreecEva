from collections import defaultdict, Counter

# Simulated sensor data ingestion and processing pipeline
def ingest_sensor_stream(raw_packets):
    parsed = []
    for packet in raw_packets:
        if len(packet) < 5:
            continue
        node_id = packet[0] << 2
        temp_raw = (packet[1] << 4) | (packet[2] >> 4)
        hum_raw = ((packet[2] & 0x0F) << 8) | packet[3]
        checksum = packet[4]
        computed = (node_id ^ temp_raw ^ hum_raw) & 0xFF
        if computed == checksum:
            parsed.append((node_id, temp_raw / 10.0, hum_raw / 10.0))
    return parsed

def filter_outliers(data_seq, limit=50.0):
    # Irrelevant filtering for humidity outliers (distractor)
    return [x for x in data_seq if x[2] <= limit]

def compute_rolling_average(values, window=3):
    smoothed = []
    for i in range(len(values)):
        start = max(0, i - window + 1)
        smoothed.append(sum(values[start:i+1]) / (i - start + 1))
    return smoothed

def generate_synthetic_data(baseline, count):
    # Dead code path — never called
    return [baseline * (1 + i * 0.01) for i in range(count)]

def analyze_trend_pattern(seq):
    trend_score = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1]:
            trend_score += 1
        elif seq[i] < seq[i-1]:
            trend_score -= 1
    return abs(trend_score)

def extract_diagnostic_flags(sensor_data):
    flags = defaultdict(int)
    temperature_readings = [x[1] for x in sensor_data]
    humidity_readings = [x[2] for x in sensor_data]
    
    avg_temp = sum(temperature_readings) / len(temperature_readings)
    avg_hum = sum(humidity_readings) / len(humidity_readings)
    
    # Distractor: complex but unused humidity trend analysis
    hum_trend = analyze_trend_pattern(humidity_readings)
    flags['high_variability'] = int(len([x for x in temperature_readings if abs(x - avg_temp) > 5]) > 3)
    flags['temp_spike'] = int(any(t > 35 for t in temperature_readings))
    flags['stable_zone'] = int(all(20 <= t <= 25 for t in temperature_readings))
    
    # Real signal buried in noise
    flags['critical_phase'] = int(avg_temp > 30 and avg_hum < 40)
    
    # More red herrings
    entropy_marker = 0
    for t in temperature_readings:
        entropy_marker ^= int(t * 10) & 0x7
    flags['entropy_flag'] = entropy_marker
    
    return flags, temperature_readings

def transform_keys(data_list):
    # Unused transformation function (decoy)
    return [{'id': d[0], 't': d[1], 'h': d[2]} for d in data_list]

def build_threshold_map(config_level):
    # Misleading configuration map with irrelevant entries
    base = {
        't_low': 18, 't_high': 32, 'h_critical': 60,
        'noise_floor': 0.5, 'gain_factor': 1.2,
        'decay_rate': 0.85, 'window_size': 7
    }
    if config_level > 2:
        base['t_alert'] = 35
        base['h_sensitive'] = 45
    return base

def aggregate_node_metrics(clean_data):
    node_stats = defaultdict(lambda: {'temps': [], 'hums': []})
    for node_id, temp, hum in clean_data:
        node_stats[node_id]['temps'].append(temp)
        node_stats[node_id]['hums'].append(hum)
    
    summary = {}
    for nid, metrics in node_stats.items():
        t_vals = metrics['temps']
        h_vals = metrics['hums']
        summary[nid] = {
            'avg_t': round(sum(t_vals) / len(t_vals), 2),
            'avg_h': round(sum(h_vals) / len(h_vals), 2),
            'range_t': max(t_vals) - min(t_vals),
            'stability': len(t_vals) >= 5 and max(t_vals) - min(t_vals) <= 3
        }
    return summary

def calculate_composite_index(entries):
    # Complex-looking but unused scoring index (red herring)
    index = 0.0
    for e in entries:
        index += e['avg_t'] * 0.7 - e['avg_h'] * 0.3
    return round(index / len(entries), 3) if entries else 0

def process_metrics(aggregated_data, threshold_map):
    diagnostics = []
    for node_id, stats in aggregated_data.items():
        t_avg = stats['avg_t']
        h_avg = stats['avg_h']
        
        # Core logic hidden among distractions
        score = 0
        if t_avg > threshold_map['t_high']:
            score += 3
        if h_avg < 30:
            score += 2  # Dry condition bonus
        if stats['range_t'] > 8:
            score += 1
        if stats['stability']:
            score -= 2  # Stable systems penalized in this metric (non-intuitive)
        
        # Irrelevant bitwise manipulation (looks important)
        encoded = (int(t_avg) << 3) ^ (int(h_avg) & 0xFF)
        encoded = (encoded ^ (encoded >> 4)) & 0x3FF
        
        diagnostics.append(score)
    
    # Final computation buried at the end
    total = sum(diagnostics)
    adjustment = len([d for d in diagnostics if d >= 3])
    final_diagnostic = total * 7 - adjustment * 3
    
    # Decoy output line (never reached in logic flow)
    # final_diagnostic = int(calculate_composite_index(aggregated_data) * 10)
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Simulated raw byte packets from IoT sensors
    raw_data_stream = [
        [0x1A, 0x32, 0x45, 0x67, 0x7C],
        [0x1A, 0x33, 0x44, 0x81, 0x7E],
        [0x1A, 0x35, 0x43, 0x90, 0x7D],
        [0x1A, 0x34, 0x42, 0x95, 0x7B],
        [0x1A, 0x36, 0x41, 0xA0, 0x7A],
        [0x2B, 0x41, 0x23, 0x45, 0x67],
        [0x2B, 0x42, 0x22, 0x50, 0x68],
        [0x2B, 0x43, 0x21, 0x55, 0x69],
        [0x2B, 0x42, 0x20, 0x60, 0x6A],
        [0x2B, 0x41, 0x19, 0x65, 0x6B],
        [0x2B, 0x39, 0x18, 0x70, 0x6C],
        [0x2B, 0x38, 0x17, 0x75, 0x6D]
    ]

    # Step 1: Ingest and validate packets
    parsed_data = ingest_sensor_stream(raw_data_stream)
    
    # Step 2: Filter invalid humidity readings (mostly irrelevant)
    filtered_data = filter_outliers(parsed_data, limit=50.0)
    
    # Step 3: Extract diagnostic flags (only some fields used later)
    flag_map, temp_series = extract_diagnostic_flags(filtered_data)
    
    # Step 4: Aggregate by node
    aggregated_data = aggregate_node_metrics(filtered_data)
    
    # Step 5: Build threshold configuration (contains decoy values)
    threshold_map = build_threshold_map(config_level=3)
    
    # Step 6: Process metrics to compute final diagnostic score
    final_diagnostic = process_metrics(aggregated_data, threshold_map)
    
    # Output result
    print(f"Result: {final_diagnostic}")