import os
import shutil
import re

os.chdir("/Users/KristinDay/Desktop")
src_files = os.listdir("IN-gov-txts")
os.chdir("IN-gov-txts")
myfile = ''
for doc in src_files:
    f = open(doc)
    f = f.read().lower()
    p = re.compile('.*?_', re.MULTILINE | re.DOTALL)
    f = p.sub('', f)
    g = re.compile('\\n', re.MULTILINE | re.DOTALL)
    f = g.sub(' ', f)
    d = re.compile('[^ a-zA-Z\\-]', re.MULTILINE | re.DOTALL) #need to fix this expression so that white space is kept
    f = d.sub(' ', f)
    e = re.compile('\d', re.MULTILINE | re.DOTALL)
    f = e.sub('', f)
    myfile = myfile + ' ' + f

# create dictionary from myfile text
from collections import defaultdict


#create list of unique words from myfile
def get_word_space(data):
    word_space = ''
    data = data.split()
    for w in data:
        if len(word_space) == 0:
            word_space = w
        elif w not in word_space:
            word_space = word_space + ', ' + w
        else:
            continue
    return word_space

INOpinList = get_word_space(myfile)
#count number of unique words in list
print("length is ", len(INOpinList))

#write list to a text file
os.chdir("/Users/KristinDay/Desktop")
z = open('INOpinList.txt', "w", newline='')
z.write(INOpinList)
z.close()
