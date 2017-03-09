import random
import multiprocessing
import timeit
import os
from time import time

debug = True

def list_append(count, out_list):
	if (debug == True):
		print "main pid:" + str(os.getpid()	)
	for i in range(count):
		out_list.append(random.random())

if __name__ == "__main__":

	size = 10000000
	jobs = []
	out_list = list()

	starttime = time()
	if (debug == True):
		print "main pid:" + str(os.getpid()	)
	process = list_append (size, out_list)
	singletime = time() - starttime

	starttime = time()
	if (debug == True):
		print "main pid:" + str(os.getpid()	)
	process = multiprocessing.Process(target=list_append, args=(size, out_list))
	jobs.append(process)


	for j in jobs:
		j.start()

	for j in jobs:
		j.join()

	multitime = time() - starttime

	if (debug == True):
		print "single processing: " + str(round(singletime, 2))
		print "multi processing: " + str(round(multitime, 2))
		print str((100 - ((round(singletime, 2)/round(multitime, 2)) * 100)) * -1)
