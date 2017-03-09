#!/usr/bin/env python
# -*- coding: utf-8 -*-

from concurrent.futures import ProcessPoolExecutor, as_completed
import sys
import time


def gera_lprimos(ate_n):
    result = []
    for p in range(2, ate_n+1):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            result.append(p)
    return result

def run_serial(n):
	return({i: gera_lprimos(i) for i in range(1,n+1)})


def run_primes_serial():
    n = 1000
    run_serial(n)
