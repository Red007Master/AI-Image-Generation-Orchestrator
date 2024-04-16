from StableDefusion.utils import decode_and_save_base64
from StableDefusion.configuration import webui_server_url
import urllib.request
import json
import requests

def call_api(api_endpoint, **payload):
    data = json.dumps(payload).encode('utf-8')
    request = urllib.request.Request(
        f'{webui_server_url}/{api_endpoint}',
        headers={'Content-Type': 'application/json'},
        data=data,
    )
    response = urllib.request.urlopen(request)
    return json.loads(response.read().decode('utf-8'))


def call_set_model_api(model_to_use):
    option_payload = {
        "sd_model_checkpoint": model_to_use,
    }
    response = requests.post(url=f'{webui_server_url}/sdapi/v1/options', json=option_payload)

def call_txt2img_api(save_path, **payload):
    response = call_api('sdapi/v1/txt2img', **payload)
    for index, image in enumerate(response.get('images')):
        decode_and_save_base64(image, save_path)


def call_img2img_api(save_path, **payload):
    response = call_api('sdapi/v1/img2img', **payload)
    for index, image in enumerate(response.get('images')):
        decode_and_save_base64(image, save_path)