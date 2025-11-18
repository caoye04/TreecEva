red_channel = 0b11010110
blend_mask = 0b10110011
filter_mask = 0b11110000

# Apply artistic blending using XOR
blended = red_channel ^ blend_mask

# Apply filtering using AND
final_intensity = blended & filter_mask

print(f'Result: {final_intensity}')