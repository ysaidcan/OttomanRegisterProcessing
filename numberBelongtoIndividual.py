import pandas as pd
import numpy as np


def doOverlap(NumcoordH0,NumcoordH1,NumcoordH2,NumcoordH3,NumcoordW0,NumcoordW1,NumcoordW2,NumcoordW3,coordH0,coordH1,coordH2,coordH3,coordW0,coordW1,coordW2,coordW3):
    # If one rectangle is on left side of other
    avgNumH=NumcoordH0+NumcoordH1+NumcoordH2+NumcoordH3;
    avgNumH=avgNumH/4
    avgNumW= NumcoordW0+NumcoordW1+NumcoordW2+NumcoordW3;
    avgNumW=avgNumW/4
    if (min(coordH0,coordH1,coordH2,coordH3)  < avgNumH <max(coordH0,coordH1,coordH2,coordH3) and min(coordW0,coordW1,coordW2,coordW3) < avgNumW<max(coordW0,coordW1,coordW2,coordW3)):
        return True
    else:
        return False


def isLeftI(NumcoordH0,NumcoordH1,NumcoordH2,NumcoordH3,NumcoordW0,NumcoordW1,NumcoordW2,NumcoordW3,coordH0,coordH1,coordH2,coordH3,coordW0,coordW1,coordW2,coordW3):
    # If one rectangle is on left side of other
    avgNumH=NumcoordH0+NumcoordH1+NumcoordH2+NumcoordH3;
    avgNumH=avgNumH/4
    avgNumW= NumcoordW0+NumcoordW1+NumcoordW2+NumcoordW3;
    avgNumW=avgNumW/4
    minH=min(coordH0,coordH1,coordH2,coordH3)
    maxH=max(coordH0,coordH1,coordH2,coordH3)
    maxW=max(coordW0,coordW1,coordW2,coordW3)
    minW=min(coordW0,coordW1,coordW2,coordW3)
    meanW=  ( maxW+minW ) / 2
    meanH = (maxH + minH) / 2

    if ( minH < avgNumH < meanH and  minW < avgNumW< meanW):
        return True
    else:
        return False


def isRightH(NumcoordH0,NumcoordH1,NumcoordH2,NumcoordH3,NumcoordW0,NumcoordW1,NumcoordW2,NumcoordW3,coordH0,coordH1,coordH2,coordH3,coordW0,coordW1,coordW2,coordW3):
    # If one rectangle is on left side of other
    avgNumH=NumcoordH0+NumcoordH1+NumcoordH2+NumcoordH3;
    avgNumH=avgNumH/4
    avgNumW= NumcoordW0+NumcoordW1+NumcoordW2+NumcoordW3;
    avgNumW=avgNumW/4
    minH=min(coordH0,coordH1,coordH2,coordH3)
    maxH=max(coordH0,coordH1,coordH2,coordH3)
    maxW=max(coordW0,coordW1,coordW2,coordW3)
    minW=min(coordW0,coordW1,coordW2,coordW3)
    meanW=  ( maxW+minW ) / 2
    meanH = (maxH + minH) / 2


    if ( minH < avgNumH < meanH and  meanW < avgNumW< maxW):
        return True
    else:
        return False


def isBottomA(NumcoordH0,NumcoordH1,NumcoordH2,NumcoordH3,NumcoordW0,NumcoordW1,NumcoordW2,NumcoordW3,coordH0,coordH1,coordH2,coordH3,coordW0,coordW1,coordW2,coordW3):
    # If one rectangle is on left side of other
    avgNumH=NumcoordH0+NumcoordH1+NumcoordH2+NumcoordH3;
    avgNumH=avgNumH/4
    avgNumW= NumcoordW0+NumcoordW1+NumcoordW2+NumcoordW3;
    avgNumW=avgNumW/4
    minH=min(coordH0,coordH1,coordH2,coordH3)
    maxH=max(coordH0,coordH1,coordH2,coordH3)
    maxW=max(coordW0,coordW1,coordW2,coordW3)
    minW=min(coordW0,coordW1,coordW2,coordW3)
    meanW=  ( maxW+minW ) / 2
    meanH = (maxH + minH) / 2
    if ( meanH < avgNumH < maxH ):
        return True
    else:
        return False

