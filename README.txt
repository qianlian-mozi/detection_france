# detection_france

Drone-captured image's object detection with transformer-based bakcbone and detector architecture

This is the project work of computer secience lesson when I study in France.

To use this project,make sure with this environment:
1.mmdetection==v3.1.0
2.mmengine==v0.8.4
3.mmcv==2.0.1

You could install these environmet from the document [https://mmdetection.readthedocs.io/en/latest/get_started.html] or follow the steps below:
1.pip install openmim
2.cd mmdetection
2.mim install -v -e .

The log file is uploaded as '20231016_173555.log', the result shows the detector can perform bbox/map:0.2890 in visdrone. We use the coco metric to evaluate the performence, for more result, please check the file '20231016_173555.log'.

To test the model, download our trained model [], use the cfg file 'dino-5scale_swin-t_8xb2-12e_coco.py', and make sure the visdrone dataset is already changed to the right coco_format, or you can directly download it from here [], put the dataset int the main root. Use the sentence like this:
python tools/test.py dino-5scale_swin-t_8xb2-12e_coco.py epoch_12.pth 

To train the model, use the sentence like this:
python tools/train.py dino-5scale_swin-t_8xb2-12e_coco.py

