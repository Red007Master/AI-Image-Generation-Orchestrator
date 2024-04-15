from StableDefusion.utils import *
from StableDefusion.configuration import *
import json

batch_size = 1

def get_payload(refimg_path, prompt):
    init_images = [
        encode_file_to_base64(refimg_path)
    ]

    # prompt = "front portrait, 29-year-old female adult, pants, button-down shirt, recon armor, mugshot, western illustration, clean lines, minimalist, western, cowboy hat, <lora:western_illustration_offset:0.7> <lora:flat_illustration:0.5>"
    height = default_height
    width = default_width
    seed = default_seed
    steps = default_steps
    cfg_scale = default_cfg_scale

    img2imgPayload = {
        "batch_size": batch_size if len(init_images) == 1 else len(init_images),
        "cfg_scale": cfg_scale,
        "comments": {},
        "denoising_strength": 0.6,
        "disable_extra_networks": False,
        "do_not_save_grid": True,
        "do_not_save_samples": True,
        "height": height,
        "image_cfg_scale": 1.5,
        "init_images": init_images,
        "initial_noise_multiplier": 1,
        "inpaint_full_res": 0,
        "inpaint_full_res_padding": 32,
        "inpainting_fill": 1,
        "inpainting_mask_invert": 0,
        "mask_blur": 4,
        "mask_blur_x": 4,
        "mask_blur_y": 4,
        "mask_round": True,
        "n_iter": 1,
        "negative_prompt": "worst quality, large head, low quality, extra digits, bad eye, , ng_deepnegative_v1_75t EasyNegativeV2",
        "override_settings": {},
        "override_settings_restore_afterwards": True,
        "prompt": prompt,
        "resize_mode": 0,
        "restore_faces": False,
        "s_churn": 0,
        "s_min_uncond": 0,
        "s_noise": 1,
        "s_tmin": 0,
        "sampler_name": "Euler",
        "script_args": [],
        "seed": seed,
        "seed_enable_extras": True,
        "seed_resize_from_h": -1,
        "seed_resize_from_w": -1,
        "steps": steps,
        "styles": [],
        "subseed": -1,
        "subseed_strength": 0,
        "tiling": False,
        "width": width,
    }

    return img2imgPayload