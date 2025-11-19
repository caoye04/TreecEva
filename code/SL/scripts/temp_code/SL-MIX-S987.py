from dataclasses import dataclass
from typing import NamedTuple
import math

class RideMetrics(NamedTuple):
    capacity: int
    cycle_time: float
    queue_length: int

def calculate_loading_factor(pattern_type: str, guests: int) -> float:
    factors = {
        'standard': 1.0,
        'express': 1.3,
        'family': 0.8,
        'vip': 1.5
    }
    base_factor = factors.get(pattern_type, 1.0)
    return base_factor * (1 + math.log(guests + 1) / 10)

def get_ride_metrics(ride_id: int) -> RideMetrics:
    metrics_db = {
        101: RideMetrics(24, 180.5, 85),
        102: RideMetrics(16, 150.0, 120),
        103: RideMetrics(32, 200.0, 65)
    }
    return metrics_db[ride_id]

# Main processing
ride_cycles = [101, 102, 103]
efficiency_scores = {}

for cycle in ride_cycles:
    metrics = get_ride_metrics(cycle)
    
    # Determine loading pattern based on queue length
    if metrics.queue_length < 70:
        pattern = 'express'
    elif metrics.queue_length < 100:
        pattern = 'standard'
    else:
        pattern = 'family'
    
    loading_factor = calculate_loading_factor(pattern, metrics.queue_length)
    throughput = (metrics.capacity / metrics.cycle_time) * 3600  # per hour
    efficiency = throughput * loading_factor
    efficiency_scores[cycle] = round(efficiency, 2)

# Apply park-wide adjustments
peak_hour_bonus = {101: 1.1, 102: 1.05, 103: 1.15}
adjusted_scores = {rid: eff * peak_hour_bonus[rid] for rid, eff in efficiency_scores.items()}

# Calculate final efficiency score
base_score = sum(adjusted_scores.values())
complexity_penalty = len(ride_cycles) * 2.5
final_efficiency_score = int(base_score - complexity_penalty)

print(f"Result: {final_efficiency_score}")