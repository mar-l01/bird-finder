# bird-finder
This repository uses a Detection Transformer (DETR) model to detect birds in images by predicting a bounding box.

## NABirds Dataset
This repository uses the NABirds of the Cornell Lab of Ornithology, a data-set with 48.000 photographs of birds, which can be found here: https://dl.allaboutbirds.org/nabirds.  
(Data provided by the Cornell Lab of Ornithology, with thanks to photographers and contributors of crowdsourced data at AllAboutBirds.org/Labs. This material is based upon work supported by the National Science Foundation under Grant No. 1010818.)

## Detection Transformer (DETR) Model
More details on applying the DETR model can be found here: https://huggingface.co/facebook/detr-resnet-50.  
If you are interested in more details on the underlying architecture of the model, have a look here: https://arxiv.org/abs/2005.12872.

## Evaluation
For evaluating the DETR model on the NABirds dataset, we are comparing the predicted bounding box of the model with the target bounding box as labeled in the dataset.  
The comparison is done by calculating the Intersection over Union (IoU):  
$iou = \frac{area-of-overlap}{area-of-union}$
