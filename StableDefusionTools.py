from StableDefusion.api import *
from StableDefusion.payload import get_payload
from StableDefusion.configuration import model_to_use

def Img2Img_sd(tmp_save_path, prompt, refimg_path):
    call_set_model_api(model_to_use)
    payload = get_payload(refimg_path, prompt)
    call_img2img_api(tmp_save_path, **payload)