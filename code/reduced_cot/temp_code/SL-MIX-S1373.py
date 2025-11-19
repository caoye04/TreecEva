from dataclasses import dataclass
from typing import List
import math

def calculate_parity(value: int) -> int:
    parity = 0
    while value:
        parity ^= value & 1
        value >>= 1
    return parity

def adjust_phase(state: int, parity: int) -> int:
    match parity:
        case 0:
            return state << 1
        case 1:
            return state >> 1 if state > 1 else state
        case _:
            return state

@dataclass
class ParticleMeasurement:
    id: str
    state_value: int
    entanglement_factor: float

measurements = [
    ParticleMeasurement('P001', 42, 1.5),
    ParticleMeasurement('P002', 18, 2.0),
    ParticleMeasurement('P003', 73, 0.8),
    ParticleMeasurement('P004', 29, 1.2)
]

# Sort measurements by state_value in descending order
sorted_measurements = sorted(measurements, key=lambda m: m.state_value, reverse=True)

coherence_index = 0
for i, measurement in enumerate(sorted_measurements):
    base_adjustment = measurement.state_value
    parity = calculate_parity(base_adjustment)
    adjusted_state = adjust_phase(base_adjustment, parity)
    
    if i % 2 == 0:
        coherence_index += adjusted_state * measurement.entanglement_factor
    else:
        coherence_index -= adjusted_state / measurement.entanglement_factor

coherence_index = int(coherence_index)
print(f"Result: {coherence_index}")