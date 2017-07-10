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
    #parsedStr = list(map(lambda x:x.split(':'), str.split(',')))
    #return parsedStr
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

def whichFeatureIndex(value,coloumnList):
    l = list(coloumnList)
    for i in range(0,len(l)):
        item = l[i]
        if value == item:
            return i
            
    return -1        

def writeSparseRowInFile(f, row, coloumn, value):
    f.write(str(row))
    f.write(" ")
    f.write(str(coloumn))
    f.write(" ")
    f.write(str(value))
    f.write("\n")

def writeX(dataframe,inputColoumns,OutFileName):
    m = len(dataframe)
    numColoumns = len(inputColoumns)
    uniqueColoumns = []
    n = 0

    for index in range(0,numColoumns):
        unique_col = readUniqueData(inputColoumns[index])
        uniqueColoumns.append(unique_col)
        n = n + len(unique_col)
    
    f = open(OutFileName,"w")

    for index in range(0,m):
        shiftIndex = 0
        for index1 in range(0,numColoumns):
            unique = uniqueColoumns[index1]
            series = dataframe[inputColoumns[index1]]
            pStr = parseString(series[index])
            
            for index2 in range(0,len(pStr)):
                ind = whichFeatureIndex(pStr[index2][0],unique)
                if ind != -1:
                    Xrow = index+1
                    Xcoloumn = ind+1+shiftIndex
                    Xvalue = pStr[index2][1][0]
                    writeSparseRowInFile(f,Xrow,Xcoloumn,Xvalue)
            
            shiftIndex = shiftIndex + len(unique)        


def readUniqueData(coloumnName):
    # for genres
    fileName = ".\\data\\train_"
    fileName = fileName + coloumnName + ".txt"
    f  = open(fileName,"r")
    data = []
    for line in f:
        data.append(line.rstrip('\n'))
        
    return data


def main():
    dataframe = readFile(".\\5f828822-4--4-hotstar_dataset\\train_data.json")
    
    
    #inputColoumns = ["genres","dow"]
    #OutFileName = ".\\X_2_g_d_sparse.txt"
    #writeX(dataframe,inputColoumns,OutFileName)
    
    inputColoumns = ["genres","cities","dow","tod","titles"]
    OutFileName = ".\\X_5_g_c_d_t_t_sparse.txt"
    writeX(dataframe,inputColoumns,OutFileName)
    
    

main()
