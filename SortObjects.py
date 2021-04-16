import pandas as pd
import numpy as np

PIXELS_BETWEEN_ROWS=120

iznik_individuals=pd.read_csv('last_coordinates.csv');


iznik_individuals['avgW']= 1.0 / iznik_individuals['avgW'];

iznik_individuals=iznik_individuals.sort_values(by=['registerID','PageNum','avgH'],ignore_index=True)

rowNumber=np.zeros(len(iznik_individuals['avgH']))


pageArray=iznik_individuals['PageNum']
heightArray = iznik_individuals['avgH']


newRow = 0
previousRow = 0
currentRow = 0
for i in range (0, len(heightArray)):
    if i>0:
        if pageArray[i]!=pageArray[i-1]:
            previousRow = 0
            currentRow = 0
            newRow = 0

    currentRow=heightArray[i]
    if currentRow > previousRow + PIXELS_BETWEEN_ROWS:
        newRow=newRow+1;
    rowNumber[i]= newRow;
    previousRow=currentRow

print("Hello");

iznik_individuals['Row'] = rowNumber


iznik_individuals=iznik_individuals.sort_values(by=['registerID','PageNum', 'isLeft','Row', 'avgW'])

rowNumber=np.zeros(len(iznik_individuals['avgH']))


personID=np.zeros(len(iznik_individuals['avgH']))

personIDPage=np.zeros(len(iznik_individuals['avgH']))


newRow = 0
previousRow = 0
currentRow = 0
counter=1
for i in range (0, len(heightArray)):
    personID[i]=i+1
    if i>0:
        if pageArray[i]!=pageArray[i-1]:
            counter=1
    personIDPage[i]=counter
    counter=counter+1



iznik_individuals['personID'] = personID
iznik_individuals['personIDPage'] = personIDPage





iznik_individuals.to_csv("individuals_with_rows.csv");






