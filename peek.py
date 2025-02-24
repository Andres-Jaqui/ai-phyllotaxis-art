from PIL import Image
import os
folder = "data/raw"
for file in os.listdir(folder):
    img = Image.open(os.path.join(folder, file))
    print(f"Loaded {file}: {img.size}")