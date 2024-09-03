import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt


def main():
    # Check if image file path is provided
    if len(sys.argv) < 2:
        print('Usage: python script.py /path/to/your/image.png')
        return

    # Get image file path from command line argument
    img_path = sys.argv[1]

    # Load image
    img = cv2.imread(img_path)

    # Define range for red color
    lower_red = np.array([0, 0, 100])
    upper_red = np.array([50, 50, 255])

    # Threshold the HSV image to get only red colors
    mask = cv2.inRange(img, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img, img, mask=mask)

    # Convert red pixels to black
    res[np.where((res == [0, 0, 255]).all(axis=2))] = [0, 0, 0]

    # Create SVG
    fig, ax = plt.subplots(figsize=(0.48, 0.48), dpi=100)
    ax.imshow(res)
    ax.axis('off')

    # Save SVG to the same directory as the input image, with the same base name
    svg_path = img_path.rsplit('.', 1)[0] + '.svg'
    plt.savefig(svg_path, format='svg', transparent=True)


if __name__ == '__main__':
    main()
