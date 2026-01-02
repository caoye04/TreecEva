def analyze_component(integrity_check, redundancy_flag):
    if integrity_check < 10:
        return integrity_check * 3 + 7
    elif integrity_check < 25 or redundancy_flag:
        temp_val = (integrity_check // 4) * 2
        adjustment = 11 if temp_val % 3 == 0 else 5
        return temp_val + adjustment
    else:
        return sum([i for i in range(1, integrity_check % 9)])


def evaluate_pathway(stability_index):
    pathway_data = []
    for i in range(3):
        stability_index = (stability_index + i**2) % 17
        pathway_data.append(stability_index)
    
    # Irrelevant transformation (distractor)
    transformed = [x ^ 5 for x in pathway_data]
    normalized = [y / max(pathway_data) for y in pathway_data if y > 5]
    
    if len(normalized) == 0:
        return 1
    return int(sum(normalized))

# Misleading initialization block (dead code path)
def deprecated_calc(x):
    return (x << 2) - x  # Unused function

legacy_mode = True
compatibility_offset = 86
fallback_buffer = [0] * 5

# Core logic with embedded distractions
logic_flow = 42
overhead_penalty = 13

# Red herring: complex-looking but unused bitwise chain
obfuscation_mask = (logic_flow ^ 0xA3) & 0xFF
obfuscation_shift = (obfuscation_mask >> 2) | 0x1C
validation_key = obfuscation_shift ^ 0x5D  # Never used again

# Distractor: fake state tracker
state_log = []
for tick in range(5):
    if tick % 2 == 0:
        state_log.append(f"TICK_{tick}")

# Conditional expression mix (relevant)
base_metric = logic_flow if logic_flow > 40 else 17
adjustment_factor = overhead_penalty if overhead_penalty < 20 else 1

# Nested dictionary structure with decoy entries
system_profile = {
    'core': {
        'primary': base_metric,
        'auxiliary': adjustment_factor,
        'flags': {
            'optimized': True,
            'legacy': False
        }
    },
    'deprecated': {
        'buffer_size': compatibility_offset,
        'active': False
    },
    'diagnostics': {
        'last_run': 'N/A',
        'checksum': 0xDEADBEEF  # Decoy value
    }
}

# Simulated data corruption check (irrelevant)
corruption_flag = False
data_fragments = [1, 2, 3]
for fragment in data_fragments:
    if fragment & 1:
        corruption_flag = not corruption_flag

# Key computation begins here — real path
integrity_level = system_profile['core']['primary'] - 5
redundancy_enabled = system_profile['core']['flags']['optimized'] and (integrity_level % 2 == 0)

component_score = analyze_component(integrity_level, redundancy_enabled)
pathway_rating = evaluate_pathway(component_score % 19)

# Real overhead calculation buried among noise
penalty_modifier = 1.5 if system_profile['core']['flags']['legacy'] else 0.8
adjusted_penalty = overhead_penalty * penalty_modifier

# Critical conditional expression
final_weight = pathway_rating if component_score > 30 else (logic_flow // 5)

# Actual answer derivation
intermediate_result = (component_score + final_weight) // 2

# Secondary irrelevant loop (simulates logging)
log_archive = []
for idx in range(3):
    log_archive.append({"entry_id": idx, "status": "OK"})

# Another decoy function call
unused_diagnostic = evaluate_pathway(11)

# Real efficiency formula
def compute_efficiency(flow, penalty):
    raw = flow * 0.75
    deduction = penalty * 0.4
    return int(raw - deduction)

# This is the key statement
efficiency_score = compute_efficiency(logic_flow, overhead_penalty)

# Print required result
print(f"Result: {efficiency_score}")