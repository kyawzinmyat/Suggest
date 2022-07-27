import csv
from trie import Trie
import pickle


trie = Trie()

def load_trie(word):
    trie.insert(word)

def load_words():
    with open("words.csv", "r") as dic:
        reader = csv.reader(dic)
        for row in reader:
            load_trie(row[0].lower())
            
def suggest():
    text = input("Enter suffix :")
    possible = trie.retrieve(text, show = False)
    max = len(text)
    while not possible and max != 0:
        print("hello")
        possible = trie.retrieve(text[:max - 1])
        max -= 1        
    result =  [edit_dist(text, i) for i in possible]
    test = dict(zip(possible, result))
    test = sorted(test.items(), key = lambda x: x[1])
    for i in test:
        print(i[0])


def load_word_obj(file_name = "pickle.csv"):
    load_words()
    with open(file_name, "wb") as file:
        data = pickle.dump(trie, file)

#load_words()
#
# while True:
#suggest()
#print(trie.retrieve("a", show = False))
#load_word_obj()
