def transform_id(package_id):
    return sum(ord(c) * (i + 1) for i, c in enumerate(package_id))

package_registry = [
    "PKG-Alpha-782",
    "PKG-Beta-914",
    "PKG-Gamma-331",
    "PKG-Delta-526",
    "PKG-Epsilon-849"
]

processed_weights = []
for idx, pkg in enumerate(package_registry):
    if idx % 2 == 0:
        processed_weights.append(transform_id(pkg))
    else:
        processed_weights.append(transform_id(pkg[::-1]))

segment_scores = []
for i in range(0, len(processed_weights), 2):
    if i+1 < len(processed_weights):
        segment_scores.append(processed_weights[i] ^ processed_weights[i+1])
    else:
        segment_scores.append(processed_weights[i])

authentication_score = 0
for score in segment_scores:
    if score > 1000:
        authentication_score += score & 0xFF
    else:
        authentication_score += score

print(f"Result: {authentication_score}")