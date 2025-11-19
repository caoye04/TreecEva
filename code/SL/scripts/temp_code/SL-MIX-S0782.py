from dataclasses import dataclass
from typing import List

@dataclass
class ZoneStatus:
    name: str
    capacity: int
    current_occupancy: int
    maintenance_flag: bool

# Zone configurations
zones = [
    ZoneStatus('thrill_mountain', 150, 142, False),
    ZoneStatus('aquatic_cove', 200, 189, True),
    ZoneStatus('space_station', 100, 95, False)
]

# Visitor request data
visitor_requests = [25, 18, 33, 12, 45, 8, 22]
weather_factor = 0.85  # Reduced capacity due to weather
allowed_entries = 0
safety_protocol_active = True
max_concurrent_visitors = 600

current_total_occupancy = sum(zone.current_occupancy for zone in zones)

for i, request_size in enumerate(visitor_requests):
    # Early return if safety protocol limits reached
    if current_total_occupancy >= max_concurrent_visitors:
        break
    
    # Short-circuit evaluation for quick rejection
    if request_size <= 0 or (safety_protocol_active and request_size > 30):
        continue
    
    # Ternary operator for adjusted request size
    adjusted_request = int(request_size * weather_factor) if weather_factor < 1.0 else request_size
    
    # Process zone availability using switch-like logic
    available_capacity = 0
    for zone in zones:
        # Skip maintenance zones
        if zone.maintenance_flag:
            continue
        
        # Calculate available space in each zone
        zone_available = max(0, int(zone.capacity * weather_factor) - zone.current_occupancy)
        available_capacity += zone_available
    
    # Determine if request can be fulfilled
    if adjusted_request <= available_capacity:
        # Update occupancy
        current_total_occupancy += adjusted_request
        allowed_entries += 1 if adjusted_request > 15 else 0
    elif i >= 4:  # After 5th request, try partial fulfillment
        partial_entry = min(adjusted_request, available_capacity)
        if partial_entry > 0:
            current_total_occupancy += partial_entry
            allowed_entries += 1

# Final adjustment based on total occupancy
allowed_entries = allowed_entries * 2 if current_total_occupancy < 500 else allowed_entries

print(f"Result: {allowed_entries}")