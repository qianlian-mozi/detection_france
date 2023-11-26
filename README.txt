# detection_france

Drone-captured image's object detection with transformer-based bakcbone and detector architecture

This is the project work of computer secience lesson in France.

To use this project,make sure with this environment:
0.PyTorch==1.11.0+cu113
1.mmdetection==v3.1.0
2.mmengine==v0.8.4
3.mmcv==2.0.1

You could install these environmet from the document [https://mmdetection.readthedocs.io/en/latest/get_started.html] or follow the steps below:
(0.before we sucessfully upload the main documents,you can still get the files from here [https://drive.google.com/file/d/11g1zs3MlLLsMOcNgRyEBio0zAK7MSU8B/view?usp=sharing], note that we changes many files different from the official repo, so you may not easily download it from offical repo.)
1.pip install openmim
2.cd detection_france (or if you download from the google drive's file, use this: cd mmdetection; anyway,change the root to the main repository.)
2.mim install -v -e .

The log file is uploaded as '20231016_173555.log', the result shows the detector can perform bbox/map:0.2890 in visdrone. We use the coco metric to evaluate the performence, for more result, please check the file '20231016_173555.log'.The whole detector contains the swintiny as a backbone and the dino as a head. We changes some faults caused by the dimention.

To test the model, download our trained model [https://drive.google.com/file/d/11mqZG0BXz0VnuKIITShxio8obpN7NuSA/view?usp=sharing], use the cfg file 'dino-5scale_swin-t_8xb2-12e_coco.py', and make sure the visdrone dataset is already changed to the right coco_format, or you can directly download it from here [https://drive.google.com/file/d/11oDTRjruaKy69Yyb3DpNxySQO84aVsu8/view?usp=sharing], put the dataset int the main root. Use the sentence like this:
python tools/test.py dino-5scale_swin-t_8xb2-12e_coco.py epoch_12.pth 

To train the model, use the sentence like this:
python tools/train.py dino-5scale_swin-t_8xb2-12e_coco.py

We uploads some examples to the folder [output],and show them in the jupyternotebook [showresultinjupyter.ipynb], or you can check directly in the output/vis dict.

