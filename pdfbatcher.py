import os
from PIL import Image
import time

pdf_dir = "PDF"
image_dir = "Images"
if not os.path.exists(pdf_dir):
    os.makedirs(pdf_dir)

start_time = time.time()
total_images = 0
total_pdfs = 0
for dirpath, dirnames, filenames in os.walk(image_dir):
    if dirpath != image_dir and (any(f.endswith(".jpg") for f in filenames) or any(f.endswith(".png") for f in filenames) or any(f.endswith(".webp") for f in filenames)) and dirpath != pdf_dir:
        images = [os.path.join(dirpath, f) for f in filenames if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".webp")]
        pdf_path = os.path.join(pdf_dir, os.path.basename(dirpath) + ".pdf")
        im_list = []
        total_images += len(images)
        total_pdfs += 1
        print(f"Processing folder: {dirpath}")
        start_folder_time = time.time()
        for i in images:
            if i.endswith(".png"):
                img = Image.open(i).convert("RGB")
                jpg_path = os.path.splitext(i)[0] + ".jpg"
                img.save(jpg_path)
                im_list.append(img)
            elif i.endswith(".webp"):
                img = Image.open(i).convert("RGB")
                jpg_path = os.path.splitext(i)[0] + ".jpg"
                img.save(jpg_path)
                im_list.append(img)
            else:
                im = Image.open(i)
                im_list.append(im)
        im_list[0].save(pdf_path, save_all=True, append_images=im_list[1:])
        print(f"Time taken for folder {dirpath} <::> {time.time() - start_folder_time} seconds")
print(f"Total images converted: {total_images}")
print(f"Total PDFs created: {total_pdfs}")
print(f"Total time taken: {time.time() - start_time} seconds")
