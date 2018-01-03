## Write a Python script to concatenate following dictionaries to create a new one.
def main():
    dict = {}
    dict1 = {"Giants":"East Rutherford", "Steelers": "Pittsburgh", "Patriots": "Foxborough" }
    dict2 = {"Yankees": "Bronx", "Mets": "Queens"}
    dict3 = {"Knicks":"Manhattan", "Nets":"Brooklyn"}
    dict.update(dict1)
    dict.update(dict2)
    dict.update(dict3)
    print(dict)

main()