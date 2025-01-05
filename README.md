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

$$IoU = \frac{\text{Area of Overlap}}{\text{Area of Union}}$$

### Evaluation of 1000 images
We let the model predict the location of birds in 1000 images. Below, the distribution of the computed IoU is shown.

![diagram_distribution_iou_1000](https://github.com/user-attachments/assets/b4c3a9fd-b55e-411b-8449-7103637bd91d)

 Instead of using the actual IoU value, we classify the quality of a prediction as follows:  
- excellent: IoU == 1
- perfect: IoU > 0.9
- very good: IoU > 0.8
- good: IoU > 0.7
- acceptable: IoU > 0.5
- poor: IoU <= 0.5

### Examples
Below, an example for each quality category as described above is listed. The green rectangle shows the predicted bounding box, the blue rectangle the target bounding box.
<p>
    <img width=200 src=https://github.com/user-attachments/assets/fc15b410-9d33-48e6-949e-f5f964460acf></img>
    <img width=200 src=https://github.com/user-attachments/assets/4704790d-80cf-4f2f-9ff0-711f081329ec></img>
    <img width=200 src=https://github.com/user-attachments/assets/9830f0c6-a37d-4dd9-b462-ee56e77b934e></img>
</p>
<p>
    <img width=200 src=https://github.com/user-attachments/assets/7c7590b4-0b1a-4259-8bc6-d2c41198bf6e></img>
    <img width=200 src=https://github.com/user-attachments/assets/c74ef383-9c1d-483f-9844-1dba2c711e8c></img>
    <img width=200 src=https://github.com/user-attachments/assets/01bbdc7a-57bb-4c72-9365-3a119a9eb48e></img>
</p>
