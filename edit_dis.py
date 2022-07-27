def edit_dist(str1, str2):
    cache = {}
    def recur(i, j):
        if (i, j) in cache:
            return cache[(i, j)]
        elif i == -1:
            return j + 1
        elif j == -1:
            return i + 1
        elif str1[i] == str2[j]:
            return recur(i-1, j-1)
        result = min(recur(i - 1, j), recur(i - 1 , j - 1), recur(i, j - 1)) + 1
        cache[(i, j)] = result
        return result
    return recur(len(str1) - 1 , len(str2) - 1)

#print(edit_dist("a cat" * 10, "the cats" * 10))