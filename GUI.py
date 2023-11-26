import io
import os
import PySimpleGUI as sg
from PIL import Image
import numpy as np
import warnings
import mmcv
import torch
warnings.filterwarnings("ignore")
from mmdet.apis import (async_inference_detector, inference_detector,
                        init_detector, show_result_pyplot)

config_file = r"./dino-5scale_swin-t_8xb2-12e_coco.py"
ckpt_file = r"./epoch_12.pth"
img_file = r"./0000346_00001_d_0000346.jpg"

file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]

height, width = 600,600
def main():

    layout = 	[
# 		[sg.Text('MMDetection',justification='center',pad=(200,0))],
        
		[sg.Text('config file',size=(16,1)), sg.In(config_file,size=(80,1), key='config'), sg.FileBrowse()],
        [sg.Text('model checkpoint',size=(16,1), auto_size_text=False), sg.In(ckpt_file,size=(80,1), key='ckpt'), sg.FileBrowse()],
		[sg.Text('Path to image',size=(16,1)), sg.In(img_file,size=(80,1), key='image'), sg.FileBrowse()],
        
		[sg.Text('Device',size=(16,1)), sg.Combo(['cuda:0','cpu'],default_value='cpu',key='device')],
		[sg.Text('Score threshold',size=(16,1)), sg.Slider(range=(0,1), orientation='h', resolution=0.1, default_value=0.3, size=(15,15), key='threshold')],
		[sg.OK('Detect'), sg.Exit()],
        
        [sg.Image(key="source_image",size=(height,width),background_color='grey'),
        sg.Image(key="detected_image",size=(height,width),background_color='gray')],
        ]

    window = sg.Window('MMDetection', 
                   layout,
                   default_element_size=(14,2),
                   text_justification='right',
                   auto_size_text=False,
                   # element_justification='c'
                   )

    while True:
        event, values = window.read()
        config = values['config']
        ckpt = values['ckpt']
        device = values['device']
        input_img = values["image"]
        score_thr = values['threshold']

        if os.path.exists(input_img):
                # image = Image.open(input_img)
                image = Image.open(input_img)
                image.thumbnail((height,width))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["source_image"].update(data=bio.getvalue())

        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "Detect":

            model = init_detector(config, ckpt, device=device)
            result = inference_detector(model, input_img)
            out = 'detect.png'
            show_result_pyplot(model, input_img, result, score_thr=score_thr, out_file=out)
            
            # image = Image.fromarray(img)
            image = Image.open(out)
            image.thumbnail((height,width))
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            window["detected_image"].update(data=bio.getvalue())

    window.close()


if __name__ == "__main__":

    main()
