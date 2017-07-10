import json
import pandas as pd
import numpy as np
import re


def readFile(fileName):
    
    with open(fileName, 'r') as jsonfile1:
        data_dict = json.load(jsonfile1)

    t = pd.DataFrame.from_dict(data_dict, orient='index')
    #t.reset_index(level='0', inplace=True)
    t.rename(columns = {'index':'ID'},inplace=True)
    t.shape
    return t

def parseString(str):
    if len(str) == 0:
        return []
    str = str + ","
    t1 = re.split('\:\d+\,',str)
    titles = list(filter(lambda x:x != '',t1))
    n = re.findall('\:\d+\,',str)
    timeinsec = list(map(lambda x:re.findall('\d+',x),n))
    parsedStr = []*len(titles)

    for iiii in range(0,len(titles)):
        p = ['']*2
        p[0] = titles[iiii]
        p[1] = timeinsec[iiii]
        parsedStr.append(p)

    return parsedStr    

def readUniqueData(coloumnName):
    fileName = ".\\data\\train_"
    fileName = fileName + coloumnName + ".txt"
    f  = open(fileName,"r")
    data = []
    for line in f:
        data.append(line.rstrip('\n'))
        
    return data

def whichFeatureIndex(value,coloumnList):
    l = list(coloumnList)
    for i in range(0,len(l)):
        item = l[i]
        if value == item:
            return i

def writeD(OutFileName,D):
    f = open(OutFileName,"w")
    
    for title,count in D.items():
        f.write(title)
        f.write(";")
        f.write(str(count))
        f.write("\n")

            
def findTopColoumns(series, uniqueData, OutFileName):

    m = len(series)
    D = {}
    for index in range(0,len(uniqueData)):
        D[uniqueData[index]] = 0
    
    for index in range(0,m):
        pStr = parseString(series[index])
            
        for index2 in range(0,len(pStr)):
            D[pStr[index2][0]] += int(pStr[index2][1][0])
    
    
    writeD(OutFileName,D)
    
    
def main():
    dataframe = readFile(".\\5f828822-4--4-hotstar_dataset\\train_data.json")
    OutFileName = ".\\top50titles.txt"
    series = dataframe["titles"]
    uniqueData = readUniqueData("titles")
    findTopColoumns(series, uniqueData, OutFileName)
    
    

main()
