def register_color(palette):
    def decorator(func):
        color_name, hex_val = func()
        palette[color_name] = hex_val
        return func
    return decorator

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def complement_color(hex_color):
    rgb = hex_to_rgb(hex_color)
    complement = tuple(255 - c for c in rgb)
    return rgb_to_hex(complement)

palette = {}

@register_color(palette)
def crimson():
    return ('crimson', '#dc143c')

@register_color(palette)
def azure():
    return ('azure', '#007fff')

@register_color(palette)
def lime():
    return ('lime', '#00ff00')

transformed_palette = {name: complement_color(hex_val) for name, hex_val in palette.items()}

azure_complement_hex = transformed_palette['azure']
azure_complement_rgb = hex_to_rgb(azure_complement_hex)
blue_component = azure_complement_rgb[2]
print(f"Result: {blue_component}")