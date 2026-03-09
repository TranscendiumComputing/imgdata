from PIL import Image
import sys
    
filepath = sys.argv[1]
img = Image.open(filepath)
print("ImgData by Transcendium Computing :3")
print("Image format is " + str(img.format) + ".")
print("Image resolution is " + str(img.size) + ".")
picmode = str(img.mode)
if picmode == "L":
    print("Image is a grayscale (black and white) image.")
elif picmode == "RGB":
    print("Image is a color (RGB) image.")
else:
    print("Unrecognized format. This does not nesessarily mean the image is corrupted, however.")