iznik_individuals=pd.read_csv('individuals_with_rows.csv');

iznik_individuals=iznik_individuals.sort_values(by=['personID'])

numbersRecognized=pd.read_csv('recognized_numbers.csv');


NumregisterID = numbersRecognized.iloc[:, 0]
NumPageNum = numbersRecognized.iloc[:, 1]
NumobjType = numbersRecognized.iloc[:, 2]
NumavgW = numbersRecognized.iloc[:, 3]
NumavgH = numbersRecognized.iloc[:, 4]
NumisLeft = numbersRecognized.iloc[:, 5]
NumisEdge = numbersRecognized.iloc[:, 6]
NumcoordW0 = numbersRecognized.iloc[:, 7]
NumcoordH0 = numbersRecognized.iloc[:, 8]
NumcoordW1 = numbersRecognized.iloc[:, 9]
NumcoordH1 = numbersRecognized.iloc[:, 10]
NumcoordW2 = numbersRecognized.iloc[:, 11]
NumcoordH2 = numbersRecognized.iloc[:, 12]
NumcoordW3 = numbersRecognized.iloc[:, 13]
NumcoordH3 = numbersRecognized.iloc[:, 14]


registerID = iznik_individuals.iloc[:, 0]
PageNum = iznik_individuals.iloc[:, 1]
objType = iznik_individuals.iloc[:, 2]
avgW = iznik_individuals.iloc[:, 3]
avgH = iznik_individuals.iloc[:, 4]
isLeft = iznik_individuals.iloc[:, 5]
isEdge = iznik_individuals.iloc[:, 6]
coordW0 = iznik_individuals.iloc[:, 7]
coordH0 = iznik_individuals.iloc[:, 8]
coordW1 = iznik_individuals.iloc[:, 9]
coordH1 = iznik_individuals.iloc[:, 10]
coordW2 = iznik_individuals.iloc[:, 11]
coordH2 = iznik_individuals.iloc[:, 12]
coordW3 = iznik_individuals.iloc[:, 13]
coordH3 = iznik_individuals.iloc[:, 14]
Row = iznik_individuals.iloc[:, 15]
InPageID = iznik_individuals.iloc[:, 16]
PersonID = iznik_individuals.iloc[:,17]



sessionMat=np.zeros((len(NumcoordH3),31),dtype=float)
sessionMat.fill(np.nan)

