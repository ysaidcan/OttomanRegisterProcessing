# OttomanRegisterProcessing

First, install dhSegment toolbox. Installation instructions can be found at the following link:
https://dhsegment.readthedocs.io/en/latest/start/install.html

We have Ottoman population registers obtained from 1840-1860s. These registers contain demographic information about the male population. There are population-place start symbols, individuals and households. A sample that shows different types of objects in these registers can be found below figure:

![NFS_d___01454_00030 (1)](https://user-images.githubusercontent.com/4293082/114822724-2a633a00-9dcb-11eb-8076-8cad5ac64f9c.png)

Over 500000 people were read manually and entered Microsoft Access Databases. In this project, we annotated individuals and populated place names to train CNN models in these registers. See example below:

![NFS_d___01452_00002](https://user-images.githubusercontent.com/4293082/114823044-a1003780-9dcb-11eb-9fbb-2e5be4548b62.png)

The annotated datasets can be found :

Zistovi/images
Zistovi/labels

or 

İznik_images
İznik_labels

folders. To the training Python script, you have to provide path to original images, path to annotated images and a classes text files. You can select the pretrained model
as Unet or Resnet50 architecture. Furthermore, you can select whether to use GPU. For more information see dhSegment toolbox:

Sofia Ares Oliveira, Benoit Seguin, and Frederic Kaplan. Dhsegment: a generic deep-learning approach for document segmentation. In Frontiers in Handwriting Recognition (ICFHR), 2018 16th International Conference on, 7–12. IEEE, 2018.

[The training file is:](train_iznik_villages.py)
