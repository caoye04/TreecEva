from collections import defaultdict
import bisect

def compute_signature_hash(signature, position):
    hash_val = 0
    for i, char in enumerate(signature):
        hash_val += (ord(char) * (i + 1) * (position + 1))
    return hash_val % 1000

def process_batch(batch, bucket_collisions):
    for pos, sig in enumerate(batch):
        hash_key = compute_signature_hash(sig, pos)
        bucket_collisions[hash_key] += 1

packet_batches = [
    ["A1B2", "C3D4", "E5F6"],
    ["G7H8", "I9J0", "A1B2"],
    ["K1L2", "M3N4", "O5P6", "Q7R8"]
]

bucket_collisions = defaultdict(int)
for batch in packet_batches:
    process_batch(batch, bucket_collisions)

sorted_buckets = sorted(bucket_collisions.keys())
sorted_counts = [bucket_collisions[b] for b in sorted_buckets]

threshold = 2
target_index = bisect.bisect_right(sorted_counts, threshold)
target_bucket = sorted_buckets[target_index] if target_index < len(sorted_buckets) else -1

print(f"Result: {target_bucket}")