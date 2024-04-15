from PixAI.repaint import img2img

def Img2Img_pai(tmp_save_path, prompt, refimg_path):
    img2img(refimg_path, tmp_save_path, prompt)