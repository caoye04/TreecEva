from collections import defaultdict, Counter
import math

# Simulated system telemetry data from a distributed sensor network
timestamps = [1623456780, 1623456789, 1623456795, 1623456805, 1623456810]
sensor_readings = [23.4, 24.1, 22.9, 25.0, 23.8]
packet_loss_rate = [0.01, 0.03, 0.02, 0.05, 0.04]

# Irrelevant preprocessing: frequency analysis (unused later)
frequency_map = defaultdict(int)
for ts in timestamps:
    second = ts % 60
    frequency_map[second // 10] += 1

# Distractor: historical baseline (not used in final calculation)
historical_avg = sum(sensor_readings) / len(sensor_readings)
baseline_deviation = [abs(x - historical_avg) for x in sensor_readings]

# Real processing path begins: timing interval calculation
timing_intervals = []
for i in range(1, len(timestamps)):
    timing_intervals.append(timestamps[i] - timestamps[i-1])

def compute_stability_index(intervals):
    if not intervals:
        return 0.0
    mean_interval = sum(intervals) / len(intervals)
    variance = sum((x - mean_interval) ** 2 for x in intervals) / len(intervals)
    stability = math.exp(-variance / 100.0)
    return round(stability, 6)

# Misleading function: looks important but unused
def calculate_packet_score(loss_rates):
    avg_loss = sum(loss_rates) / len(loss_rates)
    return int((1 - avg_loss) * 100)

# Another red herring: checksum validation (never called)
def validate_checksum(data_list):
    total = 0
    for val in data_list:
        total += int(val * 10) % 7
    return total % 13 == 0

# Core diagnostic logic
class SensorDiagnostics:
    def __init__(self, readings, intervals):
        self.readings = readings
        self.intervals = intervals
        self.anomalies = []

    def detect_outliers(self):
        mean = sum(self.readings) / len(self.readings)
        std_dev = (sum((x - mean) ** 2 for x in self.readings) / len(self.readings)) ** 0.5
        threshold = 1.5 * std_dev
        return [i for i, x in enumerate(self.readings) if abs(x - mean) > threshold]

    def get_consistency_score(self):
        stability = compute_stability_index(self.intervals)
        return stability * 1000  # Scale up for integer emphasis

# Dead code path: simulation override (never triggered)
simulation_mode = False
if simulation_mode:
    timing_intervals = [10, 10, 10, 10]
    sensor_readings = [20.0] * 5

# Initialize diagnostic engine
diag_engine = SensorDiagnostics(sensor_readings, timing_intervals)
anomaly_count = len(diag_engine.detect_outliers())
consistency_score = int(diag_engine.get_consistency_score())

# Decoy data structure (partially misleading)
diagnostics = {
    'raw_intervals': timing_intervals,
    'stability_raw': compute_stability_index(timing_intervals),
    'outlier_indices': diag_engine.anomalies,
    'placeholder_flag': True,
    'metadata': {'version': '2.1', 'nodes': 5}
}

timing_log = defaultdict(list)
for i, interval in enumerate(timing_intervals):
    bucket = f"window_{i//2}"
    timing_log[bucket].append(interval)

# Secondary distractor: frequency count of intervals (not used)
interval_counter = Counter(timing_intervals)

# Critical red herring variable (looks like it's used but isn't)
temp_correction_factor = math.log(consistency_score + 1) if consistency_score > 0 else 0

# Another decoy operation: zipping unrelated sequences
zipped_diagnostics = list(zip(sensor_readings, packet_loss_rate, baseline_deviation))

# Fake aggregation that seems relevant
pseudo_aggregate = 0
for reading, loss in zipped_diagnostics:
    pseudo_aggregate += int(reading / (loss + 0.01))

# Real final computation function
def aggregate_metrics(log_dict, diag_dict):
    # Extract only the lengths of each window
    window_weights = [len(log_dict[key]) for key in sorted(log_dict.keys())]
    base_score = diag_dict['stability_raw'] * 1000
    
    # Apply weighted adjustment based on window distribution
    adjustment = 0
    for i, w in enumerate(window_weights):
        adjustment += w * (i + 1) * 10
    
    # Final deterministic transformation
    result = int(base_score) + adjustment - anomaly_count * 5
    return result

# Execute critical statement
final_diagnostic = aggregate_metrics(timing_log, diagnostics)

# Print final result as required
print(f"Target result: {final_diagnostic}")