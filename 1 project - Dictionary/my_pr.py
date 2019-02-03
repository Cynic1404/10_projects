import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    if w.lower() in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Y or N?" % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            s = 1
            while yn == "N":
                if input("Did you mean %s instead? Y or N?" % get_close_matches(w, data.keys())[s]) == "Y":
                    return data[get_close_matches(w, data.keys())[s]]
                s +=1
                if s == 3:
                    return "We didn't understand your entry"
    else:
        return "This word doesn't exist"

word = input("Your word: ")


output = translate(word)

if type(output) == list:
    s = 1
    for item in output:
        print(s, item)
        s +=1
else:
    print(output)

