#!/usr/bin/python3

from fullyAssociative import tester as fullyAssociative_tester
from directMapped import tester as directMapped_tester
from setAssociative import tester as setAssociative_tester
from cacheBlocking import tester as cacheBlocking_tester
from cacheOblivious import tester as cacheOblivious_tester

total = 0

total += fullyAssociative_tester.score_fullyAssociative(path="fullyAssociative/", verbose=False)
total += directMapped_tester.score_directMapped(path="directMapped/", verbose=False)
total += setAssociative_tester.score_setAssociative(path="setAssociative/", verbose=False)
total += cacheBlocking_tester.score_cacheBlocking(path="cacheBlocking/", verbose=False)
total += cacheOblivious_tester.score_cacheOblivious(path="cacheOblivious/", verbose=False)

print("Score on assignment: {} out of 150.".format(total))
