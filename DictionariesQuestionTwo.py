## Write a Python script to add a key to a dictionary.

def addKey(key, value, dict):
    if key not in dict:
        dict[key] = value
    print(dict)

def main():
    myDict = {"Two": 2, "Three": 3, "Four": 4, "One": 1, "Six": 6, "Five": 5}
    addKey("Seven", 7, myDict)

main()