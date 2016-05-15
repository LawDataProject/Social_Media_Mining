import os
import shutil
import re
import csv

os.chdir("/Users/KristinDay/Desktop/IN-gov-txts")


f = open('1.txt')
f = f.read().lower()
p = re.compile('.*?_', re.MULTILINE | re.DOTALL)
f = p.sub('', f)
g = re.compile('\\n', re.MULTILINE | re.DOTALL)
f = g.sub(' ', f)
d = re.compile('[^ \'a-zA-Z\\-]', re.MULTILINE | re.DOTALL) #need to fix this expression so that white space is kept
f = d.sub(' ', f)
#print(f)
e = re.compile('\d', re.MULTILINE | re.DOTALL)
f = e.sub('', f)
#print(f)

# create dictionary from myfile text
from collections import defaultdict


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


TestDict = get_word_space(f)


os.chdir("/Users/KristinDay/Desktop")

z = open('INOpinDict.txt', "w", newline='')
#w = csv.DictWriter(z, fieldnames=TestDict.keys(), restval='0', extrasaction='ignore')
z.write(TestDict)
z.close()

#writer = csv.writer(open('INOpinDict.csv', 'wb', newline=''))
#for key, value in TestDict.items():
    #writer.writerow([key, value])