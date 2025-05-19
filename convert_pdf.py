from pdf2image import convert_from_path
import os

pdf_path = "Stamboomboek Familie Senders.pdf"
output_dir = "pages"
os.makedirs(output_dir, exist_ok=True)

images = convert_from_path(pdf_path, dpi=150)
for i, img in enumerate(images):
    img.save(f"{output_dir}/page_{i+1:03}.jpg", "JPEG")

