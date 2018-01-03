## Write a Python script to sort (ascending and descending) a dictionary by value.


# By their very definition, Dictionaries cannot be ordered like lists or tuples.
# We must then convert our desired dictionaries to ordered tuples.
# We will do this using the 'operator' module.

import operator

def sortDict(dict):
    sortedbyvalue = sorted(dict.items(), key = operator.itemgetter(1))
    reversebyvalue = sorted(dict.items(), key = operator.itemgetter(1), reverse = True)
    print("Your dictionary sorted in order by value is:", sortedbyvalue)
    print("Your dictionary in descending order by value is:", reversebyvalue)


def main():
    mydict = {"Two": 2, "Three": 3, "Four": 4, "One": 1, "Six": 6, "Five": 5}
    sortDict(mydict)

main()