

from smallCompanyType import smallCompanyType as s 

b=s.SmallCompanyType()


texts=["Lemay.ai Hotel","Farah's variety","felding and associates","Lemay.ai Consulting"]

for text in texts:
    ctype = b.getCompanyType(text)
    csubtype = b.getCompanySubtype(text)
    print(text,"is a",ctype,csubtype)
