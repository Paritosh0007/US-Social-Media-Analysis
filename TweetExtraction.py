# Citation - www.stackoverflow.com



import json
with open('C:/Users/Sujatha Sivakumar/Desktop/Spring2017/DataScience/TrumpTweets.json', 'r') as f:
    text=[]
    counter=0
    my_output_file = open("TrumpExtractGeneral.txt","w")
    for row in f.read().split("\n"):
        text = row.split("\",\"")
        if(len(text)>2):   
           counter+= 1                 
           my_output_file.write(text[2].split("\":\"")[1]+"\n")
    
    my_output_file.close()