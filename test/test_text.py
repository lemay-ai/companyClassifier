import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from companyClassifier import companyClassifier as s

b=s.CompanyClassifier()


texts=["Lemay.ai Hotel","Farah's variety","felding and associates","Lemay.ai Consulting"]
ctypes_subtypes = b.classifyCompany(texts)

for company in texts:
    print(company,"is a",ctypes_subtypes["type"][company],ctypes_subtypes["subtype"][company])
