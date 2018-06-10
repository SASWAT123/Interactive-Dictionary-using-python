import json
from difflib import get_close_matches as gcm

data = json.load(open("data.json"))

def meaning(word):
    word = word.lower()

    if(word in data):
        return data[word]
    elif(len(gcm(word, data.keys())) > 0):
        option = input("Did you mean %s? Enter Y if yes, N if no: " %gcm(word, data.keys())[0])
        if(option == "Y"):
            return data[gcm(word, data.keys())[0]]
        elif(option == "N"):
            return "The word dosen't exist. Please check again."
        else:
            return "We did not understand your query"
    else:
        return "The word dosen't exist. Please check again."

word = input("Please enter a word: ")
output = meaning(word)
if(type(output) == list):
    for item in output:
        print(item)
else:
    print(output)
