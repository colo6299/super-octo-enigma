
# This code is bad, and I should feel bad for having written it. 
# The based version of this same thing is in my markov project
def most_common_words(text, num):
    
    word_dictionary = {}
    for word in text.split():
        if word not in word_dictionary:
            word_dictionary[word] = 1
        else:
            word_dictionary[word] += 1

    top_n = [('', 0)] * num

    def _helper(word):
        for index, number in enumerate(top_n):
            if word_dictionary[word] > number[1]:
                top_n.insert(index, (word, word_dictionary[word]))
                top_n.pop()
                return

    for word in word_dictionary:
        _helper(word)
    
    return top_n


if __name__ == "__main__":
    print(most_common_words("# This code is bad, and I should feel bad for having written it. # The based version of this same thing is in my markov project", 4))