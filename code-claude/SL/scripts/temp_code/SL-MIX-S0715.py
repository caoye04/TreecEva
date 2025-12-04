def is_operational(status_code, launch_year):
    # Status code decoder: 1=active, 0=inactive, -1=decommissioned
    # Satellites launched before 2000 have a different status coding
    if launch_year < 2000:
        return status_code > 0
    else:
        return status_code == 1

def calculate_orbit_efficiency(orbit_type, altitude):
    # Higher value means better efficiency
    efficiency_factors = {
        'LEO': 0.85,
        'MEO': 0.72,
        'GEO': 0.95,
        'HEO': 0.68
    }
    
    # Altitude adjustment factor
    if altitude < 500:
        altitude_factor = 0.9
    elif altitude < 2000:
        altitude_factor = 1.0
    else:
        altitude_factor = 0.95
        
    return efficiency_factors.get(orbit_type, 0.5) * altitude_factor

def calculate_active_satellites(satellite_data):
    active_count = 0
    efficiency_sum = 0
    
    for satellite in satellite_data:
        name = satellite['name']
        status = satellite['status']
        year = satellite['launch_year']
        orbit = satellite['orbit_type']
        alt = satellite['altitude']
        
        # Calculate orbit efficiency but we don't use it for active count
        efficiency = calculate_orbit_efficiency(orbit, alt)
        efficiency_sum += efficiency
        
        # Check if satellite is operational
        if is_operational(status, year):
            active_count += 1
    
    # We track efficiency but don't use it in final result
    avg_efficiency = efficiency_sum / len(satellite_data) if satellite_data else 0
    
    return active_count

# Satellite database with status codes, launch years, and orbital parameters
satellite_data = [
    {'name': 'Sentinel-1A', 'status': 1, 'launch_year': 2014, 'orbit_type': 'LEO', 'altitude': 693},
    {'name': 'Galileo-11', 'status': 1, 'launch_year': 2015, 'orbit_type': 'MEO', 'altitude': 23222},
    {'name': 'Landsat-7', 'status': 0, 'launch_year': 1999, 'orbit_type': 'LEO', 'altitude': 705},
    {'name': 'Intelsat-6', 'status': -1, 'launch_year': 1991, 'orbit_type': 'GEO', 'altitude': 35786},
    {'name': 'NOAA-19', 'status': 1, 'launch_year': 2009, 'orbit_type': 'LEO', 'altitude': 870},
    {'name': 'GOES-16', 'status': 1, 'launch_year': 2016, 'orbit_type': 'GEO', 'altitude': 35800},
    {'name': 'Hubble', 'status': 1, 'launch_year': 1990, 'orbit_type': 'LEO', 'altitude': 540}
]

# Calculate the number of active satellites
active_satellites = calculate_active_satellites(satellite_data)

# Tracking additional metrics (not used for final answer)
total_satellites = len(satellite_data)
leo_satellites = sum(1 for sat in satellite_data if sat['orbit_type'] == 'LEO')
geo_satellites = sum(1 for sat in satellite_data if sat['orbit_type'] == 'GEO')

print(f"Result: {active_satellites}")