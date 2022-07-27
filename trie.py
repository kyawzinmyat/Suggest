class node:
    def __init__(self):
        self.next = [None for i in range(26)]
        self.is_end = True
        self.is_word = False
        

class Trie:
    def __init__(self):
        self.next = node()

    def insert(self, word):
        current_node = self.next
        for char in word:
            index = self.hash(char)
            if current_node.next[index]:
                current_node.next[index].is_end = False
                current_node = current_node.next[index]
            else:
                current_node.next[index] = node()
                current_node.next[index].is_end = False
                current_node = current_node.next[index]
        current_node.is_end = True
        current_node.is_word = True
    

    def hash(self, char):
        return ord(char) - ord("a")

        

    def retrieve(self,surfix, show = True):
        current_node = self.next
        for char in surfix:
            if current_node:
                index = self.hash(char)
                current_node = current_node.next[index]
        result = []
        return self.traverse(current_node, surfix, show, result) if current_node else None

    def traverse(self, current, word, show, result):
        if current.is_end or current.is_word:
            if show:    
                print(word)
            result.append(word)
        for index,node in enumerate(current.next):
            if node:
                self.traverse(node, word + chr(ord("a") + index), show, result)       
        return result
        
        
        

    
#trie = Trie()
#trie.insert("goal")
#trie.insert("goat")
#trie.insert("go")
#
#trie.retrieve("go")