for j in range(0,len(NumcoordW3)):
    print("Processed ------%" + str(j/len(NumcoordH3)*100.0)+"\n")
    for i in range(0, len(PersonID)):
        if(doOverlap(NumcoordH0[j],NumcoordH1[j],NumcoordH2[j],NumcoordH3[j],NumcoordW0[j],NumcoordW1[j],NumcoordW2[j],NumcoordW3[j],coordH0[i],coordH1[i],coordH2[i],coordH3[i],coordW0[i],coordW1[i],coordW2[i],coordW3[i]) and NumPageNum[j]==PageNum[i] and NumregisterID[j]==registerID[i]):
            isIndividual=isLeftI(NumcoordH0[j], NumcoordH1[j], NumcoordH2[j], NumcoordH3[j], NumcoordW0[j], NumcoordW1[j],
                      NumcoordW2[j], NumcoordW3[j], coordH0[i], coordH1[i], coordH2[i], coordH3[i], coordW0[i],
                      coordW1[i], coordW2[i], coordW3[i])
            isHousehold=isRightH(NumcoordH0[j], NumcoordH1[j], NumcoordH2[j], NumcoordH3[j], NumcoordW0[j], NumcoordW1[j],
                      NumcoordW2[j], NumcoordW3[j], coordH0[i], coordH1[i], coordH2[i], coordH3[i], coordW0[i],
                      coordW1[i], coordW2[i], coordW3[i])
            isBottom=isBottomA(NumcoordH0[j], NumcoordH1[j], NumcoordH2[j], NumcoordH3[j], NumcoordW0[j], NumcoordW1[j],
                      NumcoordW2[j], NumcoordW3[j], coordH0[i], coordH1[i], coordH2[i], coordH3[i], coordW0[i],
                      coordW1[i], coordW2[i], coordW3[i])
            sessionMat[j,0]=NumregisterID[j]
            sessionMat[j, 1] = NumPageNum[j]
            sessionMat[j, 2] = NumobjType[j]
            sessionMat[j,3] = NumavgW[j]
            sessionMat[j,4] = NumavgH[j]
            sessionMat[j,5] = isLeft[i]
            sessionMat[j,6] = isEdge[i]
            sessionMat[j,7]=NumcoordW0[j]
            sessionMat[j,8]=NumcoordH0[j]
            sessionMat[j,9]=NumcoordW1[j]
            sessionMat[j, 10] = NumcoordH1[j]
            sessionMat[j, 11] = NumcoordW2[j]
            sessionMat[j, 12] = NumcoordH2[j]
            sessionMat[j,13] = NumcoordW3[j]
            sessionMat[j, 14] = NumcoordH3[j]
            sessionMat[j, 15] = 1/avgW[i]
            sessionMat[j, 16] = avgH[i]
            sessionMat[j, 17] = coordW0[i]
            sessionMat[j, 18] = coordH0[i]
            sessionMat[j, 19] = coordW1[i]
            sessionMat[j, 20] = coordH1[i]
            sessionMat[j, 21] = coordW2[i]
            sessionMat[j, 22] = coordH2[i]
            sessionMat[j, 23] = coordW3[i]
            sessionMat[j, 24] = coordH3[i]
            sessionMat[j, 25] = Row[i]
            sessionMat[j, 26] = InPageID[i]
            sessionMat[j, 27] = PersonID[i]
            sessionMat[j, 28] = isIndividual
            sessionMat[j, 29] = isHousehold
            sessionMat[j, 30] = isBottom




dataset = pd.DataFrame({'NumregisterID':sessionMat[:,0],'NumPageNum':sessionMat[:,1],'NumobjType':sessionMat[:,2],'NumavgW':sessionMat[:,3],'NumavgH':sessionMat[:,4],
'NumisLeft':sessionMat[:,5],'NumisEdge':sessionMat[:,6],'NumcoordW0':sessionMat[:,7],'NumcoordH0':sessionMat[:,8],
'NumcoordW1':sessionMat[:,9],'NumcoordH1':sessionMat[:,10],'NumcoordW2':sessionMat[:,11],'NumcoordH2':sessionMat[:,12],'NumcoordW3':sessionMat[:,13],
'NumcoordH3': sessionMat[:, 14],'avgW': sessionMat[:, 15], 'avgH': sessionMat[:, 16], 'coordW0': sessionMat[:, 17],
'coordH0': sessionMat[:, 18], 'coordW1': sessionMat[:, 19], 'coordH1': sessionMat[:, 20], 'coordW2': sessionMat[:, 21],
'coordH2': sessionMat[:, 22], 'coordW3': sessionMat[:, 23],'coordH3': sessionMat[:, 24],'Row': sessionMat[:, 25], 'InPageID': sessionMat[:, 26], 'Lab_sub': sessionMat[:, 27],'IsIndividual': sessionMat[:, 28], 'IsHousehold': sessionMat[:, 29], 'IsBottom': sessionMat[:, 30]})

dataset.dropna(axis=0, how='any', inplace=True)

dataset.to_csv('numbers_individuals_combined_alternative.csv', encoding='utf-8')



