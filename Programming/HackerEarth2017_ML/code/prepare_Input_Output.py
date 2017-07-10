import json
import pandas as pd
#import scipy.io as sio
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

def writeY(series):
    f = open(".\\Y.txt","w")
    size = len(series)

    for item in series:
        if item == 'neg':
            f.write('0')
            f.write("\n")
        elif item == 'pos':
            f.write('1')
            f.write("\n")
            

def whichFeatureIndex(value,coloumnList):
    l = list(coloumnList)
    for i in range(0,len(l)):
        item = l[i]
        if value == item:
            return i

def writeXFile(f, xi):
    for item in xi:
        f.write(',')
        f.write(str(item))
        

def writeXnew(dataframe,inputColoumns,OutFileName):
    m = len(dataframe)
    numColoumns = len(inputColoumns)
    uniqueColoumns = []
    n = 0
    #XX = []

    for index in range(0,numColoumns):
        unique_col = readUniqueData(inputColoumns[index])
        uniqueColoumns.append(unique_col)
        n = n + len(unique_col)
    
    newSize = m/10
    start = 0
    end = int(newSize)
    for upperI in range (0,10):
    
        f = open(OutFileName+str(upperI),"w")
        for index in range(start,end):
            Xi = [] #[0]*n
            
            for index1 in range(0,numColoumns):
                unique = uniqueColoumns[index1]
                series = dataframe[inputColoumns[index1]]
                Xl = [0]*len(unique)
                pStr = parseString(series[index])
                #f.write(series[index])
                #f.write("\n")
                for index2 in range(0,len(pStr)):
                    ind = whichFeatureIndex(pStr[index2][0],unique)
                    Xl[ind] = pStr[index2][1][0]
                    #print (pStr[index2][0])
                    #print (pStr[index2][1])

                Xi = Xi + Xl
            writeXFile(f,Xi)
            f.write("\n")
            #XX.append(Xi)
        start = end
        end = end + int(newSize)

    #sio.savemat("XX.mat",{'X':XX})        
        
        

def writeX(dataframe,inputColoumns,OutFileName):
    m = len(dataframe)
    numColoumns = len(inputColoumns)
    uniqueColoumns = []
    n = 0
    #XX = []


    for index in range(0,numColoumns):
        unique_col = readUniqueData(inputColoumns[index])
        uniqueColoumns.append(unique_col)
        n = n + len(unique_col)
    
    f = open(OutFileName,"w")

    for index in range(0,m):
        Xi = [] #[0]*n
        
        for index1 in range(0,numColoumns):
            unique = uniqueColoumns[index1]
            series = dataframe[inputColoumns[index1]]
            Xl = [0]*len(unique)
            pStr = parseString(series[index])
            #f.write(series[index])
            #f.write("\n")
            for index2 in range(0,len(pStr)):
                ind = whichFeatureIndex(pStr[index2][0],unique)
                Xl[ind] = pStr[index2][1][0]
                #print (pStr[index2][0])
                #print (pStr[index2][1])

            Xi = Xi + Xl
        writeXFile(f,Xi)
        f.write("\n")
        #XX.append(Xi)

    #sio.savemat("XX.mat",{'X':XX})

def writeX_genres(series):
    m = len(series)
    unique_genres = readUniqueData() #parseColoumn(series)
    n = len(unique_genres)
    f = open(".\\X_genres.txt","w")

    for index in range(0,m):
        Xi = [0]*n
        pStr = parseString(series[index])
        for index1 in range(0,len(pStr)):
            ind = whichFeatureIndex(pStr[index1][0],unique_genres)
            Xi[ind] = pStr[index1][1]

        writeXFile(f,Xi)
        f.write("\n")



def readUniqueData(coloumnName):
    # for genres
    fileName = ".\\data\\train_"
    fileName = fileName + coloumnName + ".txt"
    f  = open(fileName,"r")
    data = []
    for line in f:
        data.append(line.rstrip('\n'))
        
    return data


def main1():
    dataframe = readFile(".\\5f828822-4--4-hotstar_dataset\\train_data.json")
    
    #inputColoumns = ["genres","dow","tod"]
    #OutFileName = ".\\X_3_g_d_t.txt"
    #writeX(dataframe,inputColoumns,OutFileName)
    
    #inputColoumns = ["genres","cities","dow"]
    #OutFileName = ".\\X_3_g_c_d.txt"
    #writeX(dataframe,inputColoumns,OutFileName)
    
    #inputColoumns = ["genres","cities","tod"]
    #OutFileName = ".\\X_3_g_c_t.txt"
    #writeX(dataframe,inputColoumns,OutFileName)
    
    #inputColoumns = ["genres","cities"]
    #OutFileName = ".\\X_2_g_c.txt"
    #writeX(dataframe,inputColoumns,OutFileName)
    
    #inputColoumns = ["genres","dow"]
    #OutFileName = ".\\X_2_g_d.txt"
    #writeX(dataframe,inputColoumns,OutFileName)
    
    #inputColoumns = ["titles"]
    #OutFileName = ".\\X_1_t.txt"
    #writeXnew(dataframe,inputColoumns,OutFileName)
    
    inputColoumns = ["genres","cities","dow","tod","titles"]
    OutFileName = ".\\X_5_g_c_d_t_t.txt"
    writeXnew(dataframe,inputColoumns,OutFileName)
    
    
    #writeX_genres(dataframe['genres'])
    #writeY(dataframe['segment'])


main1()
