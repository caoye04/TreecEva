def analyze_efficiency(logs):
    total = 0
    for i, log in enumerate(logs):
        if i % 2 == 0:
            total += len(log) * 0.1
    return total

# Irrelevant helper function (decoy)
def validate_integrity(data):
    checksum = 0
    for item in data:
        if isinstance(item, str):
            checksum ^= hash(item)
    return checksum % 100 == 0

# Another decoy: complex but unused transformation
decoys = [x ** 2 + 3*x - 1 for x in range(15)]
processed_decoys = list(map(lambda z: z // 2 if z > 10 else z, decoys))

# Real data pipeline
process_stages = [
    {'stage': 'heating', 'temp': 300, 'duration': 120, 'catalyst': True},
    {'stage': 'cooling', 'temp': 150, 'duration': 90, 'catalyst': False},
    {'stage': 'pressurize', 'temp': 200, 'duration': 60, 'catalyst': True},
    {'stage': 'reaction', 'temp': 450, 'duration': 180, 'catalyst': True}
]

status_flags = {stage['stage']: False for stage in process_stages}

# Simulate intermediate checks (mostly irrelevant)
for idx, stage in enumerate(process_stages):
    if 'p' in stage['stage']:
        status_flags[stage['stage']] = True
    elif stage['temp'] > 250:
        status_flags[stage['stage']] = True

# Distractor: unused nested loop over zipped structures
snapshot_log = ['start', 'mid', 'end']
stage_names = [s['stage'] for s in process_stages]
for log_entry, (i, name) in zip(snapshot_log, enumerate(stage_names)):
    if len(name) % 2 == 0:
        continue  # dead branch with no effect

# Core calculation function
def calculate_thermal_output(stages):
    base_heat = 0
    efficiency_mod = 1.0
    catalyst_bonus = 0
    duration_factor = 0

    # Real logic begins
    for stage in stages:
        temp = stage['temp']
        duration = stage['duration']
        uses_catalyst = stage['catalyst']

        if temp < 200:
            base_heat -= temp * 0.5
        elif temp < 400:
            base_heat += temp * 1.2
        else:
            base_heat += temp * 1.8  # high-temp multiplier

        duration_factor += duration ** 0.5

        if uses_catalyst:
            catalyst_bonus += 25

        # Early exit red herring (never triggered due to data)
        if temp > 500:
            efficiency_mod *= 0.5
            break

    # Misleading comment: "adjust for external pressure" (no real pressure data)
    environmental_dampener = 0.9 + (len(stages) * 0.01)  # minor tweak

    final_output = (base_heat + duration_factor + catalyst_bonus) * environmental_dampener

    # This assignment is critical
    thermal_capacity = int(final_output)  # round down to integer

    return thermal_capacity

# Spurious analysis on flags (dead code path)
active_count = 0
for flag in status_flags.values():
    if flag:
        active_count += 1

# Unused lambda transformation on decoy list
double_shift = lambda x: x << 1
transformed = [double_shift(d) for d in processed_decoys if d > 20]

# Key execution point
thermal_capacity = calculate_thermal_output(process_stages)

# Print result as required
print(f"Result: {thermal_capacity}")