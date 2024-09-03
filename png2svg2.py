import sys
from PIL import Image
import numpy as np
from skimage import measure
from skimage.draw import polygon_perimeter
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

# Check if image file path is provided
if len(sys.argv) < 2:
    print("Usage: python script.py /path/to/your/image.png")
    sys.exit()

# Load image
image = Image.open(sys.argv[1])

# Convert image to numpy array
image_array = np.array(image)

# Create a mask for the red pixels
red_pixels = (image_array[:,:,0] > 100) & (image_array[:,:,1] < 50) & (image_array[:,:,2] < 50)

# Find contours of the red regions
contours = measure.find_contours(red_pixels, 0.5)

# Create a new image to draw the paths on
fig, ax = plt.subplots()

# Convert each contour to a path and add it to the plot
for contour in contours:
    path = Path(contour)
    patch = patches.PathPatch(path, facecolor='black', lw=2)
    ax.add_patch(patch)

# Remove axis and set aspect ratio to equal to keep the original image ratio
plt.axis('off')
ax.set_aspect('equal')

# Save the plot to an SVG file
plt.savefig(sys.argv[1].rsplit('.', 1)[0] + '.svg', format='svg', bbox_inches='tight', pad_inches = 0)
