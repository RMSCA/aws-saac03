from pytesseract import image_to_string
from PIL import Image
import os
import json

# Directory containing your images
images_folder = "/Users/howellzhu/Documents/1_GitHub/aws-saac03/SAA-C03_0"
extracted_data = []

for filename in os.listdir(images_folder):
    if filename.endswith((".png", ".jpg", ".jpeg")):
        image_path = os.path.join(images_folder, filename)
        text = image_to_string(Image.open(image_path))
        extracted_data.append({"text": text, "image": filename})

# Save the extracted data to a JSON file
with open("data.json", "w") as f:
    json.dump(extracted_data, f)

print("Text extraction completed. Saved to data.json.")
