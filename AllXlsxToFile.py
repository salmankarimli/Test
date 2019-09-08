import os
import glob
import pandas
hardan=input("excel fayllarin yerleshdiyi papkasni yazin (mes. e:\Folder) ===>")
hara=input("excel fayllari cemleyenden sonra saxlanilacaq yer (mes e:\cemfayl.xlsx) ===>")

def concatenate(indir,outfile):
    os.chdir(indir)
    fileList=glob.glob("*.xlsx")
    dfList=[]

    i=1
    for filename in fileList:
        print(i,filename)
        i=i+1
        df=pandas.read_excel(filename,header=0)
        dfList.append(df)
    concatDF=pandas.concat(dfList,axis=0)
    concatDF.to_excel(outfile,index=None)

concatenate(hardan,hara) 