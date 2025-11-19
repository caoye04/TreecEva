from functools import reduce

def adjust_weights(weights):
    adjusted = []
    for i in range(len(weights)):
        left = weights[i-1] if i > 0 else 0
        right = weights[i+1] if i < len(weights)-1 else 0
        adjustment = (left + right) // 2 if (left + right) % 2 == 0 else (left + right + 1) // 2
        adjusted.append(weights[i] + adjustment)
    return adjusted

def compute_checksum(values):
    checksum = 0
    for val in values:
        checksum ^= val
    return checksum

package_weights = [12, 7, 23, 8, 15, 30]
transformed_weights = list(map(lambda x: x * 2 if x % 2 == 0 else x * 3, package_weights))
adjusted_weights = adjust_weights(transformed_weights)
filtered_weights = list(filter(lambda x: x > 30, adjusted_weights))
final_checksum = compute_checksum(filtered_weights) if filtered_weights else 0
print(f"Result: {final_checksum}")