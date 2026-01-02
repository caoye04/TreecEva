import math

# Simulated agricultural block data with noise and irrelevant metrics
def generate_block_data():
    raw_data = [
        {'id': 'A1', 'moisture': 0.68, 'ph': 6.4, 'temp': 22.1, 'weed_density': 3, 'yield_potential': 85},
        {'id': 'A2', 'moisture': 0.71, 'ph': 6.8, 'temp': 23.5, 'weed_density': 6, 'yield_potential': 70},
        {'id': 'A3', 'moisture': 0.78, 'ph': 5.9, 'temp': 20.0, 'weed_density': 2, 'yield_potential': 90},
        {'id': 'A4', 'moisture': 0.63, 'ph': 6.2, 'temp': 24.3, 'weed_density': 8, 'yield_potential': 60},
        {'id': 'A5', 'moisture': 0.75, 'ph': 6.7, 'temp': 21.8, 'weed_density': 1, 'yield_potential': 95}
    ]
    return raw_data

# Irrelevant preprocessing: converts block IDs to binary hash (unused later)
def encode_block_id(block_id):
    return bin(hash(block_id) % 128)[2:].zfill(7)

# Distractor function: calculates unused 'field_entropy' based on weed distribution
def calculate_field_entropy(blocks):
    densities = [b['weed_density'] for b in blocks]
    total = sum(densities)
    if total == 0:
        return 0.0
    entropy = 0.0
    for d in densities:
        p = d / total
        if p > 0:
            entropy -= p * math.log(p)
    return round(entropy, 4)

# Real processing: filters blocks by optimal moisture and pH
# Moisture in [0.65, 0.75], pH in [6.3, 6.8]
def filter_optimal_blocks(blocks):
    filtered = []
    for b in blocks:
        m, p = b['moisture'], b['ph']
        if 0.65 <= m <= 0.75 and 6.3 <= p <= 6.8:
            filtered.append(b)
    return filtered

# Secondary filter: remove high weed density (>4 weeds/m²)
def remove_weedy_blocks(blocks):
    return [b for b in blocks if b['weed_density'] <= 4]

# Distractor: computes average temperature deviation from ideal (unused)
def temp_deviation_score(blocks):
    ideal = 22.0
    devs = [abs(b['temp'] - ideal) for b in blocks]
    return sum(devs) / len(devs) if devs else 0

# Core transformation: applies yield boost based on low weed density and temp
boost_factor = lambda wd, t: 1.1 if wd <= 2 and 21 <= t <= 23 else 1.0

# Process block: applies boost and adjusts yield_potential
# Also includes red herring string manipulation on block ID
def process_block(block):
    # Irrelevant string transformation
    transformed_id = ''.join(sorted(block['id'])) + '_proc'
    boosted_yield = block['yield_potential'] * boost_factor(block['weed_density'], block['temp'])
    # Add computed flag (used only partially)
    block['adjusted_yield'] = round(boosted_yield, 2)
    block['processed_id'] = transformed_id
    return block

# Orchestrate real processing chain
def process_blocks(blocks):
    step1 = filter_optimal_blocks(blocks)
    step2 = remove_weedy_blocks(step1)  # Further reduces set
    processed = [process_block(b) for b in step2]
    return processed

# Fake aggregation: uses set to find unique temp values (distractor)
def get_unique_temps(blocks):
    return sorted(set(round(b['temp'], 1) for b in blocks))

# Another decoy: finds max-min moisture range among selected (unused)
def moisture_range(blocks):
    moists = [b['moisture'] for b in blocks]
    return (max(moists) - min(moists)) if moists else 0.0

# Actual optimization: maximizes yield by selecting top 2 blocks by adjusted_yield
def optimize_harvest(blocks):
    if len(blocks) == 0:
        return 0
    # Sort descending by adjusted_yield
    sorted_blocks = sorted(blocks, key=lambda x: x['adjusted_yield'], reverse=True)
    top_two = sorted_blocks[:2]
    # Final yield is average of top two yields multiplied by block count multiplier
    avg_yield = sum(b['adjusted_yield'] for b in top_two) / len(top_two)
    multiplier = len(blocks)  # depends on how many passed all filters
    return round(avg_yield * multiplier, 4)

# --- Entry point ---
if __name__ == '__main__':
    
    # Generate base data
    all_blocks = generate_block_data()
    
    # Compute irrelevant metrics (distraction level 1)
    field_entropy = calculate_field_entropy(all_blocks)
    unique_temperatures = get_unique_temps(all_blocks)
    moisture_span = moisture_range(all_blocks)
    temp_dev = temp_deviation_score(all_blocks)
    
    # Encode all block IDs (dead code path - results unused)
    encoded_ids = {b['id']: encode_block_id(b['id']) for b in all_blocks}
    
    # Real pipeline begins here
    processed_blocks = process_blocks(all_blocks)  # This filters and transforms
    
    # Critical statement
    final_yield = optimize_harvest(processed_blocks)
    
    # Print result as required
    print(f"Result: {final_yield}")