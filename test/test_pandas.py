import glob
import pandas as pd
from IPython.display import display

import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from companyClassifier import companyClassifier as s

b=s.CompanyClassifier()
files = glob.glob('TargetBusinesses_*.csv')
#files = 'TargetBusinesses_Colonnade.csv'

def getCategory(row):
    resultsDict = b.classifyCompany([row["name"]])
    row["Type"]=resultsDict["type"][row["name"]]
    row["Subtype"]=resultsDict["subtype"][row["name"]]
    return row

for file in files:
    df = pd.read_csv(file)
    df=df.apply(getCategory, axis=1)
    print(df[['name','Type','Subtype']])
