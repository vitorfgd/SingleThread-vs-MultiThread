from multiprocessing import Pool
from random import choice
from string import printable
from time import time

debug = True

def build_test_list():
    testlist = [[], [], [], [], []]
    for sublist in testlist:
        for _ in xrange(5000):
            sublist.append(''.join(choice(printable) for i in xrange(20)))
    return testlist

def process_list(l):
    result = []
    tmp = []
    for n in range(len(l)):
        if l[n] not in tmp:
            result.insert(n, l[n]+' ('+str(l.count(l[n]))+')')
            tmp.insert(0, l[n])
    return result

def single(l):
    results = []
    for sublist in l:
        results.append(process_list(sublist))
    return results

def multi(l):
    pool = Pool()
    results = pool.map(process_list, l)
    return results

testlist = build_test_list()

#here starts the single processing
starttime = time()
singleresults = single(testlist)
singletime = time() - starttime

#here starts the multiprocessing processing
starttime = time()
multiresults = multi(testlist)
multitime = time() - starttime

if (debug == True):
    print "{0:.2f}sec".format(singletime)
    print "{0:.2f}sec".format(multitime)
    print str((100 - ((round(singletime, 2)/round(multitime, 2)) * 100)) * -1)
