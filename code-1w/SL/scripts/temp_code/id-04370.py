from collections import defaultdict, Counter

# Simulate server load monitoring across regions and services
def monitor_infrastructure_load():
    region_loads = [
        ('us-west', 23), ('eu-central', 18), ('us-west', 15), ('ap-south', 31),
        ('eu-central', 27), ('us-west', 19), ('ap-south', 25), ('us-east', 14),
        ('eu-central', 22), ('us-east', 19), ('us-west', 21), ('ap-south', 29)
    ]

    # Track total usage per region (relevant)
    usage_tracker = defaultdict(int)
    for region, load in region_loads:
        usage_tracker[region] += load

    # Misleading: Count frequency of each exact (region, load) pair (semi-relevant distractor)
    pair_counter = Counter(region_loads)

    # Dead code path: This list is never used further
    high_load_threshold = 25
    oversized_regions = [r for r, l in region_loads if l > high_load_threshold]

    # Simulate auxiliary calculation: average per-entry load (distractor)
    total_entries = len(region_loads)
    avg_load_per_entry = sum(l for _, l in region_loads) / total_entries

    # Irrelevant smoothing factor based on unique regions
    unique_region_count = len(set(r for r, _ in region_loads))
    smoothing_factor = avg_load_per_entry / unique_region_count

    # Secondary tracker: count occurrences per region (partially redundant)
    region_frequency = defaultdict(int)
    for region, _ in region_loads:
        region_frequency[region] += 1

    # Compute peak capacity from actual accumulated loads (this is the key step)
    peak_capacity = max(usage_tracker.values()) if usage_tracker else 0

    # Additional red herring: normalized peak using smoothing (never used)
    normalized_peak = peak_capacity * smoothing_factor

    # Final result output
    print(f"Result: {peak_capacity}")

    return peak_capacity

# Execute simulation
monitor_infrastructure_load()