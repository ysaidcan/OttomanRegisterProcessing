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

[You can find the training file from this link](train_iznik_villages.py)

After you train your model, it will be saved to the provided output path. You can use the trained model for your test images. For that you will need demo files which can be found in:

[You can find the demo file from this link](demo_iznik.py)

It will output a csv file which includes pixelwise positions of the found objects. It will also draw boxes around detected objects. An example of a register page with detected objects is shown below:

![NFS_d___02865_00003_boxes](https://user-images.githubusercontent.com/4293082/114997273-543e5e80-9ea8-11eb-8251-f35817dafd74.jpg)

The detected objects can be sorted in a way that Arabic language requires. Arabic scripts start from the right top of the page. Therefore, sorting must be done in this way. Right top objects comes before. Another important point is that page is divided from the middle. Therefore, sorting must take into account this fact. Sorting script can be found below:

[You can find the sorting Python script from this link](SortObjects.py)

In some part of the Ottoman Population registers collected in 1840-1860, the age, person number and household number is written in red. To take advantage of this fact, we applied red color filter to spot the numerals. 

[You can find the red color mask Python script from this link](MaskAll.py)

The original image of an example register page and red filtered version is demonstrated at below figure.

![NFS_d___01452_00002](https://user-images.githubusercontent.com/4293082/115024083-47316780-9ec8-11eb-8123-9e5521cf8dd3.jpg)

A numeral spotting model can be trained by using the masked registers under the numerals folder. The model can be tested by using a demo script file. It will again marked the numerals on the document images and output a csv files for the locations of these numerals. A sample detected numerals in a register page can be found below:

[You can find the numeral recognition Python script](numberRecognition.py)

![NFS_d___02865_00003_masked_boxes](https://user-images.githubusercontent.com/4293082/115106232-3f2b0380-9f6c-11eb-991a-593607259e43.jpg)

[Numbers and individuals can be combined with this Python script. ] (numberBelongtoIndividual.py)










