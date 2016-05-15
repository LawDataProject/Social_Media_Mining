import os
import urllib2
from json import loads
import math
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross-validation
import re
from urlparse import urlparse
from xgoogle.search import GoogleSearch, SearchError
import pandas as pd

def fetch_data(source_url):
    request = urllib2.urlopen(request)


os.chdir("/Users/KristinDay/Desktop/xgoogle")

#read in the dictionary of legal terms - this will be set x
reader = csv.reader(open('INOpinDict.csv', 'rb'))
INOpinDict = dict(reader)

#read in the dictionary of user question words - this will be set y
reader = csv.reader(open('UserQDict.csv', 'rb'))
UserQDict = dict(reader)

# HELPER
def fetch_data(source_url):
	request = urllib2.Request(source_url)
	try:
		response = urllib2.urlopen(request)
		data = response.read()
		return (data, source_url)
	except urllib2.URLError, e:
		return (None, e)

def save_data(data, filename):
	fh = open(filename, "w")
	fh.write(data)

def get_hits(term):
	#data = fetch_data("http://api.thriftdb.com/api.hnsearch.com/items/_search?q=" + term)
	#if data[0] is not None:
	#	if loads(data[0])['hits'] > 0:  #loads() dumps a json file which is what the hnsearch api returns
	#		return loads(data[0])['hits']
#		else:
#			return 0.000001
#	else:
#		return data[1]
    gs = GoogleSearch(key)
    gs.results_per_page = 100
    results = gs.get_results()
    return results

# Distance Measure
def normalized_index_distance(nr_results_x, nr_results_y, nr_results_x_y, index_size = 11200000):
    c_x = math.log(nr_results_x)
    c_y = math.log(nr_results_y)
    c_x_y = math.log(nr_results_x_y)
    c_m = math.log(index_size)
    return (max(c_x, c_y) - c_x_y) / (c_m - min(c_x, c_y))

hits = {}  # create an empty dict to save results
for key in UserQDict:
    for target in INOpinDict:
        # Code from Python Library
        #gs = GoogleSearch(key)
        #gs.results_per_page = 100
        #results = gs.get_results()
        hits[key] = get_hits(key)
        normalized_index_distance(hits[key], hits[target], get_hits(key + '+' + target))