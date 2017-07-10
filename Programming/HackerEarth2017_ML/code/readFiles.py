import json
import pandas as pd
import re

def readFile(fileName):
    
    with open(fileName, 'r') as jsonfile1:
        data_dict = json.load(jsonfile1)

    t = pd.DataFrame.from_dict(data_dict, orient='index')
    #t.reset_index(level=0, inplace=True)
    t.rename(columns = {'index':'ID'},inplace=True)
    t.shape
    return t

def writeFile(fileName,data):
    f = open(fileName,'w')
    for item in data:
        f.write(item)
        f.write("\n")

#       a = 'delhi:45;mumbai:34;bengaluru:67'
#       In [7]: list(map(lambda x:x.split(':'), a.split(';')))
#       Out[7]: [['delhi', '45'], ['mumbai', '34'], ['bengaluru', '67']]
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
    
def parseColoumn(series):

    size = len(series)
    uniqueColoumnEntries = set()
    for index in range(0,size):
        pStr = parseString(series[index])
        for index1 in range(0,len(pStr)):
            uniqueColoumnEntries.add(pStr[index1][0])

    return uniqueColoumnEntries

def handleFile(fileName):
    dataFrame = readFile(fileName)
    
    #uniqueCities = parseColoumn(dataFrame['cities'])
    #writeFile(".\\train_cities.txt",uniqueCities)
    
    uniqueTitles = parseColoumn(dataFrame['titles'])
    writeFile(".\\train_titles.txt",uniqueTitles)
    
    #uniqueGenres = parseColoumn(dataFrame['genres'])
    #writeFile(".\\train_genres.txt",uniqueGenres)
    
    #uniqueTod = parseColoumn(dataFrame['tod'])
    #writeFile(".\\train_tod.txt",uniqueTod)
    
    #uniqueDow = parseColoumn(dataFrame['dow'])
    #writeFile(".\\train_dow.txt",uniqueDow)

    
def main():

    handleFile(".\\5f828822-4--4-hotstar_dataset\\train_data.json")
    #handleFile(".\\5f828822-4--4-hotstar_dataset\\test_data.json")

main()



