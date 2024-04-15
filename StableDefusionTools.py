from StableDefusion.api import *
from StableDefusion.payload import get_payload

def Img2Img_sd(tmp_save_path, prompt, refimg_path):
    payload = get_payload(refimg_path, prompt)
    call_img2img_api(tmp_save_path, **payload)