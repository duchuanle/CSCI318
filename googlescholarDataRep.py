import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import scholarly
import xml.etree.ElementTree as ET
tree = ET.parse(test.xml)


def howManyHyphens(title):
    return title.count('-');


def main():
    search_query = scholarly.search_pubs_query('Perception');

    objects = ('0','1','2','3','4','>4');
    y_pos = np.arange(len(objects))
    citationCount = [0,0,0,0,0,0]
    articleCount = [0,0,0,0,0,0]
    for index,x in zip(range(10),search_query):
        print(x)
        hyphenCount = howManyHyphens(x.bib["title"])
        if(hyphenCount == 0):
            citationCount[0] += x.citedby
            articleCount[0] += 1
        elif(hyphenCount == 1):
            citationCount[1] += x.citedby
            articleCount[1] += 1
        elif(hyphenCount == 2):
            citationCount[2] += x.citedby
            articleCount[2] += 1
        elif(hyphenCount == 3):
            citationCount[3] += x.citedby
            articleCount[3] += 1
        elif(hyphenCount == 4):
            citationCount[4] += x.citedby
            articleCount[4] += 1
        elif(hyphenCount >= 5):
            citationCount[5] += x.citedby
            articleCount[5] += 1


    meanCitationCount = citationCount
    print(*citationCount)
    for num,citeCount in enumerate(meanCitationCount,start=0):
        if(articleCount[num] != 0):
            meanCitationCount[num] = citeCount/articleCount[num]

    print(*meanCitationCount)
    
    plt.bar(y_pos,citationCount,align = 'center', alpha = 0.5)
    plt.xticks(y_pos,objects)
    plt.ylabel('Mean Citation Count')
    plt.title('Mean Citation Count and Hyphens')

    plt.show()
    

main()




