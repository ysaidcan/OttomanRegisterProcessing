import pandas as pd

iznik_individuals=pd.read_csv(
    'numbers_individuals_combined_alternative.csv');


accessDataset=pd.read_csv(
    'NFS_Data_Manisa.csv');

iznik_individuals.DefterNo.astype(float)
iznik_individuals.FileNo.astype(float)
iznik_individuals.PersonInPage.astype(float)

accessDataset.DefterNo.astype(float)
accessDataset.FileNo.astype(float)
accessDataset.PersonInPage.astype(float)

result = pd.merge(iznik_individuals, accessDataset, on=['DefterNo', 'FileNo', 'PersonInPage'])

result.to_csv('merged_access_CV.csv', encoding='utf-8')
