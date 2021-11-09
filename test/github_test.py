import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from companyClassifier import companyClassifier as s
import pytest

b=s.CompanyClassifier()


texts=["Lemay.ai Hotel","Farah's variety","felding and associates","Lemay.ai Consulting"]
ctypes_subtypes = b.classifyCompany(texts)

def test_results():
    for i in range(len(texts)):
        company = texts[i]
        if i == 0:
            assert ctypes_subtypes["type"][company] == 'B2BC'
            assert ctypes_subtypes["subtype"][company] == 'Hotel'
        elif i == 1:
            assert ctypes_subtypes["type"][company] == 'B2BC'
            assert ctypes_subtypes["subtype"][company] == 'Dealer'
        elif i == 2:
            assert ctypes_subtypes["type"][company] == 'B2BC'
            assert ctypes_subtypes["subtype"][company] == 'Financial Services'
        elif i ==3:
            assert ctypes_subtypes["type"][company] == 'B2BC'
            assert ctypes_subtypes["subtype"][company] == 'Computer Services'