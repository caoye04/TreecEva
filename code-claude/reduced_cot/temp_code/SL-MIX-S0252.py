from collections import Counter, defaultdict
import math

def satellite_tracking_system():
    # Satellite orbital data (altitude in km, operational status)
    satellite_data = [
        ("GPS-32", 20180, True),
        ("Sentinel-5", 824, True),
        ("Hubble", 547, True),
        ("Starlink-1095", 550, False),
        ("ISS", 408, True),
        ("Landsat-9", 705, True),
        ("GOES-16", 35786, True),
        ("Starlink-2311", 550, True),
        ("Iridium-126", 780, False),
        ("NOAA-20", 828, True)
    ]
    
    # Atmospheric drag coefficients (irrelevant for counting)
    drag_factors = defaultdict(lambda: 0.0)
    drag_factors.update({
        "LEO": 0.12,     # Low Earth Orbit
        "MEO": 0.05,     # Medium Earth Orbit
        "GEO": 0.001     # Geostationary Orbit
    })
    
    # Orbital classification function (distracting)
    def classify_orbit(altitude):
        if altitude < 500:
            return "LEO-Low"
        elif altitude < 1000:
            return "LEO-High"
        elif altitude < 25000:
            return "MEO"
        else:
            return "GEO"
    
    # Signal strength calculation (misleading)
    def calculate_signal_strength(altitude, is_active):
        if not is_active:
            return 0
        base_strength = 100 * (1 / math.log(altitude + 100))
        return round(base_strength, 2)
    
    # Track orbital perturbations (irrelevant)
    orbital_perturbations = Counter()
    for sat in satellite_data:
        orbit_class = classify_orbit(sat[1])
        orbital_perturbations[orbit_class] += int(sat[1] % 10)
    
    # Calculate transmission latency (misleading)
    transmission_latency = lambda alt: 2 * alt / 299792.458  # Speed of light in km/s
    latency_values = [transmission_latency(sat[1]) for sat in satellite_data]
    avg_latency = sum(latency_values) / len(latency_values)
    
    # Operational satellite counter (relevant)
    geo_sats = sum(1 for sat in satellite_data if sat[2] and classify_orbit(sat[1]) == "GEO")
    meo_sats = sum(1 for sat in satellite_data if sat[2] and classify_orbit(sat[1]) == "MEO")
    leo_sats = sum(1 for sat in satellite_data if sat[2] and (classify_orbit(sat[1]).startswith("LEO")))
    
    # Signal quality assessment (distracting)
    signal_quality = defaultdict(list)
    for sat in satellite_data:
        signal = calculate_signal_strength(sat[1], sat[2])
        orbit = classify_orbit(sat[1])
        signal_quality[orbit].append(signal)
    
    # Potential satellite collisions (misleading)
    collision_risk = 0
    for i, sat1 in enumerate(satellite_data):
        for sat2 in satellite_data[i+1:]:
            if abs(sat1[1] - sat2[1]) < 10 and sat1[2] and sat2[2]:
                collision_risk += 1
    
    # Redundant calculation (distracting)
    backup_count = len([s for s in satellite_data if s[2]]) - 1
    
    # This is the actual result we want
    active_satellites = sum(1 for sat in satellite_data if sat[2])
    
    # Misleading final calculation
    total_system_reliability = ((geo_sats * 0.99) + (meo_sats * 0.95) + (leo_sats * 0.9)) / active_satellites
    
    return active_satellites

# Simulate telemetry processing (irrelevant)
telemetry_packets = ["0x1F3A", "0x2E4B", "0x3F5C"]
telemetry_checksum = sum(int(packet, 16) for packet in telemetry_packets)

# Weather conditions affecting signal (distracting)
weather_impact = {
    "clear": 1.0,
    "cloudy": 0.9,
    "rain": 0.7,
    "storm": 0.4
}
current_weather = "rain"

# Execute tracking system
active_satellites = satellite_tracking_system()
print(f"Result: {active_satellites}")