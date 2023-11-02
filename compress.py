from PIL import Image
from tqdm import tqdm
import os
import sys

def compress_image(input_path, output_path, max_size):
    image = Image.open(input_path)

    while True:
        image.save(output_path, optimize=True, quality=85)  # Adjust the quality factor as needed
        if os.path.getsize(output_path) / (1024 * 1024) <= max_size:
            break
        image = image.resize((int(image.width * 0.9), int(image.height * 0.9)))

if __name__ == "__main__":
    input_directory = sys.argv[1]  # Replace with the directory containing your images
    max_size_mb = 4

    for root, dirs, files in tqdm(os.walk(input_directory)):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                input_path = os.path.join(root, file)
                output_path = os.path.join(root , f'compressed_{file}') 

                if os.path.getsize(input_path) > max_size_mb * 1024 * 1024:
                    compress_image(input_path, output_path, max_size_mb)
                    os.remove(input_path)
                    os.rename(output_path, input_path)
                    #print(f"Compressed {file} to {max_size_mb} MB")
                else:
                    print(f"{file} is already less than {max_size_mb} MB")

