import pandas as pd
import random

#raw_trees=pd.read_csv("FinalOverObTableWAR.csv")

fields = ['CLUSTER',
'ID',
'tree_obs_id',
'tree_spp',
'tree_dbh',
'tree_stems',
'tree_height',
'tree_crown_class',
'tree_stems_per',
'tree_ba',
'stand_id',
'OverOb_wOverIDForTypBAFGrndPresCrzrSoilWet_over_id'
]

reduced_data = pd.read_csv("FinalOverObTableWAR.csv", usecols = fields)

#single plot for testing
df2 = reduced_data[reduced_data['OverOb_wOverIDForTypBAFGrndPresCrzrSoilWet_over_id'] == 'POKWAR047']

df2['tree_height_cont'] = df2['tree_height'] + [random.random() for _ in range(0, len(df2))]





#full working versions
reduced_data['tree_height_cont'] = reduced_data['tree_height'] + [random.random() for _ in range(0, len(reduced_data))]

reduced_data['ht_percentile_stand'] = reduced_data.groupby('stand_id')['tree_height_cont'].rank(pct=True)
reduced_data['BA_percentile_stand'] = reduced_data.groupby('stand_id')['tree_ba'].rank(pct=True)

reduced_data['ht_percentile_plot'] = reduced_data.groupby('OverOb_wOverIDForTypBAFGrndPresCrzrSoilWet_over_id')['tree_height_cont'].rank(pct=True)
reduced_data['BA_percentile_plot'] = reduced_data.groupby('OverOb_wOverIDForTypBAFGrndPresCrzrSoilWet_over_id')['tree_ba'].rank(pct=True)



#BAL - Basal area in trees larger - not working yet

df2['BAL']=df2['tree_ba'].gt(df2['tree_ba']).sum()

sum(df2['tree_ba'])
