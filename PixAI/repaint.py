#!/usr/bin/python
from PixAI.PixaiAPI import PixaiAPI
import io
import os
import sys
import time
from PIL import Image
from PixAI.credentials import *


# model url looks like pixai.art/model/12345/67890
# use the second number which refers to the specific version of a model
# model = 1632080534138643945 # epic realism

# the following is a good preset that I recommend
model = 1693971202393705839 # western toon style
lora = {
    '1613982114424770324': 0.7, # western illustration vector
    '1638766839267720162': 0.5, # niji-flat
}
# the following will be added to all prompts
preamble = "mugshot, western illustration, clean lines, minimalist, "

# whether to use high priority tasks, which cost more credits
high_priority = False

def img2img(refimg_path, tmp_save_path, prompt):
    client = PixaiAPI(token)
    filename = refimg_path
    task = client.img2img(filename, preamble + prompt,
                          size=(480, 576),
                          priority=1000 if high_priority else 0,
                          modelId=model,
                          lora=lora,
                          strength=0.6,
                          steps=14,
                          batchSize=4,
                          )
    while True:
        if task.get_data():
            image = Image.open(io.BytesIO(task.data)).crop((0, 0, 480, 576))
            # you can further process the image here
            # for example, make the background transparent
            # image = rembg.remove(image)
            image.save(tmp_save_path)
            break
        else:
            time.sleep(1)
