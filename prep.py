from PIL import Image
import os
input_folder = "data/raw"
output_folder = "data/processed"
os.makedirs(output_folder, exist_ok=True)
for file in os.listdir(input_folder):
    img = Image.open(os.path.join(input_folder, file))
    img_resized = img.resize((256, 256))
    img_resized.save(os.path.join(output_folder, file))
    print(f"Resized {file} to 256x256")