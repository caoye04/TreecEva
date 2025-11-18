from itertools import permutations

def calculate_mix_value(a, b):
    return a * b + a + b

def max_color_value(base_colors):
    n = len(base_colors)
    max_val = 0
    
    # Try all possible orderings of colors
    for perm in permutations(base_colors):
        # Dynamic programming approach to track max value at each step
        dp = [0] * (n + 1)
        dp[0] = perm[0]
        
        for i in range(1, n):
            # Mix current color with previous accumulated value
            mixed = calculate_mix_value(dp[i-1], perm[i])
            dp[i] = mixed
            
            if mixed > max_val:
                max_val = mixed
    
    return max_val

# Base colors for the artist's palette
artist_palette = [2, 3, 5, 7]

# Calculate maximum achievable color value
final_masterpiece_value = max_color_value(artist_palette)
print(f"Result: {final_masterpiece_value}")