# detection_france

Drone-captured image's object detection with transformer-based bakcbone and detector architecture

This is the project work of computer secience lesson in France.

To use this project,make sure with this environment:
0.PyTorch==1.11.0+cu113
1.mmdetection==v3.1.0
2.mmengine==v0.8.4
3.mmcv==2.0.1

You could install these environmet from the document [https://mmdetection.readthedocs.io/en/latest/get_started.html] or follow the steps below:
1.pip install openmim
2.git clone https://github.com/qianlian-mozi/detection_france.git
3.cd detection_france
4.mim install -v -e .

The log file is uploaded as '20231016_173555.log', the result shows the detector can perform bbox/map:0.2890 in visdrone. We use the coco metric to evaluate the performence, for more result, please check the file '20231016_173555.log'.The whole detector contains the swintiny as a backbone and the dino as a head. We changes some faults caused by the dimention and apis problems caused by the version updated with mmdet.

To test the model, download our trained model [https://drive.google.com/file/d/11mqZG0BXz0VnuKIITShxio8obpN7NuSA/view?usp=sharing], use the cfg file 'dino-5scale_swin-t_8xb2-12e_coco.py', and make sure the visdrone dataset is already changed to the right coco_format, or you can directly download it from here [https://drive.google.com/file/d/11oDTRjruaKy69Yyb3DpNxySQO84aVsu8/view?usp=sharing], put the dataset int the main root. Use the sentence like this:
python tools/test.py dino-5scale_swin-t_8xb2-12e_coco.py epoch_12.pth 

To train the model, use the sentence like this:
python tools/train.py dino-5scale_swin-t_8xb2-12e_coco.py

We uploads some examples to the folder [output],and show them in the jupyternotebook [showresultinjupyter.ipynb], or you can check directly in the output/vis dict.

We upload a GUI.py file to give a simple GUI interface function that we learned in this term. The lib is quite similar as pyqt5 but looks better.You can easily use it buy the window, choose a config file, a checkpoint pth file and a img file, you can find the result create in your dict:./out/vis/[your img name], and also showed in the GUI window! Just as the png file 'show_of_GUI.png' shown.

