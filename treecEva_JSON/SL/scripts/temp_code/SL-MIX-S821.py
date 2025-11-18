rgb_normalizer = lambda r, g, b: (r/255.0, g/255.0, b/255.0)

red_component, green_component, blue_component = 153, 76, 255
normalized_red, normalized_green, normalized_blue = rgb_normalizer(red_component, green_component, blue_component)

# Color encoding formula: hex(round(n*255)) concatenated
encoded_color = hex(round(normalized_red*255))[2:].zfill(2) + \
                hex(round(normalized_green*255))[2:].zfill(2) + \
                hex(round(normalized_blue*255))[2:].zfill(2)

print(f"Result: {encoded_color}")