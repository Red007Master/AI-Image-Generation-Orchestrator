import os
import sys
import datetime
from StableDefusion.utils import *
from StableDefusionTools import Img2Img_sd
from PixAITools import Img2Img_pai

test_mode = True

def post_process_image(temp_image_path, ref_image_path):
    if not test_mode:
        copy_image(ref_image_path)
        replace_image(ref_image_path, temp_image_path)
    

def main():
    timestamp = str(int(datetime.datetime.now().timestamp()))
    random_string = get_random_string(5)
    temp_filename = f"tmp_{timestamp}_{random_string}"

    temp_folder = os.path.join(tempfile.gettempdir(), 'RimworldAIAvatarGenImages')
    temp_image_path = os.path.join(temp_folder, temp_filename + '.png')
    os.makedirs(temp_folder, exist_ok=True)

    prompt = sys.argv[2]
    ref_image_path = sys.argv[3]

    if sys.argv[1] == 'sdlocal':
        print(f'Using local Stable Defusion instance [{sys.argv[1]}] with prompt:\n[{prompt}].\nTmp file:\n[{temp_image_path}]')
        Img2Img_sd(temp_image_path, prompt, ref_image_path)
        post_process_image(temp_image_path, ref_image_path)
    elif sys.argv[1] == 'pixai':
        print(f'Using PixAI [{sys.argv[1]}] with prompt:\n[{prompt}].')
        Img2Img_pai(temp_image_path, prompt, ref_image_path)
        post_process_image(temp_image_path, ref_image_path)
    else:
        print('Unknown')

if __name__ == '__main__':
    for _ in range(10):
        main()