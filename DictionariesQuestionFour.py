##  Write a Python script to check if a given key already exists in a dictionary.

def checkDict(dict):
    cont = "y"
    while cont == "y":
        word = input("Please enter a word. ")
        if word in dict:
             print("This word is in your dictionary.")
        else:
            print("This word is not in your dictionary.")
        cont = input("Would you like to continue? ")

def main():
    dict = {"Giants":"East Rutherford", "Steelers": "Pittsburgh", "Patriots": "Foxborough"}
    checkDict(dict)

main()