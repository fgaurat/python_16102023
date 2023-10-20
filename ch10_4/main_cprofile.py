#!/usr/bin/env python
"""
Le module
"""
import cProfile
import re
import pstats
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG,format="%(asctime)s - %(levelname)s - %(name)s - %(filename)s:%(lineno)d - %(message)s")
"%(asctime)s - %(levelname)s - %(name)s - %(filename)s:%(lineno)d - %(message)s"


def is_prime(num):
    """
    is_prime
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def nth_prime(n):
    """
    nth_prime
    """
    count = 0
    num = 2
    while True:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1


def main():
    # print(nth_prime(1000))
    # cProfile.run('re.compile("foo|bar")')
    # cProfile.run('nth_prime(1000)')
    # cProfile.run('nth_prime(1000)',"nth_prime.pstat")
    # stats= pstats.Stats("nth_prime.pstat")
    # stats.sort_stats(pstats.SortKey.TIME).print_stats(10)
    logging.warning('Watch out!')  # will print a message to the console
    logging.info('I told you so')  # will not print anything    
if __name__ == '__main__':
    main()
