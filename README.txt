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

To test the model, download our trained model [https://drive.google.com/file/d/11mqZG0BXz0VnuKIITShxio8obpN7NuSA/view?usp=sharing], use the cfg file 'dino-5scale_swin-t_8xb2-12e_coco.py', and make sure the visdrone dataset is already changed to the right coco_format, or you can directly download it from here [https://drive.google.com/file/d/12gO-wIwZ1xedAkhusat9uAVgTXMM-KuS/view?usp=sharing] and here is the train/val json noting if you need:[https://drive.google.com/file/d/132C_byasaAu7ggPaviL3AA9SfUwZnyMB/view?usp=sharing][https://drive.google.com/file/d/135rqyDRyMKxtNUd5_vhEtC3-MHdh16i-/view?usp=sharing], put the dataset int the main root and the json notes at the right place. Use the sentence like this to start the testing:
python tools/test.py dino-5scale_swin-t_8xb2-12e_coco.py epoch_12.pth 
For more requirements, read the tools/test.py to get more information and para settings.

To train the model, use the sentence like this:
python tools/train.py dino-5scale_swin-t_8xb2-12e_coco.py
Also, more para settings please check the train.py file.

We uploads some examples to the folder [output],and show them in the jupyternotebook [showresultinjupyter.ipynb], or you can check directly in the output/vis dict.

We upload a GUI.py file to give a simple GUI interface function that we learned in this term. The lib is quite similar as pyqt5 but looks better.You can easily use it buy the window, choose a config file, a checkpoint pth file and a img file, you can find the result create in your dict:./out/vis/[your img name], and also showed in the GUI window! Just as the png file 'show_of_GUI.png' shown.

We uploading another interesing model as pdino, constracted as pyramid pooling transformer as backbone and dino as head. The most interesing thing is this pyramid pooling model is fully recoded to mmdetection3x's format by myself.So, if you want to know more about the mmdetection repo and learn how to transfer a timm model or others based on origianal pytorch model into mmdetection3x, this may help you. Kindly check the new backbone at:pdino_models, and the results also uploaded, you can see them in dic:pdino_result_pic and pdino_config_ruslt.And the modelfile for this version is here:[https://drive.google.com/file/d/12zH7P-exjR9SxqazxxjHZcsPzH8yIBdl/view?usp=sharing] if you want to test it.
