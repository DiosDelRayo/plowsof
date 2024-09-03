import sys
import base64
from xml.etree import ElementTree as ET


def main():
    # Check if SVG file path is provided
    if len(sys.argv) < 2:
        print('Usage: python script.py /path/to/your.svg')
        return

    # Get SVG file path from command line argument
    svg_path = sys.argv[1]

    # Parse SVG file
    tree = ET.parse(svg_path)
    root = tree.getroot()

    # Namespace map
    nsmap = {'svg': 'http://www.w3.org/2000/svg'}

    # Add fill='black' to each path tag
    for path in root.findall('.//svg:path', nsmap):
        path.attrib['fill'] = 'black'

    # Convert modified SVG to string
    svg_string = ET.tostring(root, encoding='unicode')

    # Encode SVG string to base64
    encoded_string = base64.b64encode(svg_string.encode('utf-8')).decode('utf-8')

    # Generate data URI
    data_uri = 'data:image/svg+xml;base64,' + encoded_string

    print(data_uri)

if __name__ == '__main__':
    main()
