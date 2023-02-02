from os import walk, path, makedirs
from PIL import Image
from time import time

start_time = time()
total_images = 0
total_pdfs = 0
pdf_dir = "PDF"
image_dir = "Images"
if not path.exists(pdf_dir):
    makedirs(pdf_dir)

for dirpath, dirnames, filenames in walk(image_dir):
    try:
        if dirpath != image_dir and dirpath != pdf_dir:
            print(f"Processing folder: {dirpath}")
            start_folder_time = time()
            im_list = []
            
            pdf_path = path.join(pdf_dir, path.basename(dirpath) + ".pdf")
            images = [path.join(dirpath, f) for f in filenames if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".webp")]
            total_images += len(images)
            
            for i in images:
                img = Image.open(i).convert("RGB")
                jpg_path = path.splitext(i)[0] + ".jpg"
                img.save(jpg_path)
                im_list.append(img)

            im_list[0].save(pdf_path, save_all=True, append_images=im_list[1:])
            total_pdfs += 1
            print(f"Time taken for folder {dirpath} <::> {time() - start_folder_time} seconds")
    except:
        print("Directory contained no images")

print(f"Total images converted: {total_images}")
print(f"Total PDFs created: {total_pdfs}")
print(f"Total time taken: {time() - start_time} seconds")
