import os
import shutil
import base64
import tempfile
import random
import string
from pathlib import Path

def encode_file_to_base64(path):
    with open(path, 'rb') as file:
        return base64.b64encode(file.read()).decode('utf-8')

def decode_and_save_base64(base64_str, save_path):
    with open(save_path, "wb") as file:
        file.write(base64.b64decode(base64_str))

def replace_image(old_path, new_path):
    if os.path.isfile(new_path):
        shutil.copy2(new_path, old_path)
        print(f"Image replaced successfully: {old_path}")
    else:
        print("Error: New image not found.")

def get_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def copy_image(image_path):
    image_name = Path(image_path).stem  # Get the original name of the image file
    new_name = f"{image_name}_original.png"
    
    if os.path.isfile(image_path):
        shutil.copy(image_path, new_name)
        print(f"Image copied successfully: {new_name}")
    else:
        print("Error: File not found.")