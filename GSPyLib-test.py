import os
import urllib
import mechanize
import re

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'chrome')]


os.chdir("/Users/KristinDay/Desktop")

#read in the dictionary of legal terms - this will be set x
reader = csv.reader(open('INOpinDict.csv', 'rb'))
INOpinDict = dict(reader)

#read in the dictionary of user question words - this will be set y
reader = csv.reader(open('UserQDict.csv', 'rb'))
UserQDict = dict(reader)

def NGD(words, print = FALSE, list = FALSE):
    #make sure words is a 2 item list
    if(len(words) != 2):
        print("Error: words doesn't have 2 items")
    else:
        continue

    M = 8058044651 # num of web pages searched by google in 2007

    for key in UserQDict:
        x = key
        for target in INOpinDict:
            y = target

            freq.x = getGoogleCount(x, language=language)
            freq.y = getGoogleCount(y, language=language)
            freq.xy = getGoogleCount(c(x,y), language=language)

def getGoogleCount(x, y, language="en"):
    entry = x + '+' + y
    query = "https://www.google.com/search?sclient=psy-ab&site=&source=hp&q=" + entry + "&oq=" + entry
    # start extraction at indicator word position
    p = re.compile("of about", re.MULTILINE | re.DOTALL)
    posExtractStart = p.findall()