import math

def analyze_orbital_phases(phases):
    # Irrelevant analysis function (dead code path)
    total = 0
    for p in phases:
        total += math.sin(p) ** 2
    return total

def validate_checksum(data):
    # Misleading checksum computation (distractor)
    checksum = 0
    for i, val in enumerate(data.values()):
        checksum ^= (i + 1) * hash(str(val)) % 17
    return checksum == 5

def transform_coordinates(coords):
    # Unused transformation logic (red herring)
    x, y, z = coords
    r = math.sqrt(x**2 + y**2 + z**2)
    theta = math.atan2(y, x)
    phi = math.acos(z / r) if r != 0 else 0
    return (r, theta, phi)

def compute_harmonic_sequence(n):
    # Decoy mathematical function with no impact on result
    if n <= 0:
        return []
    seq = [1]
    for i in range(1, n):
        seq.append(seq[-1] + 1 / (i + 1))
    return seq

def evaluate_resonance_ratio(primary, secondary):
    # Seemingly important physics calculation (misleading intermediate)
    ratio = primary / secondary
    return abs(ratio - round(ratio)) < 0.05

def calculate_stellar_flux(data):
    # Core relevant logic (buried among distractions)
    base_intensity = data['luminosity'] / (4 * math.pi * data['distance']**2)
    
    # Conditional expression usage (required feature)
    modifier = 1.5 if data['atmosphere']['opacity'] > 0.7 else 0.8
    
    # Dictionary operations (required feature)
    elements = data['atmosphere']['elements']
    metallicity_factor = sum([
        elements.get('Fe', 0),
        elements.get('Si', 0) * 0.7,
        elements.get('Mg', 0) * 0.5
    ]) + 1  # Avoid zero
    
    # Modular arithmetic and combinatorics hint
    cycle_count = data['orbital_period'] // 100
    phase_shift = (data['orbital_phase'] + cycle_count) % 8
    
    # Complex nested logic with interdependencies (3-4 levels)
    if data['stellar_class'] in ['G', 'K']:
        if data['magnetic_activity']:
            activity_mod = 0.9 - (data['sunspot_coverage'] * 0.005)
            if activity_mod < 0.7:
                activity_mod = 0.7
        else:
            activity_mod = 1.0
        
        if phase_shift > 4:
            diurnal_mod = 0.85
        else:
            diurnal_mod = 1.0
        
        # Key composite calculation
        flux = base_intensity * modifier * metallicity_factor * activity_mod * diurnal_mod
        
        # Final adjustment using bit manipulation (unexpected twist)
        flux_int = int(flux)
        masked = flux_int ^ 0b101010  # Bitwise XOR distraction that affects result
        flux = float(masked) + (flux - int(flux))  # Preserve fractional part
    else:
        flux = base_intensity * 0.5  # Not taken, but looks plausible
    
    return flux

# Main execution block
if __name__ == '__main__':
    # Large dictionary with many fields (mix of relevant and irrelevant)
    system_data = {
        'name': 'TRAPPIST-1e Analog',
        'stellar_class': 'K',
        'luminosity': 384400,  # In W
        'distance': 149600,      # In km (approx 1 AU)
        'orbital_period': 612,   # In days
        'orbital_phase': 6,      # Phase index
        'magnetic_activity': True,
        'sunspot_coverage': 15,  # Percentage
        'atmosphere': {
            'opacity': 0.85,
            'pressure': 101.3,
            'temperature': 288,
            'elements': {
                'N2': 78,
                'O2': 21,
                'CO2': 0.04,
                'Ar': 0.93,
                'Fe': 0.0015,
                'Si': 0.0008,
                'Mg': 0.0006,
                'Ne': 0.001
            }
        },
        'moons': ['moon_alpha', 'moon_beta'],  # Irrelevant list
        'discovery_year': 2023,
        'spectral_data': [0.1, 0.4, 0.7, 1.2, 0.9],  # Unused sensor readings
        'calibration_offset': 0.0034  # Distractor constant
    }

    # Dead code paths and irrelevant computations (intervention)
    _ = analyze_orbital_phases([0.1, 1.2, 2.3, 3.4])
    _ = compute_harmonic_sequence(5)
    _ = transform_coordinates((1000, 2000, 3000))
    _ = validate_checksum(system_data)

    # Critical execution point
    final_flux = calculate_stellar_flux(system_data)
    
    # Print result as required
    print(f"Result: {final_flux}")