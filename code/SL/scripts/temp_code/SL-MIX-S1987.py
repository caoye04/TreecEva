import math
from functools import reduce

def compute_frequency_weight(band_index, attenuation_map):
    base_freq = 2 ** band_index
    attenuation = attenuation_map.get(band_index, 1.0)
    return math.log(base_freq) * math.exp(-attenuation)

def aggregate_responses(band_weights, att_map):
    responses = {}
    for band_idx in band_weights:
        if band_idx % 2 == 0 and band_idx > 0:
            weight_factor = band_weights[band_idx]
            raw_response = compute_frequency_weight(band_idx, att_map)
            responses[band_idx] = raw_response * weight_factor
    return responses

def calculate_system_score(freq_responses):
    positive_responses = {k: v for k, v in freq_responses.items() if v > 0}
    if not positive_responses:
        return 0
    product = reduce(lambda x, y: x * y, positive_responses.values(), 1)
    return math.log10(abs(product)) if product != 0 else 0

# System configuration
attenuation_profile = {2: 0.5, 4: 0.3, 6: 0.7, 8: 0.2}
band_coefficients = {0: 1.0, 2: 1.5, 4: 2.0, 6: 1.2, 8: 1.8}

# Process signals
weighted_responses = aggregate_responses(band_coefficients, attenuation_profile)
processed_response_score = calculate_system_score(weighted_responses)
print(f"Result: {round(processed_response_score, 6)}")