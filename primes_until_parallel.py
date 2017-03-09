#!/usr/bin/env python
# -*- coding: utf-8 -*-

from concurrent.futures import ProcessPoolExecutor, as_completed
import sys
import time


def gera_lprimos(ate_n):
	result = []
	count=0
	for p in range(2, ate_n+1):
		for i in range(2, p):
			if p % i == 0:
				break
		else:
			result.append(p)
			count = count+1
	return result


def run_multiprocess(n):
	waits = {}

	with ProcessPoolExecutor() as executor:
		waits = {
			executor.submit(gera_lprimos, i) : i
			for i in range(1,n+1)
		}
		return({
			waits[processo]: processo.result()
			for processo in as_completed(waits)
		})

def run_primes_parallel():
    n = 1000
    x = run_multiprocess(n)
