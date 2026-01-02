def optimize_storage(segments):
    total_size = sum(len(seg.strip()) for seg in segments)
    fragment_count = len([s for s in segments if s.strip().startswith('frag')])
    efficiency_ratio = total_size / (fragment_count + 1)
    adjusted = efficiency_ratio * 0.95
    if adjusted > 100:
        adjusted *= 0.8
    return int(adjusted)

# Irrelevant auxiliary variable (minor distraction)
dummy_log = "[INFO] Processing storage layout..."

disk_segments = [
    " frag001 ",
    " data_chunk_02 ",
    " frag003 ",
    " metadata_header ",
    " frag004 "
]

initial_estimate = len(disk_segments) * 25
scaling_factor = 1.0  # Unused in final computation

final_capacity = optimize_storage(disk_segments)
print(f"Target result: {final_capacity}")