from trie import Trie
import pickle
from edit_dis import edit_dist



def load_word_obj():
    with open("pickle.csv", "rb") as file:
        data = pickle.load(file)

    return data

trie = load_word_obj()

def suggest():
    while True:
        text = input("Enter suf : ")
        if text == "":
            break
        possible = trie.retrieve(text, show = False)
        max = len(text)
        while not possible and max != 0:
            possible = trie.retrieve(text[:max - 1], show = False)
            max -= 1        
        result =  [edit_dist(text, i) for i in possible]
        test = dict(zip(possible, result))
        test = sorted(test.items(), key = lambda x: x[1])
        for i in test[:10]:
            print(i[0])

suggest()

