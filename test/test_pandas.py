import glob
import pandas as pd
from IPython.display import display
import smallCompanyType as s
b=s.SmallCompanyType()
files = glob.glob('TargetBusinesses_*.csv')
#files = 'TargetBusinesses_Colonnade.csv'

def getCategory(row):
    row["Type"]=b.getCompanyType(row["name"])
    row["Subtype"]=b.getCompanySubtype(row["name"])
    return row

for file in files:
    df = pd.read_csv(file)
    df=df.apply(getCategory, axis=1)
    print(df[['name','Type','Subtype']])
