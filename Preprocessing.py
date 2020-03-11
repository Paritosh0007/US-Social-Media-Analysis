#import HTMLParser
from html.parser import HTMLParser as h_p
import preprocessor as p
import re


filename = input("Enter The Text file name to be cleaned")

with open(filename+'.txt','r') as fileobj:
    data=fileobj.readlines()

writeobj = open(filename+'(Cleaned)'+'.txt', 'w')

for tline in data:
    print ('------' + tline)
    
   # tline=h_p.unescape(tline,"")
   # tline=h_p.decode("utf8").encode('ascii','ignore')
   # p.clean(tline)

    tline = tline.replace('\n','')  
    tline = ' '.join(re.sub("RT|http\S+|(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+|)","",tline).split())
    tline = re.sub(r'\b\d+\b', '', tline)
    
   #1 tline = ' '.join(re.sub("RT|@|https:|t.co|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tline).split())
   # tline = ' '.join(re.sub("RT|@|http\S+|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tline).split())
   # tline = ''.join(re.sub(r'^https?:\/\/.*[\r\n]*', "", tline, flags=re.MULTILINE).split()) 
    print ('******'+tline)
    writeobj.write(tline+'\n')
writeobj.close()
