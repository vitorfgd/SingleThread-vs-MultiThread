import primes_until_serial
import primes_until_parallel
from time import time

debug = True

if __name__ == '__main__':
    starttime = time()
    primes_until_serial.run_primes_serial ()
    singletime = time() - starttime
    starttime = time()
    primes_until_parallel.run_primes_parallel ()
    multitime = time() - starttime

    if (debug == True):
        print "single processing: " + str(round(singletime, 2))
        print "multi processing: " + str(round(multitime, 2))
        print str((100 - ((round(singletime, 2)/round(multitime, 2)) * 100)) * -1)
