def main():
    # Domain-specific context: Bioinformatics sequence encoding with noise
    base_pairs = 'ATCGATCG'
    encoded_sequence = [ord(c) % 7 for c in base_pairs]

    # Irrelevant transformation (dead path)
    def decoy_transform(seq):
        return [x ^ 3 for x in seq][::-1]

    # Real transformation chain
    modifiers = [2, -1, 3, 0, 4, -2, 1, 5]
    adjusted = [encoded_sequence[i] + modifiers[i] for i in range(len(encoded_sequence))]

    # Bit manipulation red herring
    masked = [x & 7 for x in adjusted]
    shifted = [x << 1 for x in masked]  # Misleading shift - not used

    # Critical lambda-based filter (only some values propagate)
    is_valid = lambda x: x > 4
    filtered = list(filter(is_valid, adjusted))  # Uses adjusted, not masked or shifted

    # Decoy set operations (distractor)
    unique_shifted = set(shifted)
    shifted_sum = sum(unique_shifted)  # Never used

    # Another decoy: sorting irrelevant data
    sorted_masked = sorted(masked, reverse=True)
    median_guess = sorted_masked[len(sorted_masked)//2]  # Unused

    # Core logic disguised among distractions
    def transform(seq):
        result = 0
        for i, val in enumerate(seq):
            result += val * (i + 1)  # Weighted sum
        result ^= 987  # Final bit mix
        return result if result > 0 else -result

    # Key assignment
    checksum = transform(filtered)

    # Dead code path with complex slicing (red herring)
    def unused_diagnostic(data):
        n = len(data)
        return data[n//2:] + data[:n//2]  # Never called

    # Print required output
    print(f"Result: {checksum}")

if __name__ == '__main__':
    main()