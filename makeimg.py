#!/bin/bash
def create_ppm_image(filename, width, height, colors):
    # Open the file for writing
    with open(filename, 'w') as f:
        # Write the PPM header
        f.write(f'P3\n{width} {height}\n255\n')

        # Calculate the size of each color cell
        cell_width = width // 4
        cell_height = height // 4

        # Write the pixel data
        for y in range(height):
            for x in range(width):
                # Determine which color cell we're in
                color_index = (y // cell_height) * 4 + (x // cell_width)
                color = colors[color_index]

                # Write the RGB values
                f.write(f'{color[0]} {color[1]} {color[2]}\n')

# Define the colors (RGB values)
colors = [
    (45, 79, 30),    # Dark Grass Green
    (30, 63, 32),    # Forest Green
    (58, 75, 53),    # Moss Green
    (60, 69, 46),    # Olive Drab
    (59, 47, 47),    # Dark Earth Brown
    (74, 55, 40),    # Rich Soil Brown
    (74, 74, 74),    # Dark Stone Gray
    (47, 79, 79),    # Slate Gray
    (54, 69, 79),    # Charcoal
    (47, 53, 59),    # Deep Granite
    (94, 80, 65),    # Dark Sandstone
    (78, 59, 49),    # Muddy Brown
    (37, 53, 41),    # Deep Pine Green
    (43, 61, 79),    # Shadow Blue
    (78, 59, 49),    # Dark Rust
    (61, 31, 47)     # Deep Burgundy
]

# Set the image dimensions
width, height = 400, 400

# Create the PPM image
create_ppm_image('dark_environment_colors.ppm', width, height, colors)

print("PPM image has been created: dark_environment_colors.ppm")

