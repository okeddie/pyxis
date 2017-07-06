#!/usr/bin/env python
"""
This is a test script to zip some tuples.
"""


def mash():
    tup1 = ('1', '2', '3', '4')
    tup2 = ('red', 'orange', 'green', 'blue')
    mash_lists = zip(tup1, tup2)
    print(mash_lists)


def do_not_mash():
    # type: () -> object
    print("Just testing. tuples not mashed.")

if __name__ == ('__main__'):
    mash()

else:
    do_not_mash()
