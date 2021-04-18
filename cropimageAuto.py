from PIL import Image
import pandas as pd
import numpy as np


accessDataset=pd.read_csv('merged_access_CV.csv');

count=0
for index, row in accessDataset.iterrows():
    oneDigit=False
    if(int(row['FileNo'])<10):
        oneDigit=True;
    DefterNo=str(int(row['DefterNo']))
    FileNo=str(int(row['FileNo']))
    ID=row['ID']
    NumcoordW0=row['NumcoordW0']
    NumcoordH0=row['NumcoordH0']
    NumcoordW1=row['NumcoordW1']
    NumcoordH1=row['NumcoordH1']
    NumcoordW2=row['NumcoordW2']
    NumcoordH2=row['NumcoordH2']
    NumcoordW3=row['NumcoordW3']
    NumcoordH3=row['NumcoordH3']

    minHeight=min(NumcoordH0,NumcoordH1,NumcoordH2,NumcoordH3)
    maxHeight = max(NumcoordH0, NumcoordH1, NumcoordH2, NumcoordH3)
    minWidth=min(NumcoordW0,NumcoordW1,NumcoordW2,NumcoordW3)
    maxWidth = max(NumcoordW0, NumcoordW1, NumcoordW2, NumcoordW3)

    if(oneDigit):
        FileNo="0"+FileNo
    image = "NFS_2865_Manisa/NFS_d___0"+DefterNo+"_"+"000"+FileNo+".jpg"
    original_img = Image.open(image)
    width, height = original_img.size
    cropped = original_img.crop((minWidth, minHeight, maxWidth, maxHeight))
    GroundTruthNumber=0
    if(row['IsIndividual']==1):
        GroundTruthNumber=int(row['PersonNumberRegistered'])
    if (row['IsHousehold'] == 1):
        GroundTruthNumber = int(row['Menzil'])
    if (row['IsBottom'] == 1):
        if(row['Age'] == '_unspecified' or row['Age'] == '_undeciphered' or pd.isna(row['Age'])):
            GroundTruthNumber=999;
        else:
            GroundTruthNumber = int(row['Age'])
    cropped.save("croppedNumbers/"+str(DefterNo)+"_"+str(FileNo)+"_"+str(ID)+"_GT"+str(GroundTruthNumber)+".jpg")

print("Done!")